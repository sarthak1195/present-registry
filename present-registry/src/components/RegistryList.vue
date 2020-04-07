<template>
  <div class="RegistryList">
        <div class="ListTitle">Our Active Registries</div>
            <ul>                
                <li class="RegistryItem"
                    v-bind:key="registry.registryID" 
                    v-for="registry in registries">
                    <router-link class="routerLink" :to="{name: 'Registry', params: {registryID: registry.registryID}}">   
                        {{registry.title}}
                    </router-link>
                </li>
            </ul>
        </div>
</template>

<script>

export default {
    name: 'RegistryList',
    components: {},
    props:["registries"]
}
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
    .RegistryList{
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

    .ListTitle{
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-weight: 700;
        font-size: 250%;
        color: #FFFEF2;
    } 

    ul{
        list-style-type: none;
    }

    .RegistryItem{
        background-color: rgb(255, 203, 246);
        padding: 10px;
        margin: 10px;
        border-bottom: 1px #ccc dotted;
        margin-bottom: 1vh;
        border-radius: 5px;
        font-weight:700;
        color: rgb(63, 63, 63);
    }
</style>