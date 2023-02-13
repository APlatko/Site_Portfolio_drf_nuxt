<template>
  <div>
    <Nuxt />
    <Footer />
  </div>
</template>


<script>
import Navbar from "~/components/Navbar";
// import Aside from "~/components/Aside";
import Footer from "~/components/Footer";


export default {
  components: {
    Navbar,
    // Aside,
    Footer,
  },
  head() {
    return {
      link: [
        { rel: "canonical", href: `http://localhost:3001${this.$route.path}` }
      ]
    }
  },
};
</script>

<style>

</style>