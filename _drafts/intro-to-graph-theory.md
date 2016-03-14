---
layout: post
title: A Brief Introduction to Graph Theory
---

I started writing a post the other day about a topic in graph theory, but I found myself giving definitions for basic concepts along the way. While they were important to the topic at hand, I believe that taking every other paragraph to explain something related is distracting, and ultimately detracts from the quality of the post.

What I'd like to do here is introduce [graph theory](https://en.wikipedia.org/wiki/Graph_theoryhttps://en.wikipedia.org/wiki/Graph_theory) and some related topics as if this is the first you've ever heard of graph theory.

### Introduction:

In a word, graph theory is the study of graphs. But these graphs are unlike what you're most likely familiar with. Graph theory graphs are a method of modeling some system that is composed of parts that share some kind of relationship(s) with each other.

Graphs are made out of two things, **nodes** (sometimes called vertices):

IMAGE

and **edges**:

IMAGE

The nodes represent an object of some kind, most likely a component in a larger system.

IMAGE

The edges represent the relationships between the nodes. These relationships can be physical or nonphysical, as can the nodes, but each edge should represent the same relationship between each of the nodes.

IMAGE

MATHEMATICALLY RIGOROUS DEFINITION OF A GRAPH HERE

Because the drawings represent something that does not exist on paper (it exists either out in the world somewhere or in our imagination) the manner in which we draw the graph does not matter. The following graph is not a graph at all, it is a drawing of a graph, or a **graph diagram**.

IMAGE

This introduces the idea of **graph isomorphism**, or the idea that two graphs diagrams can represent the same graph, even if they look different. Two such graphs are said to be *isomorphic*. Graph theorists are not concerned with the shapes of graphs, or the angles between the edges, they are *only* concerned with the relationships between the nodes. For example, the following two graphs are isomorphic.

IMAGE

Graph theorists also concern themselves with the **degree** of nodes, or the number of edges connected to a particular node. In fact, this was how Euler solved what is sometimes called the very first graph theory [problem](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg), by considering the degree of nodes, and whether they were even or odd.

### Some Important Definitions:
TODO: create includes for definitions and create custom CSS styles for them.
* own stylesheet
* markdown or html?
* use include or a <div> with CSS class?

PLANAR GRAPH

FACES

POLYGONAL GRAPH

PLATONIC GRAPH

LINE GRAPH

DUAL GRAPH / FACE GRAPH
