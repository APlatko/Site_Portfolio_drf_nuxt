<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />

        <div id="text">SOFTWARE DEVELOPER</div>
        <div id="stripe"></div>
        <div id="content-left">

          <div class="section">

            <div class="clearfix">
              <h2>{{ job.title }}</h2>
            </div>
            {{ job }}

          </div> section end -->

        </div> <!-- content-left end -->
        <Aside :education="education" />

      </div><!-- content-innertube end -->

      <div class="clear"></div>

    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>

<script>
import axios from "axios";
export default {
  async asyncData({ params }) {
    const exp = await axios.get(`http://127.0.0.1:8001/api/experience/${params.slug}`);
    const edu = await axios.get(`http://127.0.0.1:8001/api/education/`);
    return {
      job: exp.data,
      education: edu.data,
    }
  },
}
</script>

<style>

</style>