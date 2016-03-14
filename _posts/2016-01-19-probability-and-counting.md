---
layout: post
title: 01 Probability and Counting
categories: [notes, stats]
---

Apparently, Prob & Stats I is 80% probability, with a little bit of statistics spread throughout. Rather than start us out with "boring" introductory statistics, the professor started with chapter 2, probability.

The **sample space** of an experiment is the set of all possible outcomes of that experiment.

An **event** is any collection (subset) of outcomes contained in the sample space. An event is **simple** of it consists of exactly one outcome, and **compound** otherwise.

Given an experiment, the objective of probability is to assign to each event $$A$$ a number $$P(A)$$ called the probability of that event $$A$$, which will give a precise measure of the chance that $$A$$ will occur.

For any event $$A$$, $$P(A) + P(A') = 1$$, where $$A'$$ is the event "not $$A$$". Therefore, for any event $$A$$, $$P(A) \leq 1$$.

The simplest method of computing probability lies in the **equally likely outcome** case, where each outcome is equally likely. When a phrase such as "chosen at random" is used, it means that all outcomes are equally likely. In this case, for any event

$$P(\text{event}) = \frac{\text{number desired outcomes}}{\text{number possible outcomes}}$$

Another way of writing the same thing is

$$P(A) = \frac{N(A)}{N}$$

This is a simple enough rule, but unfortunately, it's the figuring out how many possible outcomes and how many desired outcomes there really are. Counting is hard.

If the first element or object of an ordered pair can be selected $$n_1$$ ways, and for each of these $$n_1$$ ways the second element of the pair can be selected $$n_2$$ ways, then the total number of possible pairs is $$n_1 n_2$$.

More generally, suppose a set consists of ordered collections of $$k$$ elements ($$k$$-tuples) and that there are $$n_1$$ possible choices for the first element; for each choice of the first element, there are $$n_2$$ possible choices for the second element; ...; for each possible choice of the first $$k-1$$ elements, there are $$n_k$$ choices for the $$k$$th element. Then there are $$n_1 \cdot n_2 \dots n_k$$ possible $$k$$-tuples.

This is the **multiplication rule for counting**

If the number of possible choices for each element decreases by one for each element, then the total number of $$k$$-tuples is $$n \cdot (n-1) \cdot (n-2) \cdot \, \dots \, \cdot 2 \cdot 1 = n!$$

If we want to choose $$k$$ items from $$n$$ *distinct* items at random, how many ways can you do this under these two conditions:

* No item repetition
* Don't count different arrangements of $$k$$ items as unique

This is referred to as **$$n$$ choose $$k$$** and is calculated by

$${n \choose k} = \frac{n(n-1)(n-2) \dots (n-k+1)}{k!}$$

For $$k = n$$ this gives 1 combination. For $$k > n$$ this gives 0 combinations. The above need only be calculated for $$k < n$$.

An alternate method of representing **$$n$$ choose $$k$$** is by the following manipulation

$${n \choose k} = \frac{n(n-1)(n-2) \dots (n-k+1)}{k!} \cdot \frac{(n-k)(n - k - 1) \dots (2)(1)}{(n-k)(n - k - 1) \dots (2)(1)} = \frac{n!}{k!(n - k)!}$$

This second method can be more computationally intensive to do by hand though, but is an easier to remember formula.

On the TI-*n*spire calculator (non-CAS), $$n$$ choose $$k$$ can be calculated by `menu > Probability > Combinations` and can be entered manually by `nCr(n, y)`. In R, $$n$$ choose $$k$$ can be calculated by the built-in function `choose(n, k)`.
