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
              <h2>Work Experience</h2>
            </div>
            <div>
              <div class="item">

                <h3>{{ job.title }}</h3>
                <h4>{{ job.company }}</h4>

                <div v-if="job.end === null" class="date">{{ job.start.slice(0, 4) }} - present</div>
                <div v-else class="date">{{ job.start.slice(0, 4) }} - {{ job.end.slice(0, 4) }}</div>

                <div class="description">
                  <p class="margin" v-html="job.contest"></p>
                  <p>Skills: {{ job.skills.join(" | ") }}</p>
                </div><!-- description end -->

                <div class="date_more">
                  <p>Link of the company <a :href="job.link" target="_blank">link</a></p>

                </div>

              </div><!-- item end -->
            </div>
          </div><!-- section end -->

        </div><!-- content-left end -->
        <Aside :education="education"/>
      </div>
      <div class="clear"></div>

    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>

<script>
import axios from "axios";

export default {
  async asyncData({params}) {
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