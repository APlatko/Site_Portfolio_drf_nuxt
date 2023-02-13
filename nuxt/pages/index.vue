<template>
  <div id="page-shadow">

    <div id="page">

      <div class="content-innertube">
        <Navbar />
        <!-- <div id="header">
        
          <h1>John William Doe</h1>
          
          <ul id="main-nav">
            <li class="current"><a href="index.html">Resume</a></li>
            <li><a href="portfolio.html">Portfolio</a></li>
            <li><a href="project.html">Project</a></li>
            <li><a href="about.html">About me</a></li>
            <li><a href="contact.php">Contact</a></li>
          </ul>
          
          <div class="clear"></div>
          
        </div> --> <!-- header end -->

        <div id="text">SOFTWARE DEVELOPER</div>
        <!-- <div id="text"><img src="img/resume.png" alt="" title=""></div> -->
        <div id="stripe"></div>



        <div id="content-left">

          <!-- <div class="section">
        
            <div class="clearfix"><h2>Personal details</h2></div>
            
            <div class="item">
            
              <ul id="personal-details">
                <li><span>Name:</span>John William Doe</li>
                <li><span>Born on:</span>July 27, 1989</li>
                <li class="clearfix"><span>Address:</span>
                  <ul id="address-lines">
                    <li>123 Street Address,</li>
                    <li>Lovely City,</li>
                    <li>My Country</li>
                  </ul>
                </li>
                <li><span>Phone:</span>0 123 456 789</li>
                <li><span>Email:</span><a href="mailto:#">address@email.com</a></li>
              </ul>
              
            </div> --><!-- item end
          </div>section end -->


          <div class="section">

            <div class="clearfix">
              <h2>Work Experience</h2>
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
                  <!-- <span v-for="skill in exp.skills" :key="skill"> -->
                  <!-- <nuxt-link :to="`/skills/${skill}`" class=""> #{{ skill }}</nuxt-link> -->
                  <!-- <span>{{ skill }}  </span> -->
                  <!-- </span> -->
                </div><!-- description end -->

                <div class="date_more">
                  <nuxt-link :to="`/experience/${exp.slug}/`" class="">see more</nuxt-link>

                </div>

              </div><!-- item end -->

              <!--<div class="item last">
            
              <h3>Fashion designer</h3>
              <h4>Fashion and Style Company</h4>
              <div class="date">2007 - 2008</div>
              
              <div class="description">
                <p class="margin">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed risus dui, bibendum ac aliquet non, volutpat quis elit.</p>
                <ul>
                  <li>Praesent venenatis est quis ipsum fringilla ut pulvinar lectus mollis.</li>
                  <li>Curabitur condimentum elementum purus, ut dapibus nunc pulvinar id.</li>
                  <li>Fusce id neque dictum felis pharetra elementum in id erat.</li>
                </ul>
              </div>  -->
              <!-- description end -->
              <!--
              <h4 class="refer">References</h4>
              <p>Mr. Jet Lee <br>Main designer<br>000 123 456 789</p>
              
            </div>--><!-- item end -->
              <!-- <div class="">
                <nuxt-link :to="`/experience/${exp.slug}/`" class="">see more</nuxt-link>

              </div> -->

            </div>
          </div><!-- section end -->

        </div><!-- content-left end -->



        <Aside :education="education" />
      </div><!-- content-innertube end -->

      <div class="clear"></div>

      <!-- <div id="footer">-->

      <!--<div id="footer-innertube">
        
          <div id="footer-address">
            <h5>Address</h5>
            <ul>
              <li>123 Street Address,</li>
              <li>Lovely City,</li>
              <li>My Country</li>
            </ul>
          </div>--><!-- footer-address end -->

      <!--<div id="footer-contact">
            <h5>Contact</h5>
            <ul>
              <li>000 123 456 789</li>
              <li><a href="mailto:#" title="Send me an email">address@email.com</a></li>
              <li><a href="contact.php">Contact form<span class="raquo">&#187;</span></a></li>
            </ul>
          </div>--><!-- footer-contact end -->

      <!--<div id="footer-social">
            <h5>Social</h5>
            <ul>
              <li><a href="#" title=""><img src="img/twitter.png" alt="twitter" title="My Twitter profile"></a></li>
              <li><a href="#" title=""><img src="img/facebook.png" alt="facebook" title="My Facebook profile"></a></li>
              <li><a href="#" title=""><img src="img/flickr.png" alt="flickr" title="My Flickr profile"></a></li>
              <li><a href="#" title=""><img src="img/linkedin.png" alt="linkedin" title="My Linkedin profile"></a></li>
            </ul>
          </div>--><!-- footer-social end -->

      <!--<div id="footer-resume">
            <h5>My resume</h5>
            <div id="download-resume"><a href="#"></a></div>
          </div>--><!-- footer-resume end -->

      <!--<div class="clear"></div>
          
          <ul id="footer-nav">
            <li><a href="index.html">Resume</a></li>
            <li><a href="portfolio.html">Portfolio</a></li>
            <li><a href="about.html">About me</a></li>
            <li><a href="contact.php">Contact</a></li>
          </ul>
          
          <div id="go-top"></div>
          
          <div class="clear"></div>
        
        </div>--><!-- footer-innertube end -->

      <!--</div>--><!-- footer end -->

    </div><!-- page end -->

  </div><!-- page-shadow end -->
</template>

<script>
// import Navbar from "~/components/Navbar";
import axios from "axios";
export default {
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8001/api/experience/`);
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
        { hid: "description", name: "description", content: "This is my profile page. You can see my working experience." },
        { hid: "keywords", name: "keywords", content: "python, developer, fullstack, backend, SQL, parsing, Selenium, MySQL, Django, Rest framework, DRF, MS Excel" }
      ]
    }
  },
}
</script>

<style>

</style>


<!-- <script>
import axios from "axios";
export default {
  watchQuery: ['page'],
  data() {
    return {
      posts: [],
      total: [],
      next: [],
      previous: [],
      current_page: 0
    }
  },
  async asyncData({route}) {

    let page = route.query.page !== undefined ? `?page=${route.query.page}` : '';
    const { data } = await axios.get(`http://127.0.0.1:8001/api/experience/`);
    console.log(data)

    let next = data.next != null ? data.next.split('/')[5] : data.next;
    let previous = data.previous != null ? data.previous.split('/')[5] : data.previous;
    let current_page = route.query.page
    return {
      posts: data.results,
      total: Math.ceil(data.count / 3),
      next: next,
      previous: previous,
      current_page: Number(current_page)
    }
  },
  head() {
    return {
      title: "Главная страница блога",
      meta: [
        { hid: "description", name: "description", content: "Это дискрипшн тут мы пишем текст не более 250 символов."},
        { hid: "keywords", name: "keywords", content: "перечисляем, ключевые, слова, для, главной"}
      ]
    }
  },
}
</script>

<style>

</style> -->