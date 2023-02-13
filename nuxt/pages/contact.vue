<template>

	<div id="page-shadow">

		<div id="page">

			<div class="content-innertube">
				<Navbar />


				<div id="text">CONTACT</div>

				<div id="stripe"></div>

				<ul id="contact-columns" class="clearfix">

					<li>
						<img src="img/phone-icon.png" alt="" title="">
						<p>+48 515 262 031</p>
					</li>

					<li>
						<img src="img/mail-icon.png" alt="" title="">
						<p><a href="mailto:antonioplatko@gmail.com">antonioplatko@gmail.com</a></p>
					</li>

					<li class="address">
						<img src="img/address-icon.png" alt="" title="">
						<p>
							Sucha 41-20,
							<br />
							Gdansk,
							<br />
							Poland
						</p>
					</li>

				</ul><!-- contact-columns end -->
				<!-- 
				<div v-else>
						<h6 class="card-header"><nuxt-link to="/signin">Authorise</nuxt-link> or <nuxt-link
								to="/register">register</nuxt-link> to leave a comment</h6>
				</div> -->

				<div>
					<span v-if="user">
						<h4 class="card-header">You are singned in as:&nbsp;<b>{{ user.username }}</b>
							&nbsp;&nbsp;&nbsp;&nbsp;<nuxt-link no-prefetch to="/signout">Sign out</nuxt-link></h4>
					</span>
				</div>

				<div id="form-container" class="clearfix">

					<div v-if="loggedIn">
						<form id="contact-form" name="contact-form" @submit.prevent="addComment">

							<div id="content-left">

								<ul id="contact-info">

									<li>
										<label for="message">* Message:</label>
										<textarea name="message" id="message" cols="35" rows="5"
											v-model="new_comment"></textarea>
									</li>

								</ul>

							</div><!-- content-left end -->


							<div id="content-right">

								<ul id="contact-info">

									<li>
										<label for="name">* Company:</label>
										<input type="text" name="company" id="name" v-model="company" value="" />
									</li>

									<li>
										<label for="email">* Email:</label>
										<input type="text" name="email" id="email" v-model="email" value="" />
									</li>

								</ul>

								<div id="submit-btn"><input type="submit" :disabled='!isComplete' name="button"
										id="button" class="submit" value="Submit" /></div>
							</div><!-- content-right end -->

						</form>
					</div>
					<div v-else>
						<h3 class="card-header"><nuxt-link to="/signin">Authorise</nuxt-link> or <nuxt-link
								to="/register">register</nuxt-link> to leave a comment</h3>
					</div>



				</div><!-- form-container end -->

				<Comments :comments="comments" />


			</div><!-- content-innertube end -->

		</div><!-- page end -->

	</div><!-- page-shadow end -->
</template>


<script>
import axios from "axios";
import Comments from "@/components/Comments";
export default {
	components: {
		Comments
	},
	data() {
		return {
			new_comment: '',
			company: '',
			email: '',
		}
	},
	methods: {
		async addComment() {
			try {
				let response = await this.$axios.post(`http://127.0.0.1:8001/api/comments/`, {
					username: this.user.username,
					text: this.new_comment,
					company: this.company,
					email: this.email,
				})
				console.log(email)
				this.new_comment = '';
				this.company = '';
				this.email = '';
				this.comments.splice(0, 0, response.data)
				console.log(response)
			} catch (err) {
				console.log(err)
			}
		},
	},

	async asyncData({ ctx }) {
		const comment = await axios.get(`http://127.0.0.1:8001/api/comments/`);
		return {
			comments: comment.data,
		}
	},
	computed: {
		loggedIn() {
			return this.$auth.loggedIn
		},
		user() {
			return this.$auth.user
		},
		isComplete() {
			return this.new_comment;
		}
	},
	head() {
		return {
			title: "Contacts Anton Platko",
			meta: [
				{ hid: "description", name: "description", content: "Here are my contacts." },
				{ hid: "keywords", name: "keywords", content: "conacts" }
			]
		}
	},
}
</script>

<style scoped>

</style>

