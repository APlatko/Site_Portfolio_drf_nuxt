<template>


  <div id="content-right">


    <div class="section">

      <div class="clearfix">
        <h2>Technical Skills</h2>
      </div>

      <div class="item">
        <div class="skills-section">
          <!-- Skills -->

          <ul class="skills">
            <li>
              <h4>Python</h4>
              <span class="rat3"></span>
            </li>
            <li>
              <h4>SQL</h4>
              <span class="rat4"></span>
            </li>
            <li>
              <h4>Django DRF</h4>
              <span class="rat5"></span>
            </li>
            <li>
              <h4>Nuxt JS</h4>
              <span class="rat4"></span>
            </li>
            <li>
              <h4>Asyncio</h4>
              <span class="rat2"></span>
            </li>
            <li>
              <h4>Selenium</h4>
              <span class="rat6"></span>
            </li>
          </ul>
          <!-- /Skills -->
        </div>
        <!-- <div v-for="cert in certs" :key="cert">
        <h3>{{ cert.course_title}}</h3>
        <img :src="cert.preview_url" style="width:200px">
        </div> -->


      </div><!-- item end -->

      <!-- item end -->

    </div><!-- section end -->

    <div class="section">

      <div class="clearfix">
        <h2>Languages</h2>
      </div>

      <div class="item">
        <h3>English - Upper-intermediate</h3>
        <h3>Polish - Beginner</h3>
        <h3>Belorussian - Native</h3>
        <h3>Russian - Native</h3>



      </div><!-- item end -->


    </div><!-- section end -->

    <div class="section">

      <div class="clearfix">
        <h2>Education</h2>
      </div>

      <div class="item">
        <div v-for="edu in education" :key="edu">

          <h4>{{ edu.field }}</h4>
          <h4>{{ edu.university }}</h4>
          <div class="date">{{ edu.date.slice(0, 4) }}</div>
          <p>{{ edu.degree }}</p>

          <div class="description">
            <img :src="edu.image" style="width:100px">
          </div><!-- description end -->

        </div><!-- item end -->

      </div>
    </div><!-- section end -->

  </div><!-- content-right end -->

</template>

<script>
export default {
  name: "Aside.vue",
  props: ['education']
}

</script>

<style scoped>

</style>