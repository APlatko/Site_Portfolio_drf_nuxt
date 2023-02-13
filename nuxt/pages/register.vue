<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />

        <div id="text">REGISTER</div>
        <div id="stripe"></div>

        <form class="form-signin" @submit.prevent="userRegister">
          <h3>Please create your login and password</h3>
          <br>
          <label for="inputUsername">Enter login:</label>
          <input id="inputUsername" placeholder="login" required="" v-model="register.username">
          <br>
          <br>
          <label for="inputPassword">Enter password:</label>
          <input type="password" id="inputPassword" placeholder="password" required="" v-model="register.password">
          <label for="ReInputPassword">Repeat password:</label>
          <input type="password" id="ReInputPassword" placeholder="repeat password" required=""
            v-model="register.password2">
          <br>
          <br>
          <button type="submit">Register</button>
        </form>

      </div><!-- content-innertube end -->

      <div class="clear"></div>

    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>

  
<script>
export default {
  data() {
    return {
      register: {
        username: '',
        password: '',
        password2: '',
      },
    }
  },
  methods: {
    async userRegister() {
      try {
        let response = await this.$axios.post('/api/register/', {
          username: this.register.username,
          password: this.register.password,
          password2: this.register.password2
        })
        await this.$auth.loginWith('local', {
          data: {
            username: this.register.username,
            password: this.register.password
          },
        })
        this.$router.back()
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>

<style scoped>

</style>