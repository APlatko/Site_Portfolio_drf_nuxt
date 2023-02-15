<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />

        <div id="text">SEARCH RESULTS</div>
        <div id="stripe"></div>

        <div id="content-left">

          <div class="section">

            <div class="clearfix">
              <h2>Founded -{{ q_result.count }}- results for query "{{ query }}"</h2>
            </div>

            <div v-for="result in q_result.results" :key="result">
              <div class="item">
                <h3>{{ result.title }}</h3>
                <h4>{{ result.company }}</h4>

                <div class="description">
                  <p class="margin" v-html="result.description"></p>
                  <p>{{ result.skills.join(" | ") }}</p>

                  <div class="date_more"><nuxt-link :to="`/experience/${result.slug}/`" class="">see more</nuxt-link>
                  </div>
                </div>


              </div>
            </div>


          </div> <!--section end -->

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
  watchQuery: ['q'],
  async asyncData({ route }) {
    const { data } = await axios.get(`http://localhost:8001/api/experience/?q=${route.query.q}`);
    const edu = await axios.get(`http://127.0.0.1:8001/api/education/`);
    return {

      q_result: data,
      education: edu.data,
      query: route.query.q,
    }
  },
}
</script>

<style>

</style>