<template>
    <div>
        <a href="#register" @click.prevent="show" class="registerBtn" @click="showModal = true">Register</a>
        <modal name="modal-register" :height="420">
            <div class="register-form">
                <form action="#" method="post">
                    <h2 class="text-center">Register</h2>       
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Name" required="required">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control" placeholder="Email" required="required">
                    </div>                    
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Username" required="required">
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" placeholder="Password" required="required">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary btn-block">Register</button>
                    </div>
                    <div class="text-sm font-normal text-center">
                        <p>Already have an account? <a href="#" class="text-blue-600 hover:text-blue-800" @click.prevent="showLogin" @keydown.tab.exact.prevent="">Login</a></p>
                    </div>
                </form>
            </div>
        </modal>
    </div>     
</template>

<script>
export default {
methods: {
    show () {
        this.$modal.show('modal-register');
    },
    showLogin () {
        this.$modal.show('modal-login');
        this.$modal.hide('modal-register');
    },
    hide () {
        this.$modal.hide('modal-register');
    }
}
}
</script>

<style>
    .register-form form {
        margin-bottom: 15px;
        background: #f7f7f7;
        box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
        padding: 30px;
    }
    .register-form h2 {
        margin: 0 0 15px;
    }
    .form-control, .btn {
        min-height: 38px;
        border-radius: 2px;
    }
    .btn {        
        font-size: 15px;
        font-weight: bold;
        background-color: #FF99CC !important;
        border: none !important;
    }

    a.registerBtn{
        display:inline;
        text-align: center;
        color:  #FFFFFC !important;
        font-weight: 700;
        font-size: 150%;
    }

    a.registerBtn:hover{
        display:inline;
        text-align: center;
        color:   rgb(255, 203, 246) !important;
        font-weight: 700;
        font-size: 150%;
    }
</style>