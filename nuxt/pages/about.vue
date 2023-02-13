<template>

	<div id="page-shadow">

		<div id="page">

			<div class="content-innertube">
				<Navbar />

				<div id="text">ABOUT ME</div>
				<div id="stripe"></div>

				<div id="about" class="clearfix">

					<img src="img/sample/myphoto2.jpg" alt="" title="">

					<div>
						<div>
							<h2>A few words about me</h2>
						</div>
						<div class="about-start">
							<p class="about-text">I have knowledge of Python, SQL, Django and strong willingness to work
								in the field of python development and eager to get real working experience.</p>

							<p class="about-text">Briefly about myself: attentive, reliable, responsible, punctual,
								multitasking, quite good at time management and goal-oriented.
								Completed course "Python programming basics" and training at Stepik platform.</p>
							<p class="about-text">Have acquired the following skills:</p>

							<p>
							<ul id="check_about">
								<li> Python: syntaxis, loops, OOP, function | </li>
								<li> GitHub | </li>
								<li> Json/CSV | </li>
								<li> Sqlite, MySQL, NoSQL (MongoDB) | </li>
								<li> RegEx | </li>
								<li> Linters, Unitest, Pytest, Black | </li>
								<li> YAGNI, KISS, DRY, SOLID</li>
							</ul>
							</p>

							<p class="about-text">Got acquainted with and had some practice in:</p>
							<p>
							<ul id="check_about">
								<li> Selenium, Aiohhtp, Asyncio, Beautifulsoup | </li>
								<li> Django, Django DRF, NuxtJS, CSS, HTML | </li>
								<li> Jira | </li>
								<li> Linux (Mint)</li>
							</ul>
							</p>
							<p class="about-text">Made some commercial and pet parsing projects.
								You can see some of them <nuxt-link to="/projects">here.</nuxt-link></p>

							<p class="about-text">At previous work had a great experience in team management of
								designers, adjusters,
								programmers and
								installers. </p>
						</div>
					</div>
					<blockquote class="about-me">
						<div class="quote-top"></div>
						<p>&#8220;In the end, it’s not the years in your life that count. It’s the life in your
							years.&#8220;</p>
						<p class="quote-author">Abraham Lincoln, 16th president of the United States</p>
					</blockquote>

				</div><!-- about end -->

				<div id="about-middle" class="clearfix">

					<div id="content-left">

						<div class="clearfix">
							<h2>My hobbies</h2>
						</div>
						<blockquote class="about-me">
							<div class="quote-top"></div>
							<p style="margin-left: 30px;">Woodworking</p>

							<p>I'm fond of making wood products. I like to
								make something unique, from natural materials, where precision and creativity are
								needed.</p>

						</blockquote>
						<blockquote class="about-me">
							<div class="quote-top"></div>
							<p style="margin-left: 30px;">Travelling</p>

							<p>I especially love nature, hiking, ocean trips, where you can breathe
								freely and enjoy beautiful views.</p>
						</blockquote>

					</div><!-- content-left end -->

					<div id="content-right">

						<div class="clearfix">
							<h2>My goals</h2>
						</div>

						<ul id="check">

							<li>Build a house</li>
							<li>Raise a son</li>
							<li>Plant a tree</li>

						</ul>

					</div><!-- content-right end -->

				</div><!-- about-middle end -->

				<br>
				<br>

			</div><!-- content-innertube end -->

		</div><!-- page end -->

	</div><!-- page-shadow end -->

</template>