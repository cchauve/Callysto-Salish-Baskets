# Interactive notebooks for creating Coast Salish basket motifs
#### Authors: Howell Tan, Jenifer Pham, Laura Gutierrez Funderburk, Cedric Chauve, Veselin Jungic
#### Contact: [Dr. Cedric Chauve](https://cchauve.github.io) and [Dr. Veselin Jungic](http://people.math.sfu.ca/~vjungic/)


### Overview

Weaving is a craft with a long history in many places around the world, including the Pacific Northwest. Woven baskets, in particular, have long been important practical and cultural objects for BC Coast Salish people. An important feature of woven baskets is the occurrence of beautiful geometric motifs/patterns, such as the ones on the basket below, exhibited at the [UBC Museum of Anthropology](https://moa.ubc.ca/). 

![](https://moa.ubc.ca/wp-content/uploads/2018/03/Basket-by-Theresa-Gabriel-Lil%E2%80%99wat.-Photo-by-Derek-Tan.jpg "Lil’wat basket by Teresa Bagriel")

The project we describe here originates from a starting collaboration between the [Department of Mathematics](http:/math.sfu.ca) at [Simon Fraser University (SFU)](http://www.sfu.ca) and baskets weavers from the [Tla'amin Nation](http://www.tlaaminnation.com). We developed a series of interactive, online [Jupyter notebooks](http://jupyter.org/) (a simple, powerful computer application) that can generate motifs similar to those observed on existing woven baskets, and can also create novel motifs. This project was funded by the Pacific Institute for [Pacific Institute for Mathematical Sciences](https://www.pims.math.ca/) and is part of the [Callysto](https://callysto.ca/) project, which aims to bring technology into Canadian classrooms.

The guiding idea of our work is that the motifs we observe on many Coast Salish baskets are highly regular and can be described very simply in terms of basic geometric shapes (broken lines, triangles, rectangles, …) and mathematical operations such as reflections and stacking. Following this observation, we designed two Jupyter notebooks inspired by baskets the Tla’amin Nation presented to us during a visit. .

* The first notebook (Atomic Motifs) implements the geometric principles of reflection and stacking as described above. It allows the user to design complex motifs by successively applying a sequence of geometric operations, starting from a simple initial shape. Tthe resulting motifs can be saved in a file that can be used by other notebooks.

* The second notebook (Combining and Editing Motifs to create 3D Basket Models) takes saved motifs and allows the user to edit them and to combine them into more complex motifs. It also includes the possibility of defining a motif from scratch, for example to be used as an initial shape by the first notebook. Then the user can combine various motifs into a circular or rectangular basket that can be displayed in three dimensions.

Our notebooks are primarily intended to be used by students during classrooms activities, with the goal of illustrating how to use simple geometric concepts and operations to design realistic patterns. We also hope our notebooks can also be useful to artist weavers, who could use them to visualize new pattern ideas. These notebooks form only a first draft of a more general tool we expect to develop over the next few months. The main feature of our approach is to visualize basket motifs under the prism of geometric shapes and symmetries. This results in the possibility of designing complex motifs from simple ones,to which simple mathematical operators are applied. Our longer-term goal is to create more realistic motifs.

### Usage 

To access these notebooks, please visit our github repo, either by following this [link](https://github.com/cchauve/Callysto-Salish-Baskets) or by clicking on “View on Github” on top of this page. They can be run without installinganything, from the [Callysto hub](https://hub.callysto.ca/), on which you can connect with an institutional, Google or Microsoft account. To start a notebook, click on the notebook, which will then open in a new browser window, and choose the “Restart & Run All” command in the top menu “Kernel”.

