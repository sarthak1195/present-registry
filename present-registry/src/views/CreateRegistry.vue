<template>
    <div class="CreateRegistry">
        <HeroImage v-bind:HeroImageData="indexData"/>
        <div class="create-registry-form">
            <div class="form-background">
                <div v-if="!created">
                    <form action="" method="">
                        <h2 class="text-center">Registry Name</h2>       
                        <div class="form-group">
                            <input type="text" class="form-control" name="registryTitle" v-model="registryTitle" required="required" >
                        </div>
                        <h2 class="text-center">Registry Description</h2>
                        <div class="form-group">
                            <input type="text" class="form-control" name="registryDescription" required="required" v-model="registryDescription">
                        </div>
                        <h2 class="text-center">Registry Image</h2>
                        <div class="form-group">
                            <input type="text" class="form-control" name="registryImageURL" required="required" v-model="registryImageURL">
                        </div>                    
                        <div class="form-group">
                            <button type="button" class="btn btn-primary btn-block" v-on:click="createRegistry()">Create Registry</button>
                        </div>
                    </form>
                </div>
                <div class="createdButton" v-if="created">
                    <router-link class="routerLink" to="/">
                        <button type="button" class="btn btn-primary btn-block" v-on:click="disableCreated()">Go back to Registries</button>
                    </router-link>
                </div> 
            </div>
        </div>
    </div> 
</template>

<script>
import HeroImage from '../components/HeroImage.vue'
import axios from 'axios'

export default {
    name: 'CreateRegistry',
    components: {HeroImage},
    data() {
        return {
            indexData: {
                title: "Create a Registry",
                description: "Fill in the necessary fields"
            },
            serviceURL: "http://info3103.cs.unb.ca:8040",
            created: false,
            registryTitle: '',
            registryDescription: '',
            registryImageURL: '',
            
        }
    },
    methods: {
        createRegistry() {
            axios
            .post(this.serviceURL+'/registry', {
                registryTitle: this.registryTitle,
                registryDescription: this.registryDescription,
                registryImageURL: this.registryImageURL
            })
            .then(function (response) {
                // created = true;
                alert("Registry Created: " + response.data)
            })
            .catch(function (error) {
                alert("Error while adding registry: " + error)
            })
        },
        disableCreated() {
            // created = false;
        }
    }
}
</script>

<style scoped>
    .create-registry-form {
        padding: 35px;
        background-color:  rgb(239, 77, 150, .65);
        width: 100%;
        background-position: 50% 25%;
        max-width: 75vh;
        margin: 0 auto;
        margin-top: 7.5vh;
        border-radius: 10px;
        border-color: #8AE1B3;
        border-style: solid;
        border-width: 5px;
        box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
    }

    h2 {
        color: white;
    }
</style>