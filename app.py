#!/usr/bin/env python3
import sys
from flask import Flask, jsonify, abort, request, make_response, session
from flask_restful import reqparse, Resource, Api
from flask_session import Session
import json
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import *
import settings
from flask_cors import CORS
import pymysql.cursors
import cgitb
import cgi
cgitb.enable()

app = Flask(__name__, static_url_path='/static')
app.secret_key = settings.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'peanutButterJam'
app.config['SESSION_COOKIE_DOMAIN'] = settings.APP_HOST
Session(app)
api = Api(app)
CORS(app)

### Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"status": "Bad Request"}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"status": "Resource not found"}), 404)

### Static Endpoint for humans
class Root(Resource):
    def get(self):
        return app.send_static_file('index.html')

api.add_resource(Root,'/')

##################################################
### SIGN-IN (Authentication and Session Management)
##################################################
class SignIn(Resource):
        #
        # Login, start a session and set/return a session cookie
        #
        # Example curl command:
        # curl -i -H "Content-Type: application/json" -X POST -d '{"username": "Casper", "password": "cr*ap"}'
        #       -c cookie-jar http://info3103.cs.unb.ca:xxxxx/signin
        #
        def post(self):
            if not request.json:
                abort(400) # bad request
            # Parse the json
            parser = reqparse.RequestParser()
            try:
                # Check for required attributes in json document, create a dictionary
                parser.add_argument('username', type=str, required=True)
                parser.add_argument('password', type=str, required=True)
                request_params = parser.parse_args()
            except:
                abort(400) # bad request

            # Already logged in
            if request_params['username'] in session:
                response = {'status': 'success'}
                responseCode = 200
            else:
                try:
                    ldapServer = Server(host=settings.LDAP_HOST)
                    ldapConnection = Connection(ldapServer,
                        raise_exceptions=True,
                        user='uid='+request_params['username']+', ou=People,ou=fcs,o=unb',
                        password = request_params['password'])
                    ldapConnection.open()
                    ldapConnection.start_tls()
                    ldapConnection.bind()
                    # At this point we have sucessfully authenticated.
                    session['username'] = request_params['username']
                    response = {'status': 'success' }
                    responseCode = 201
                except (LDAPException, error_message):
                    response = {'status': 'Access denied'}
                    responseCode = 403
                finally:
                    ldapConnection.unbind()

            return make_response(jsonify(response), responseCode)



        # GET: Check for a login
        #
        # Example curl command:
        # curl -i -H "Content-Type: application/json" -X GET -b cookie-jar
        #   http://info3103.cs.unb.ca:61340/signin
        def get(self):
            if 'username' in session:
                response = {'status': 'success'}
                responseCode = 200
            else:
                response = {'status': 'fail'}
                responseCode = 403

            return make_response(jsonify(response), responseCode)

        # DELETE: Logout: remove session
        #
        # Example curl command:
        # curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar
        #   http://info3103.cs.unb.ca:61340/signin

        def delete(self):
            if 'username' in session:
                session.pop('username', None)
                response = {'status': 'success'}
                responseCode = 200
            else:
                response = {'status': 'failed'}
                responseCode = 403
            return make_response(jsonify(response), responseCode)


