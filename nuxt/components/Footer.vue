<template>
  <div id="footer-shadow">
    <div id="footer">

      <div id="footer-innertube">

        <div id="footer-address">
          <h5>Address</h5>
          <ul>
            <li>Sucha 41-20,</li>
            <li>Gdansk,</li>
            <li>Poland</li>
          </ul>
        </div><!-- footer-address end -->

        <div id="footer-contact">
          <h5>Contact</h5>
          <ul>
            <li>+48 515 262 031</li>
            <li><nuxt-link to="mailto:antonioplatko@gmail.com"
                title="Send me an email">antonioplatko@gmail.com</nuxt-link></li>
            <li><nuxt-link to="/contact">Leave a comment<span class="raquo">&#187;</span></nuxt-link></li>
          </ul>
        </div><!-- footer-contact end -->

        <div id="footer-social">
          <h5>Social</h5>
          <ul>
            <li><a href="https://www.linkedin.com/in/anton-platko/" title="" target="blank"><img src="/img/linkedin.png"
                  alt="linkedin" title="My Linkedin profile"></a></li>
            <li><a href="https://github.com/APlatko?tab=repositories" title="" target="blank"><img
                  src="/img/github_32.png" alt="github" title="My Github profile"></a></li>
            <li><a href="https://gitlab.com/users/antonioplatko/projects" title="" target="blank"><img
                  src="/img/gitlab_32.png" alt="gitlab" title="My Gitlab profile"></a></li>
            <li><a href="skype:anterica" title=""><img src="/img/skype_32.png" alt="skype" title="My Skype profile"></a>
            </li>

          </ul>
        </div><!-- footer-social end -->

        <div id="footer-resume">
          <h5>My resume</h5>
          <div id="download-resume"><a href="/Anton_Platko_JSD_CV.pdf" download=""></a></div>
        </div><!-- footer-resume end -->

        <div class="clear"></div>

        <ul id="footer-nav">
          <li><nuxt-link to="/">Profile</nuxt-link></li>
          <li><nuxt-link to="/certificates">Certificates</nuxt-link></li>
          <li><nuxt-link to="/projects">Projects</nuxt-link></li>
          <li><nuxt-link to="/about">About me</nuxt-link></li>
          <li><nuxt-link to="/contact">Contact</nuxt-link></li>
        </ul>

        <div id="go-top"><a href="#"></a></div>

        <div class="clear"></div>

      </div> <!-- footer-innertube end -->

    </div><!-- footer end -->
  </div>
</template>


<script>
export default {
  name: "Footer",
}
</script>

<style scoped>

</style>