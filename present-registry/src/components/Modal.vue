<template>
    <div>
        <a href="#myModal" @click.prevent="show" class="loginBtn" @click="showModal = true">Login</a>
        <modal name="modal-login">
            <div class="login-form">
                <form action="/examples/actions/confirmation.php" method="post">
                    <h2 class="text-center">Log in</h2>       
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Username" required="required">
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" placeholder="Password" required="required">
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary btn-block">Log in</button>
                    </div>
                    <div class="clearfix">
                        <label class="pull-left checkbox-inline"><input type="checkbox"> Remember me</label>
                        <a href="#" class="pull-right">Forgot Password?</a>
                        <a href="#" class="pull-right ">Register</a>
                    </div>
                </form>
                <p class="text-center"><a href="#">Create an Account</a></p>
            </div>
        </modal>
    </div>     
</template>

<script>
export default {
methods: {
    show () {
        this.$modal.show('modal-login');
    },
    hide () {
        this.$modal.hide('modal-login');
    }
}
}
</script>

<style>
    .login-form form {
        margin-bottom: 15px;
        background: #f7f7f7;
        box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
        padding: 30px;
    }
    .login-form h2 {
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

    a.loginBtn{
        display:inline;
        text-align: center;
        color:  #FFFFFC !important;
        font-weight: 700;
        font-size: 150%;
    }

    a.loginBtn:hover{
        display:inline;
        text-align: center;
        color:   rgb(255, 203, 246) !important;
        font-weight: 700;
        font-size: 150%;
    }
</style>