##################################################
### Presents routing: GET & POST
##################################################
class presents(Resource):
    # GET: Return all present resources
    # Example Request: curl http://info3103.cs.unb.ca:3399/presents
    def get(self):
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            sql = 'getAllPresents'
            cursor = dbConn.cursor()
            cursor.callproc(sql)
            rows = cursor.fetchall()
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Presents": rows}), 200)

    def post(self):
        # Sample CLI Usage:
        # curl -i -X POST -H "Content-Type: application/json"
        # -d '{"presentName": "Bath and Body Works", "presentPrice": 100, "presentDescription": "Hand Lotion Pack of 3"}'
        # http://info3103.cs.unb.ca:3399/presents
        if not request.json or not 'presentName' in request.json or not 'presentDescription' in request.json or not 'presentImageURL' in request.json:
            abort(400)

        presentName = request.json['presentName'];
        presentDescription = request.json['presentDescription'];
        presentImageURL = request.json['presentImageURL'];

        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            sql = 'addPresent'
            cursor = dbConn.cursor()
            sqlArgs = (presentName, presentDescription, presentImageURL)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            dbConn.commit()

            sql = "SELECT LAST_INSERT_ID()"
            cursor = dbConn.cursor()
            cursor.execute(sql)
            dic = cursor.fetchone()
            newPresentID = dic.get('LAST_INSERT_ID()')

        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()

        uri = 'http://' + settings.APP_HOST + ':' + str(settings.APP_PORT)
        # uri = uri + str(request.url_rule) + '/' + str(row['LAST_INSERT_ID()'])
        return make_response(jsonify({"newPresentID": newPresentID}), 201)

class present(Resource):
    def get(self, presentId):
        # Example: curl http://info3103.cs.unb.ca:3399/presents/2
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)

            sql = 'getPresentById'
            cursor = dbConn.cursor()
            sqlArgs = (presentId,)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            if row is None:
                abort(404)

        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Present": row}), 200)

    def delete(self, presentId):
        # Example: curl -X DELETE http://info3103.cs.unb.ca:3399/presents/2
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)
            sql = 'deletePresentById'
            cursor = dbConn.cursor()
            sqlArgs = (presentId,)
            cursor.callproc(sql, sqlArgs)
            dbConn.commit()

        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Present Deleted": presentId}), 204)


class users(Resource):
    def get(self):
        # GET: Return all user resources
        # Example Request: curl http://info3103.cs.unb.ca:3399/users
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
            sql = 'getUsers'
            cursor = dbConn.cursor()
            cursor.callproc(sql)
            rows = cursor.fetchall()
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"users": rows}), 200)

    def post(self):
        # Sample CLI Usage:
        # curl -i -X POST -H "Content-Type: application/json"
        # -d '{"name": "Sarthak", "email": "sgupta5@unb.ca", "username": "sgupta5"}'
        # http://info3103.cs.unb.ca:3399/users
        if not request.json or not 'name' in request.json or not 'email' in request.json or not 'username' in request.json:
            abort(400)

        name = request.json['name'];
        email = request.json['email'];
        username = request.json['username'];

        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            sql = 'addUser'
            cursor = dbConn.cursor()
            sqlArgs = (name, email, username)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            dbConn.commit()
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()

        uri = 'http://' + settings.APP_HOST + ':' + str(settings.APP_PORT)
        # uri = uri + str(request.url_rule) + '/' + str(row['LAST_INSERT_ID()'])
        return make_response(jsonify({"URI": uri}), 201)

class user(Resource):
    def get(self, userId):
        # Example: curl http://info3103.cs.unb.ca:3399/users/5
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)

            sql = 'getUserById'
            cursor = dbConn.cursor()
            sqlArgs = (userId,)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            if row is None:
                abort(404)
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"User": row}), 200)

    def delete(self, userId):
        # Example: curl -X DELETE http://info3103.cs.unb.ca:3399/users/2
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)
            sql = 'deleteUserById'
            cursor = dbConn.cursor()
            sqlArgs = (userId,)
            cursor.callproc(sql, sqlArgs)
            dbConn.commit()

        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"User Deleted": userId}), 204)

