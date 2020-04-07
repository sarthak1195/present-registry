<template>
    <div class="hero-image" >
      <div class="hero-text">
        <h1>{{HeroImageData.title}}</h1>
        <p>{{HeroImageData.description}}</p>
      </div>
    </div>
</template>

<script>
export default {
    name: 'HeroImage',
    components: {
    },
    props: ['HeroImageData'],
    computed: {
        heroImageBG() {
            return {
            }
        }
    }
}
</script>

<style>
    .hero-image {
        /* background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url("../assets/images/HandingPresent.jpg") !important; */
        background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url("../assets/images/HeroLarge.jpg");
        width: 100%;
        height: 30vh; 
        background-size: cover;
        background-repeat: no-repeat;
        background-position: 50% 25%;
        position: relative;
        outline-width: 10px;
        outline-style: solid;
        outline-color:  #8AE1B3;
        box-shadow: 0px 10px 30px grey;
        
    }

    /* Place text in the middle of the image */
    .hero-text {
        font-family: 'Lora';
        text-align: center;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #FFFFFC;
    }
</style>