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
                        <input type="text" class="form-control" placeholder="Present Name" required="required"> 
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Present Description" required="required">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Image URL" required="required">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary btn-block" @click="$emit('authenticated')" >Add Present</button>
                    </div>
                </form>
            </div>
        </modal>
  </div>
</template>

<script>
export default {
    name: "AddCard",
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

        }
    },
    data() {
        return {
            presentName: String,
            presentDescription: String,
            src:String
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
</style>