class registries(Resource):
    def get(self):
        # GET: Return all registry resources
        # Example Request: curl http://info3103.cs.unb.ca:3399/registry
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
            sql = 'getRegistries'
            cursor = dbConn.cursor()
            cursor.callproc(sql)
            rows = cursor.fetchall()
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Registries": rows}), 200)

    def post(self):
        # Sample CLI Usage:
        # curl -i -X POST -H "Content-Type: application/json"
        # -d '{"registryName": "Baby Shower", "registryOwner": "ali5f"}'
        # http://info3103.cs.unb.ca:3399/registry
        if not request.json or not 'registryTitle' in request.json  or not 'registryDescription' in request.json  or not 'registryImageURL' in request.json:
            abort(400)

        registryTitle = request.json['registryTitle'];
        registryDescription = request.json['registryDescription'];
        registryImageURL = request.json['registryImageURL']

        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            sql = 'addRegistry'
            cursor = dbConn.cursor()
            sqlArgs = (registryTitle,registryDescription, registryImageURL)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            dbConn.commit()
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()

        uri = 'http://' + settings.APP_HOST + ':' + str(settings.APP_PORT)
        # uri = uri + str(request.url_rule) + '/' + str(row['LAST_INSERT_ID()'])
        return make_response(jsonify({"URI": uri}), 201)

class registry(Resource):
    def get(self, registryId):
        # Example: curl http://info3103.cs.unb.ca:3399/registry
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)

            sql = 'getRegistryById'
            cursor = dbConn.cursor()
            sqlArgs = (registryId,)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            if row is None:
                abort(404)
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Registry": row}), 200)

    def delete(self, registryId):
        # Example: curl -X DELETE http://info3103.cs.unb.ca:3399/registry/2
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)
            sql = 'deleteRegistryById'
            cursor = dbConn.cursor()
            sqlArgs = (registryId,)
            cursor.callproc(sql, sqlArgs)
            dbConn.commit()

        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Registry Deleted": registryId}), 204)

class showPresentsInRegistry(Resource):

    def get(self, registryId):
        # Example: curl http://info3103.cs.unb.ca:3399/registry/1/presents
        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)

            sql = 'showRegistryPresents'
            cursor = dbConn.cursor()
            sqlArgs = (registryId,)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchall()
            if row is None:
                abort(404)
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"presentsInRegistry": row}), 200)

class modifyPresentsInRegistry(Resource):

    def post(self, registryId, presentId):
        # Sample CLI Usage:
        # curl -i -X POST -H "Content-Type: application/json"
        # -d '{"presentId": "2"}' http://info3103.cs.unb.ca:8040/registry/2/presents

        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)

            sql = 'addPresentToRegistry'
            cursor = dbConn.cursor()
            sqlArgs = (registryId, presentId)
            cursor.callproc(sql, sqlArgs)
            row = cursor.fetchone()
            dbConn.commit()
        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Present added to Registry": row}), 200)

    def delete(self, registryId, presentId):
        # Example: curl -X DELETE http://info3103.cs.unb.ca:3399/registry/2/presents/1

        try:
            dbConn = pymysql.connect(
                settings.DB_HOST,
                settings.DB_USER,
                settings.DB_PASSWD,
                settings.DB_DATABASE,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)

            sql = 'deletePresentFromRegistry'
            cursor = dbConn.cursor()
            sqlArgs = (registryId, presentId)
            cursor.callproc(sql, sqlArgs)
            dbConn.commit()

        except:
            abort(500)
        finally:
            cursor.close()
            dbConn.close()
        return make_response(jsonify({"Present from Registry Deleted": registryId}), 204)


api = Api(app)

api.add_resource(SignIn, '/signin')

api.add_resource(presents, '/presents')
api.add_resource(present, '/presents/<int:presentId>')

api.add_resource(users, '/users')
api.add_resource(user, '/users/<int:userId>')

api.add_resource(registries, '/registry')
api.add_resource(registry, '/registry/<int:registryId>')

api.add_resource(showPresentsInRegistry, '/registry/<int:registryId>/presents')
api.add_resource(modifyPresentsInRegistry, '/registry/<int:registryId>/presents/<int:presentId>')

if __name__ == '__main__':
    app.run(host=settings.APP_HOST, port=settings.APP_PORT, debug=settings.APP_DEBUG)
