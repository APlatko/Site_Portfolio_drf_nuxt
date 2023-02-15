<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />

        <div id="text">CERTIFICATES</div>
        <div id="stripe"></div>

        <div id="content-left">

          <div class="section">
            <div class="clearfix">
              <h2>Stepik</h2>
            </div>
            <div v-for="cert in certs" :key="cert">
              <div class="item">
                <h3>{{ cert.title }}</h3>
                <h4>{{ cert.organization }}</h4>
                <div class="date">{{ cert.date }}</div>
                <a :href="cert.image" data-lightbox="roadtrip"><img :src="cert.image" height="120"></a>
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
    async asyncData({ params }) {
    const certs = await axios.get(`http://127.0.0.1:8001/api/courses/`);
    const edu = await axios.get(`http://127.0.0.1:8001/api/education/`);
    return {
      certs: certs.data,
      education: edu.data,
    }
  },
  head() {
		return {
			title: "My certificates Anton Platko",
			meta: [
				{ hid: "description", name: "description", content: "Here are my certificates." },
				{ hid: "keywords", name: "keywords", content: "certificates" }
			],
      script: [
        {
          // src: 'js/lightbox.js',
        }
      ],
		}
	},
}
</script>

<style>

</style>
