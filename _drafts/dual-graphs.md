---
layout: post
title: Polytopes and Dual Graphs
---

I was reading a [book](http://www.amazon.com/gp/product/0486678709?psc=1&redirect=true&ref_=oh_aui_detailpage_o01_s00) on graph theory a while ago, and in it there was a small portion of a chapter about the five [Platonic graphs](https://en.wikipedia.org/wiki/Platonic_graph). I asked myself a question, and I'm glad I did. Although it turns out that my question had a very simple answer, it introduced a topic to me that I find completely fascinating.

What is a Platonic graph? A Platonic graph is a graph in three dimensions that has the same vertices as one of the five Platonic solids. A Platonic solid has congruent polygonal faces with equal number of faces meeting at each vertex. Essentially, it's the 3D version of a regular polygon. The mathematical term for these 3D objects is polyhedron. I think it's safe to say that we're all familiar with polyhedrons, and for sure we're familiar with polygons. A [polytope](https://en.wikipedia.org/wiki/Polytope) is an $$n$$-dimensional version of polygons and polyhedra. All polygons and polyhedra are polytopes, but not all polytopes are either polygons or polyhedra.

Here are the five [Platonic solids](https://en.wikipedia.org/wiki/Platonic_solid):

* Tetrahedron (four faces)
* Cube (six faces)
* Octahedron (eight faces)
* Dodecahedron (twelve faces)
* Icosahedron (twenty faces)

So the Platonic graphs are the graph version of these solids (a node for every vertex, and an edge for every... well... edge). My question was if the relationships between the vertices was the same relationship as between the faces. In other words, why do the Platonic graphs use the vertices of the solids for the graph nodes instead of say, their faces?

So I fiddled around, and drew a few (bad) pictures. I started with a cube. Instead of drawing a graph of the cube with the cubes vertices as its nodes, I used the cube's faces. I used shared edges between two faces as the graph edges. The first problem that I saw was that cubes have six faces, and eight vertices. So obviously, the two versions of my "cube" cannot be equivalent.

TODO: IMAGE HERE

This second "cube" is actually an octahedron, and is called the *"dual"* of the cube graph. I then proceeded to ask myself what the dual of an octahedron was (not in those words, I wasn't aware of the terminology at the time). It turns out it's a cube!

TODO: IMAGE HERE

Another way to draw this, and this probably explains this whole phenomena better than I could with words, is to draw the octahedron *inside* the cube as the Wikipedia [article](https://en.wikipedia.org/wiki/Dual_polyhedron) does:

<div style="margin:auto; width:33%">
    <p style="width:80%; text-align:center; font-size:0.8em">
        <a href="https://commons.wikimedia.org/wiki/File:Dual_Cube-Octahedron.svg#/media/File:Dual_Cube-Octahedron.svg">
            <img style="width:100%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dual_Cube-Octahedron.svg/1200px-Dual_Cube-Octahedron.svg.png" alt="Dual Cube-Octahedron.svg">
        </a>
        <br>
        "<a href="https://commons.wikimedia.org/wiki/File:Dual_Cube-Octahedron.svg#/media/File:Dual_Cube-Octahedron.svg">Dual Cube-Octahedron</a>" by 4C - <span class="int-own-work" lang="en">Own work</span>. Licensed under <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a> via <a href="https://commons.wikimedia.org/wiki/">Commons</a>.
    </p>
</div>

The next logical question is, do the other Platonic graphs have similar relationships? My next <strike>victim</strike> graph of choice was the tetrahedon, the simplest of the Platonic graphs. Applying the same manipulations as I did with the cube, an interesting fact arose. The tetrahedron is dual to *itself*! Furthermore, the tetrahedon is one of only three types of self-dual polytopes. The first type is any polygon. The second is called a [simplex](https://en.wikipedia.org/wiki/Simplex) and is kind of a triangle in $$n$$-dimensions, this is the class the tetrahedron belongs to. The third self-dual polytope is a [24-cell](https://en.wikipedia.org/wiki/24-cell).

The dodecahedron and icosahedron are dual as well, though I think I'll spare you the drawings.

A more precise definition of graph duality would be:

TODO: FIND THIS DEFINITION:

>The dual graph of a plane graph $$G$$, is a graph that has a vertex corresponding to each face of $$G$$, and an edge joining two neighboring faces for each edge in $$G$$. We call these graphs "dual" because this is a symmetric relationship; if $$H = \text{dual}(G)$$, then $$G = \text{dual}(H)$$.
>The dual of $$G$$ is nonunique though, if $$H,J = \text{dual}(G)$$ it does not necessarily imply that $$H$$ and $$J$$ are congruent, or isomorphic.

A plane (planar) graph is one who can be drawn on a 2D plane (or a sphere interestingly enough) without edge crossings. This definition assumes that the graph $$G$$ is *planar*. This makes sense because the only way you can have *faces* of a graph, is if it's either planar or polyhedral. Are polyhedral graphs planar though? Yes, though I cannot *prove* it to you in mathematical language.

If we hold a thought experiment though, you might see what I mean. Let's think about a cube. In our mind, we're holding up a cube graph, and holding it by two parallel edges. Because this is all in our heads, we can stretch and shrink our cube. What we're going to do, is pull our cube against our chest, and stretch the outermost face apart, while at the same time pulling it towards us until out cube is completely flat.

We can do this same kind of thing for say, a [Bucky Ball](https://en.wikipedia.org/wiki/Buckminsterfullerene), or some other more complicated polyhedral graph. This is in no way a proof, but I hope it helps you see the intuition behind the matter.

For example, here are the planar drawings of the five Platonic graphs:

<div style="margin:auto; width:60%">
    <img src="http://mathworld.wolfram.com/images/eps-gif/PlatonicGraphs_800.gif" alt="Planar Platonic graphs">
</div>

All of the duals of the Platonic graphs are themselves Platonic graphs, and are therefore all planar. But what about other planar graphs? Are the dual graphs of all planar graphs planar?

A related topic to dual graphs is the concept of a [line graph](https://en.wikipedia.org/wiki/Line_graph). That is, a graph that represents the adjacencies between the edges a a graph.

TODO: DECIDE IF TALK ABOUT FACE GRAPH
