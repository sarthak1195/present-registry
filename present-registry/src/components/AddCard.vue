<template>
  <div class="AddCard">
      <a href="#addpresent" @click.prevent="show" class="AddCardModalLink" @click="showModal = true">
        <div class="presentCard-inner">
            <div class="presentCard-title">
                <h2>Add A Present</h2>
            </div>
            <div class="presentCard-image-wrap">
                <div class="add-image">?</div>
            </div>
        </div>
      </a>
        
      <modal name="modal-add-present">
            <div class="login-form">
                <form action="" @submit.prevent="addPresentToList" method="">
                    <h2 class="text-center">Add a Present</h2>      
                    <div class="form-group">
                        Name: <input type="text" class="form-control" placeholder="Present Name" required="required" v-model="presentName"> 
                    </div>
                    <div class="form-group">
                        Description: <input type="text" class="form-control" placeholder="Present Description" required="required" v-model="presentDescription">
                    </div>
                    <div class="form-group">
                        Image src: <input type="text" class="form-control" placeholder="Image URL" required="required" v-model="presentImageURL">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary btn-block" >Add Present</button>
                        <!-- <button type="submit" class="btn btn-primary btn-block" @click="addPresent" >Add Present</button> -->
                    </div>
                </form>
            </div>
        </modal>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "AddCard",
    props: ['registryID'],
    methods: {
        show () {
            this.$modal.show('modal-add-present');
        },
        showAddPresent () {
            this.$modal.hide('modal-add-present');
        },
        hide () {
            this.$modal.hide('modal-add-present');
        }, 
        addPresentToList () {

        },

        addPresent () {
            if (this.presentName != "" && this.presentDescription != "" && this.presentImageURL != "") {
                
                // API CALL #1 - Add the present to presents table

                axios
                .post(this.serviceURL+'/presents', {
                    presentName: this.presentName,
                    presentDescription: this.presentDescription, 
                    presentImageURL: this.presentImageURL
                })
                .then(function (response) {
                    this.presentID = response.data.newPresentID
                    this.addPresentToRegistry();
                })
                .catch(function (error) {
                    alert("Present Not added: " + error)
                })
            }
            else {
                alert("Present Form Inputs missing, need all 3!")
            }
        },

        addPresentToRegistry () {
            // API CALL #2 - Add the present to the registry (registryID and presentID needed)
            axios
            .post(this.serviceURL+'/registry/'+this.registryID+'/presents/'+this.presentID)
            .then(function (response) {
                alert("Present added to registry" + response.data)
                // Show New Present on Registry Page
                // Reload page if necessary 
            })
            .catch(function (error) {
                alert("Present could not be attached to the Registry: " + error)
            })
        }

    },
    data() {
        return {
            presentName: String,
            presentDescription: String,
            src:String,

            // Edit - Apr 8 (11:45 PM) 
            serviceURL: "http://info3103.cs.unb.ca:8040",
            presentImageURL: String,
            // Something similar if this doesn't work
            presentID: ''
        }
    }
}
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

    .AddCard {
        flex: 1 1 10%;
        width: 100%;
        padding: 20px;
        cursor: pointer;
    }

    .AddCardModalLink {
        text-decoration: none !important;
        color: black;
    }

    .AddCardModalLink:hover {
        text-decoration: none !important;
        color: black;
    }

    .presentCard-inner {
        position: relative;
        padding: 25px;
        box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
        background-color: rgb(255, 179, 217, 0.35);
        border-radius: 25px;
        max-width: 350px;
    }

    .presentCard-inner:hover {
        position: relative;
        padding: 25px;
        box-shadow: 0px 0px 100px rgba(0, 0, 0, 0.25);
        background-color: rgb(255, 179, 217, 0.35);
        border-radius: 25px;
        max-width: 350px;
    }

    .presentCard-image-wrap {
        width: 100%;
    }
    
    .add-image {
        color: white;
        text-align: center;
        background-color: rgb(166, 255, 184, 0.75);
        font-size: 1000%;
        border-radius: 100px;
    }

    .presentCard-title {
        font-family: 'Playfair Display', serif;
        font-size: 350px !important;
        background-color: rgb(166, 255, 184, 0.75);
        border-radius: 100px;
        box-shadow: 0px 0px 25px rgba(255, 255, 255, 0.505);
        text-align: center;
    }

    .v--modal {
        height: 42vh!important;
    }
</style>