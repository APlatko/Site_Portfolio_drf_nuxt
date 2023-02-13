<template>


	<div id="page-shadow">

		<div id="page">

			<div class="content-innertube">
				<Navbar />


				<div id="text">PROJECTS</div>
				<div id="stripe"></div>
				<div v-for="project in projects" :key="project">
					<h2> {{ project.title }}</h2>
					<ul id="project-nav">
						<li class="online">
							<a :href="project.link" target="blank"></a>
						</li>

					</ul>

					<div class="clear"></div>

					<p class="project-desc" v-html="project.description"></p>

					<div id="project-lists" class="clearfix">

						<div id="content-left">

							<div class="clearfix">
								<h3 style="margin-bottom: 15px;">Programming languages</h3>
							</div>

							<ul id="arrow" v-for="lang in project.pro_languages" :key="lang">
								<li>{{ lang }}</li>

							</ul>
						</div>

						<div id="content-right">

							<div class="clearfix">
								<h3 style="margin-bottom: 15px;">Technologies</h3>
							</div>

							<ul id="check" v-for="tech in project.technologies" :key="tech">
								<li>{{ tech }}</li>
							</ul>
						</div>

					</div> <!--project-lists end -->
				</div>
			</div><!-- content-innertube end -->



		</div><!-- page end -->

	</div><!-- page-shadow end -->
</template>


<script>
import axios from "axios";
export default {
	async asyncData(ctx) {
		const prj = await axios.get(`http://127.0.0.1:8001/api/projects/`);
		return {
			projects: prj.data,
		}
	},
	head() {
		return {
			title: "Projects Anton Platko",
			meta: [
				{ hid: "description", name: "description", content: "Here are my projects." },
				{ hid: "keywords", name: "keywords", content: "ptojects, Nuxt JS" }
			]
		}
	},
}
</script>

<style>

</style>