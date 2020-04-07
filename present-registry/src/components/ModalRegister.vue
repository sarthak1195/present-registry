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
    @import '../assets/styles/AuthenticationModal.css';
</style>