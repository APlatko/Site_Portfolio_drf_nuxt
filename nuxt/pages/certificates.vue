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
                <!-- <a :href="cert.image" target="blank"><img :src="cert.image" height="180"></a> -->


                <a :href="cert.image" data-lightbox="roadtrip" target="blank"><img :src="cert.image" height="120"></a>
                <!-- <a href="img/aboutme.png" data-lightbox="aboutme" data-title="My caption">Image #1</a> -->
                <!-- <img src="img/aboutme.png" data-lightbox="aboutme" data-title="My caption"> -->
                <!-- <button><a :href="cert.image" target="_blank">look2 certificate</a></button> -->
                <!-- <div class="save-btn">
                  <button @click="showModal = true"><a :src="cert.image">look3 certificate</a></button>
              </div> -->

                <!-- <a :href="cert.preview_url">look certificate</a> -->
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
  head() {
    return {
      script: [
        {
          src: 'js/lightbox.js',
        }
      ],
    }
  },

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
			]
		}
	},
}
</script>

<style>

</style>
