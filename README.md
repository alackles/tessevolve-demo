# Tessevolve

## What's the TL;DR?
				<p>
					This is a visualization of evolutionary fitness landscapes. 
					You can view them in 2D, 3D, and 4D (but you'll have to scroll through in 4D).
					The goal is for you to be able to understand and interpret 3D and 4D landscapes, which are difficult to show in flat images. 
					I hope it helps!
				</p>
				<h4> I don't see anything. </h4>
				<p>
					Did you click the <span class="oi oi-cog align-self-middle"></span> <b>Settings</b> button and select some data, then click <span class="oi oi-brush"></span> <b>Draw</b>?
				</p>
				<h4> Yeah, I did all that, but I still don't see anything. </h4>
				<p>
					It takes a second to render, because A-Frame has to delete everything you see and put new stuff in its place.
					Also, you might need to back up (WASD or arrow keys) or turn around; the landscapes don't always appear in front of you.
					If you still see nothing, it's possible I accidentally broke something 😦. Please contact me at the link in the header if you keep having problems.
				</p>
          		<h4> The 4D representation looks just like the 3D representation. Where's the 4th dimension?</h4>
          			<p>
          				Unfortunately, there's not a great way to represent 4D data to our 3D brains. 
						So what you're seeing is actually 3D <i>slices</i> of the complete 4D object.
						If you use your mouse wheel to <b>scroll</b>, the colors will change; this represents the fitness values for that 3D slice.
						Scrolling through multiple slices should give you some intuition about how the 4th dimension interacts with the other 3.
   	 	      		</p>

				<h4> What about the 4D lineages? Those aren't moving; are they the same in each slice?</h4>
					<p>
						No, they aren't! The lines between nodes don't move, but the nodes themselves will change color as you scroll.
						If they are saturated with color, those nodes are on that slice.
						If they are greyed out and translucent, those nodes are on a different slice. 
						Lines between nodes are displayed on all slices for simplicity and better rendering speed. 
					</p>

				<h4> What about 5D? 6D? How high can you go?</h4>
					<p>
						That's a great question! 
						As far as I know, this is the first visualization using VR of either 3D <i>or</i> 4D fitness landscapes, so it certainly isn't perfect. 
						But we would love to push the envelope even further. 
						One thing we want to do next is add <b>audio input</b> with the VR headset's built-in directional sound capabilities.
						This might add another dimension, or might be a substitute for color for colorblind, low vision, or blind users of the software.
						If you are interested in working with me on that extension, PLEASE contact me, particularly if you fit one of the descriptors above. 
					</p>

				<h4> Where are these landscapes from? </h4>

					<p>
						The <a href="https://www.epitropakis.co.uk/gecco2021/">2021 GECCO niching competition</a>, with modifications by me to integrate the C++ versions of the landscapes into our digital evolution software and extend the landscapes you see here into 4D.
					</p>

          		<h4> What tools did you use to build this? </h4>
					<p>
						For full details, see <a href="https://github.com/alackles/project-viz-3D">the GitHub repo for this site</a>. In summary:<br><br>
						&ensp; <span class="oi oi-caret-right"></span> <a href="https://github.com/mercere99/MABE2"> MABE2 (pre-alpha)</a>: a heavily in-development digital evolution framework to evolve the phylogenies. <br><br>
						&ensp; <span class="oi oi-caret-right"></span> <a href="https://aframe.io/">A-Frame (v1.2.0)</a>: an open source and shockingly straightforward web framework for virtual reality. <br><br>
						&ensp; <span class="oi oi-caret-right"></span> <a href="https://d3js.org/">D3.js (v7)</a>: an open source, easy-to-use JavaScript library for data-driven HTML, which was absolutely invaluable for programatically creating the landscapes you see. <br><br>
						&ensp; <span class="oi oi-caret-right"></span> <a href="https://getbootstrap.com">Bootstrap (v5)</a>: an open source web framework to connect the front-end to the back-end, which I used to make this website. <br><br>
						&ensp; <span class="oi oi-caret-right"></span> <a href="https://useiconic.com/open/">Open Iconic (v1.1.0)</a>: open source icons which I used for the buttons on this site. <br><br>
						And my laptop running <a href="https://endeavouros.com/">EndeavourOS</a>. 
					</p>

				<h4>Who else helped make this happen?</h4>
					<p>
						This work builds directly on Emily Dolson's previous work on <a href="https://dl.acm.org/doi/pdf/10.1145/3205651.3208301">visualizing 2D landscapes in 3D</a>; the template for this website comes from <a href="https://emilydolson.github.io/fitness_landscape_visualizations/">her demo site</a> for that paper.
            			I'm additionally thankful to Charles Ofria, Clifford Bohm, and Vincent Ragusa for helpful discussions on this project.
					</p>

				<h4>Who are you?</h4>
					<p>
						I'm a PhD student creating methods and metrics to understand evolution at different scales. 
      	    			To learn more about me, see <a href="http://github.alackles.io"> my website</a>.
					</p>
