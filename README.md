# Interactive notebooks for creating Coast Salish basket motifs
#### Authors: Howell Tan, Jenifer Pham, Laura Gutierrez Funderburk, Cedric Chauve, Veselin Jungic
#### Contact: [Dr. Cedric Chauve](https://cchauve.github.io) and [Dr. Veselin Jungic](http://people.math.sfu.ca/~vjungic/)

#### This is joint collaboration with Tla'amin Nation members: Ms. Betty Wilson, Ms. Gail Blaney, and Mr. Tyler Peters.

### Acknowledgements

We thank the Tla'amin Nation and members  Ms. Betty Wilson, Ms. Gail Blaine, and Mr. Tyler Peters for sharing their knowledge and wisdom on the craft of traditional basket weaving. Without their openness this project would have not taken place. We also acknowledge that this work was conducted in  unceded territory of the Musqueam , Skxwú7mesh, Tsleil-Waututh, Kwikwetlem nations. We thank PIMS and Cybera, as well as the Government of Canada for providing financial support and infrastructure. 

### Overview

Weaving is a craft with a long history in many places around the world, including the Pacific Northwest. Woven baskets, in particular, have long been important practical and cultural objects for BC Coast Salish people. An important feature of woven baskets is the occurrence of beautiful geometric motifs/patterns, such as the ones on the basket below, exhibited at the <a href="https://moa.ubc.ca/" target="_blank">Museum of Anthropology</a>.


![](https://moa.ubc.ca/wp-content/uploads/2018/03/Basket-by-Theresa-Gabriel-Lil%E2%80%99wat.-Photo-by-Derek-Tan.jpg "Lil’wat basket by Teresa Bagriel")

The project we describe here originates from a starting collaboration between the <a href="http:/math.sfu.ca" target="_blank">Department of Mathematics</a>  at <a href="http://www.sfu.ca" target="_blank">Simon Fraser University</a>  and baskets weavers from the <a href="http://www.tlaaminnation.com" target="_blank">Tla'amin Nation</a>. We developed a series of interactive, online <a href="http://jupyter.org/" target="_blank">Jupyter notebooks</a> (a simple, powerful computer application) that can generate motifs similar to those observed on existing woven baskets, and can also create novel motifs. This project was funded by the Pacific Institute for <a href="https://www.pims.math.ca/" target="_blank">Pacific Institute for Mathematical Sciences</a> and is part of the <a href="https://callysto.ca/" target="_blank">Callysto</a> project, which aims to bring technology into Canadian classrooms.

The guiding idea of our work is that the motifs we observe on many Coast Salish baskets are highly regular and can be described very simply in terms of basic geometric shapes (broken lines, triangles, rectangles, …) and mathematical operations such as reflections and stacking. Following this observation, we designed two Jupyter notebooks inspired by baskets the Tla’amin Nation presented to us during a visit. .

* The first notebook (Atomic Motifs) implements the geometric principles of reflection and stacking as described above. It allows the user to design complex motifs by successively applying a sequence of geometric operations, starting from a simple initial shape. Tthe resulting motifs can be saved in a file that can be used by other notebooks.

* The second notebook (Combining and Editing Motifs to create 3D Basket Models) takes saved motifs and allows the user to edit them and to combine them into more complex motifs. It also includes the possibility of defining a motif from scratch, for example to be used as an initial shape by the first notebook. Then the user can combine various motifs into a circular or rectangular basket that can be displayed in three dimensions.

Our notebooks are primarily intended to be used by students during classrooms activities, with the goal of illustrating how to use simple geometric concepts and operations to design realistic patterns. We also hope our notebooks can also be useful to artist weavers, who could use them to visualize new pattern ideas. These notebooks form only a first draft of a more general tool we expect to develop over the next few months. The main feature of our approach is to visualize basket motifs under the prism of geometric shapes and symmetries. This results in the possibility of designing complex motifs from simple ones,to which simple mathematical operators are applied. Our longer-term goal is to create more realistic motifs.

### News Articles & Stories

Here are stories and news articles covering our application. 

<a href="https://the-peak.ca/2019/01/sfu-students-utilize-indigenous-basketry-patterns-to-teach-mathematical-concepts/" target="_blank">The Peak: "SFU students utilize Indigenous basketry patterns to teach mathematical concepts"</a> By Henry Tran

<a href="http://www.sfu.ca/sfunews/stories/2018/12/math-students-help-preserve-and-promote-traditional-basketry.html" target="_blank">SFU News: "New app uses Indigenous basketry patterns to teach math concepts"</a>  By Diane Luckow


<a href="https://theconversation.com/mathematics-talent-abounds-in-indigenous-communities-98250" target="_blank">The Conversation "Mathematics talent abounds in Indigenous communities"</a>, an overview of the Math Catcher Program   By Dr. Veselin Jungic

<a href="https://www.youtube.com/watch?v=KgJJAVCxTm8" target="_blank">Project Demo </a>

### Demo Access

To access a demo of these notebooks, please visit the <a href="https://mybinder.org/v2/gh/cchauve/Callysto-Salish-Baskets/master" target="_blank">following link</a>. 

#### ENSURE YOU OPEN AND RUN THE binder_init.ipynb NOTEBOOK PRIOR TO RUNNING ALL NOTEBOOKS. 

Once you launch the demo version via myBinder, you need to initialize the notebook dependencies via the binder_init.ipynb notebook, you can find it under the notebooks/ directory.

Refer to this gif for visual aid. 

![Demo](./notebooks/images/InitNB.gif)


#### Please note this is a shared copy. To get your own copy of the notebooks please follow the instructions on the next section. 

### Usage 

To access these notebooks, please visit our github repo, either by following this <a href="https://github.com/cchauve/Callysto-Salish-Baskets" target="_blank">link</a> or by clicking on “View on Github” on top of this page. They can be run without installing anything, from the [Callysto hub](https://hub.callysto.ca/), on which you can connect with an institutional, Google or Microsoft account. A detailed guide on how to access and run the notebooks is found <a href="https://github.com/cchauve/Callysto-Salish-Baskets/blob/master/documentation/CallystoSalishCallystoNotebookSetup.pdf" target="_blank">here</a> .

