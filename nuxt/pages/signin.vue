<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />


        <div id="text">SIGN IN</div>
        <div id="stripe"></div>

        <form class="form-signin" @submit.prevent="userLogin">
          <h3>Please enter your login and password</h3>
          <br>
          <label for="inputUsername">Enter login:</label>
          <input id="inputUsername" placeholder="login" required="" v-model="login.username">
          <label for="inputPassword">Enter password:</label>
          <input type="password" id="inputPassword" placeholder="password" required="" v-model="login.password">
          <button type="submit">Singin</button>
        </form>



      </div><!-- content-innertube end -->

      <div class="clear"></div>


    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>

  
<script>
export default {
  layout: "post_detail",
  data() {
    return {
      login: {
        username: '',
        password: ''
      },
    }
  },
  methods: {
    async userLogin() {
      try {
        let response = await this.$auth.loginWith('local', { data: this.login })
        // console.log(response)
        // this.$router.push('/')
        // this.$router.back()
        this.$router.push('/contact')
      } catch (err) {
            console.log(err)
      }
    }
  }
}
</script>

<style scoped>

</style>