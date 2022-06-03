# Tessevolve

## What's the TL;DR?

This is a repo hosting the website for Tessevolve (**tesse**ract + e**volve**), a web-enabled visualization of evolutionary fitness landscapes in multiple dimensions. The website is at https://alackles.github.io/tessevolve. 

You can view them in 2D, 3D, and 4D (but you'll have to scroll through in 4D).The goal is for you to be able to understand and interpret 3D and 4D landscapes, which are difficult to show in flat images. I hope it helps!

## Where are these landscapes from? 

The [2021 GECCO niching competition](https://www.epitropakis.co.uk/gecco2021/), with modifications by me to integrate the C++ versions of the landscapes into our digital evolution software and extend the landscapes you see here into 4D.

## What tools did you use to build this?

- [MABE2](https://github.com/mercere99/MABE2) (pre-alpha): a heavily in-development digital evolution framework to evolve the phylogenies
- [A-Frame](https://aframe.io/) (v1.2.0): an open source and shockingly straightforward web framework for virtual reality
- [D3.js](https://d3js.org/) (v7): an open source, easy-to-use JavaScript library for data-driven HTML, which was absolutely invaluable for programatically creating the landscapes you see
- [Bootstrap](https://getbootstrap.com) (v5): an open source web framework to connect the front-end to the back-end, which I used to make the
- [Open Iconic](https://useiconic.com/open/) (v1.1.0): open source icons which I used for the buttons on the site

And my laptop running [EndeavourOS](https://endeavouros.com/).

## Who else helped make this happen?

This work builds directly on Emily Dolson's previous work on [visualizing 2D landscapes in 3D](https://dl.acm.org/doi/pdf/10.1145/3205651.3208301) the template for this website comes from [her demo site](https://emilydolson.github.io/fitness_landscape_visualizations) for that paper. I'm additionally thankful to Charles Ofria, Clifford Bohm, and Vincent Ragusa for helpful discussions on this project.
