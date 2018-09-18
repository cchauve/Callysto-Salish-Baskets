# Interactive notebooks for creating Coast Salish basket motifs
#### Authors: Howell Tan, Jenifer Pham, Laura Gutierrez Funderburk, Cedric Chauve, Veselin Jungic
#### Contact: [Dr. Cedric Chauve](https://cchauve.github.io) and [Dr. Veselin Jungic](http://people.math.sfu.ca/~vjungic/)


Weaving is a craft with a long history in many places around the world, including the Pacific NorthWest. Woven baskets in particular have long been important practical and cultural objects for BC Coast Salish people. An important feature of woven baskets is the occurrence of beautiful geometric motifs/patterns, such as the ones of the basket below, exposed at the [UBC Museum of Anthropology](https://moa.ubc.ca/).

![](https://moa.ubc.ca/wp-content/uploads/2018/03/Basket-by-Theresa-Gabriel-Lil%E2%80%99wat.-Photo-by-Derek-Tan.jpg "Lil’wat basket by Teresa Bagriel")

The project we describe here originates from a starting collaboration betwen the [Department of Mathematics](http:/math.sfu.ca) at [Simon Fraser University (SFU)](http://www.sfu.ca) and baskets weavers from the [Tla'amin Nation](http://www.tlaaminnation.com). It consists in the development of a series of interactive [Jupyter notebooks](http://jupyter.org/) allowing to generate motifs similar to the ones  observed on existing woven baskets, but also to create novel motifs. 

The guiding idea of our work is that the motifs we can observe on many Coast salish baskets are highly regular and can be described very simply in terms of basic geometric shapes (broken lines, triangles, rectangles, ...) and operations such as reflections and stacking. Following this observation, we designed three Jupyter notebooks, inspired by baskets we were presented during a visit to the Tla'amin Nation.
- The first notebook (**Atomic Motifs**) implements this principle and allows the user to design complex motifs by a sequence of geometric operations applied successively, starting from a simple initial shape; the resulting motifs can be saved in a file that will be used by the other notebooks. 
- The second notebook (**Combining and Editing Motifs**A) takes motifs saved in files and allows a user to edit them and to combine them into more complex motifs; it also includes the possibility to define a motif from scratch, for example to be uased as initial shape by the first notebook.
- Finally the third notebook (**3D Basket**A) allows a user to combine various motifs created by the first two notebooks into a circular or rectangular basket, that can be visualized in 3 dimensions.

To access these notebooks, please visit our github repo, either by following this [link](https://github.com/cchauve/Callysto-Salish-Baskets) or by clicking on "View on Github" on top of this page.

Our notebooks are primarily intended to be used by students during classrooms activities, with the goal to illustrate how simple geometric concepts and operations can be used to design realistic patterns; we hope is that our notebooks can also be useful to artist weavers, by allowing them to visualize different pattern ideas.

These notebooks  form only a first draft of a more general tool we expect to develop over the next few months. The main feature of our approach is to see basket motifs under the prism of geometric shapes and symmetries. This results in the possibility to design complex motifs from simple ones to which simple mathematical operators are applied. Our longer term goal is to tend toward more realistic motifs.