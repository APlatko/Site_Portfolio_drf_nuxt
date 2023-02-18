<template>
  <div id="page-shadow">

    <div id="page">
      <div class="content-innertube">
        <Navbar/>
        <div id="text">SOFTWARE DEVELOPER</div>

        <div id="stripe"></div>

        <div id="content-left">
          <div class="section">

            <div class="clearfix">
              <h2>Work Experience</h2>
            </div>
            <div class="ordering">
              <p>sort by date:</p>
              <nuxt-link :to="`/?ord=start`"><img src="/img/top.png"
                  alt="top" title="sort asc"></nuxt-link>
              <nuxt-link :to="`/?ord=-start`"><img src="/img/top.png"
                  alt="down" title="sort desc" style="transform: rotate(180deg)"></nuxt-link>
            </div>
            <div v-for="exp in experience" :key="exp.slug">
              <div class="item">
                <h3>{{ exp.title }}</h3>
                <h4>{{ exp.company }}</h4>

                <div v-if="exp.end === null" class="date">{{ exp.start.slice(0, 4) }} - present</div>
                <div v-else class="date">{{ exp.start.slice(0, 4) }} - {{ exp.end.slice(0, 4) }}</div>

                <div class="description">
                  <p class="margin" v-html="exp.description"></p>
                  <p>Skills: {{ exp.skills.join(" | ") }}</p>
                </div><!-- description end -->

                <div class="date_more">
                  <nuxt-link :to="`/experience/${exp.slug}/`" class="">see more</nuxt-link>

                </div>

              </div><!-- item end -->
            </div>
          </div><!-- section end -->

        </div><!-- content-left end -->
        <Aside :education="education"/>
      </div><!-- content-innertube end -->
      <div class="clear"></div>

    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>

<script>
import axios from "axios";

export default {
  watchQuery: ['ord'],
  async asyncData({route}) {
    let sorting = route.query.ord !== undefined ? `?ord=${route.query.ord}` : '';
    const {data} = await axios.get(`http://127.0.0.1:8001/api/experience/${sorting}`);
    const edu = await axios.get(`http://127.0.0.1:8001/api/education/`);
    return {

      experience: data.results,
      education: edu.data,
    }
  },
  head() {
    return {
      title: "Python developer Anton Platko",
      meta: [
        {
          hid: "description",
          name: "description",
          content: "This is my profile page. You can see my working experience."
        },
        {
          hid: "keywords",
          name: "keywords",
          content: "python, developer, fullstack, backend, SQL, parsing, Selenium, MySQL, Django, Rest framework, DRF, MS Excel"
        }
      ]
    }
  },
}
</script>

<style>

</style>
