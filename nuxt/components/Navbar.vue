<template>
  <div id="header">
    <h1><nuxt-link to="/">Anton Platko</nuxt-link></h1>
    <div id="asd">

      <div id="aaa">
        <form>
          <input name="q" id="input" v-model="q" type="text" placeholder="Enter search query" aria-label="Search">
          <button id="button" type="submit" @click.stop.prevent="submit()">Search</button>
        </form>
      </div>
      <div>
        <ul id="main-nav">
          <li><nuxt-link exact no-prefetch active-class="current" to="/">Profile</nuxt-link></li>
          <li><nuxt-link no-prefetch active-class="current" to="/certificates">Certificates</nuxt-link></li>
          <li><nuxt-link no-prefetch active-class="current" to="/projects">Projects</nuxt-link></li>
          <li><nuxt-link no-prefetch active-class="current" to="/about">About me</nuxt-link></li>
          <li><nuxt-link no-prefetch active-class="current" to="/contact">Contact</nuxt-link></li>
        </ul>
      </div>
    </div>
    <div class="clear"></div>
  </div><!-- header end -->
</template>

<script>
export default {
  //   name: "Navbar",
  data() {
    return {
      q: null,

    }
  },
  methods: {
    submit() {
      this.$router.push("/search?q=" + this.q);
    }
  },
  computed: {
    loggedIn() {
      return this.$auth.loggedIn
    },
    user() {
      return this.$auth.user
    }
  }
}
</script>

<style scoped>

</style>