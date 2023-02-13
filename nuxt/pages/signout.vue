<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />

        <div id="text">SIGN OUT</div>
        <div id="stripe"></div>
        <div>You are successfully signed out</div>

      </div><!-- content-innertube end -->

      <div class="clear"></div>

    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>



<script scope>
export default {
  async created() {
    await this.$auth.logout()
    this.$router.push('/contact')
  }
}
</script>