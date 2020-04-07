<template>
    <div class="CreateRegistry">
        <HeroImage v-bind:HeroImageData="indexData"/>
        <div class="create-registry-form">
            <div class="form-background">
                <form action="" method="">
                    <h2 class="text-center">Registry Name</h2>       
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Name" required="required" >
                    </div>
                    <h2 class="text-center">Registry Description</h2>
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Description" required="required" v-model="password">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary btn-block">Submit Registry</button>
                    </div>
                </form>
            </div>
        </div>
    </div> 
</template>

<script>
import HeroImage from '../components/HeroImage.vue'

export default {
    name: 'CreateRegistry',
    components: {HeroImage},
    data() {
        return {
            indexData: {
                title: "Create a Registry",
                description: "Fill in the necessary fields"
            }
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