<template>
    <div>
        <a href="#login" @click.prevent="show" class="loginBtn" @click="showModal = true">Login</a>
        <modal name="modal-login">
            <div class="login-form">
                <form action="" @submit.prevent="login" method="">
                    <h2 class="text-center">Log in</h2>       
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Username" required="required" v-model="username">
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" placeholder="Password" required="required" v-model="password">
                    </div>
                    <div class="form-group">

                        <!-- <button type="submit" class="btn btn-primary btn-block" @click="$emit('authenticated')" >Log in</button> -->
                        <button type="submit" class="btn btn-primary btn-block" @click="login()" >Log in</button>

                    </div>
                    <div class="text-sm font-normal text-center">
                        <p>Don't have an account? <a href="#" class="text-blue-600 hover:text-blue-800" @click.prevent="showRegister" @keydown.tab.exact.prevent="">Register</a></p>
                    </div>
                </form>
            </div>
        </modal>
    </div>     
</template>

<script>
import axios from 'axios'

export default {
    
    name: "ModalLogin",
    data() {
        return {
            serviceURL: "http://info3103.cs.unb.ca:8040",
            username: '',
            password: '',
        }
    },
    methods: {
        show () {
            this.$modal.show('modal-login');
        },
        showRegister () {
            this.$modal.show('modal-register');
            this.$modal.hide('modal-login');
        },
        hide () {
            this.$modal.hide('modal-login');
        },
        login () {
            if (this.username != "" && this.password != "") {
                axios
                .post(this.serviceURL+'/signin', {
                    username: this.username,
                    password: this.password 
                })
                .then(function (response) {
                    if (response.data.status == "success") {
                    
                        this.$emit('authenticated')

                    }
                })
                .catch(function (error) {
                    this.password = ""
                    alert("Incorrect username or password! Try again.")
                    console.log(error)
                })
            }
            else {
                alert("Username or Password cannot be empty")
            }
        }
    }
}
</script>

<style scoped>
    @import '../assets/styles/AuthenticationModal.css';
</style>