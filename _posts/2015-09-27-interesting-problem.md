---
layout: post
title: An Interesting Intermediate Value Theorem Problem
meta: A description of an interesting calculus problem involving the application of the Intermediate Value Theorem
---

I recently joined the math club on campus, and so far there's only been a handful of people attending (at one meeting there were three in total). The meetings have pretty much been focused on generating more interest in the math club, but we've also tried our hand at a few different interesting "Problems of the Week".

In one meeting, our faculty advisor made mention of a problem posted on his office blackboard for the last several years. We expressed interest in trying our hand at it, so he copied it down for us, and we spent the next 30ish minutes attempting to make sense of it. It was an interesting problem, and a difficult one. It did not take an extensive math background to solve, only a single intuitive theorem from Calculus I.

Here's the problem:

$$ f : \mathbb{R} \to \mathbb{R} \text{ is continuous.}$$

$$ f(x)f(f(x)) = 1 $$

$$ f(1000) = 999 \text{, find } f(500) \text{.} $$

The hardest part is knowing where to start. I'll readily confess to being quite unsure where to begin until our advisor told us it probably wouldn't be possible to find $$f(x)$$. Knowing that, there is only so much algebraic manipulation one can apply, so it was sort of simple to go from there.

I'm going to walk through the solution, but first a note on what $$ f : \mathbb{R} \to \mathbb{R} $$ means. If we say $$ f : A \to B $$, we say that $$f$$ is a function from $$A$$ to $$B$$. We call $$A$$ the *domain* and $$B$$ the *codomain* of $$f$$. This symbolism means that for all $$ x \in A$$, there is an $$f(x) \in B$$. In simple terms, $$ f : \mathbb{R} \to \mathbb{R} $$ means that for every real input to $$f$$ there is a real output.

Now for the solution. Let's call $$f(x)f(f(x)) = 1$$ some new function $$g(a)=a f(a)=1$$. Now let's try to find what $$g(f(1000))$$ is. We know that $$f(1000)$$ is $$999$$, so let's play around with $$999f(999)=1$$. It's a simple algebraic manipulation to see that $$f(999) = \frac{1}{999} $$. Now let's think; where does that get us.

I wonder if we could do the same for $$f(500)$$. Since we don't know what $$f(x)$$ is, let's instead think about how we would go about finding $$f(500)$$ from $$f(x)f(f(x)) = 1$$, using the above manipulation as a clue. What if we assume that there is some value $$b$$ such that $$f(b) = 500$$. Then we could find $$g(f(b))$$, which would then give us $$500f(500) = 1$$. We can then find $$f(500)$$ to be equal to $$\frac{1}{500}$$. Easy enough, right?

Not so fast, we made an assumption, and we really should make sure it's a valid one. So let's think, do we know for sure that there exists some value $$b$$ such that $$f(b) = 500$$? Think about the graph of $$f(x)$$. We know a few different points. We know $$f(1000) = 999$$, and we know $$f(999) = \frac{1}{999}$$. We also know $$f(x)$$ is continuous, which means that these two points, $$(1000, 999)$$, and $$(999, \frac{1}{999})$$ are connected by some curve. We don't need to know how the curve looks, but by the Intermediate Value Theorem, we know for sure that the curve at some point has the $$y$$ value $$500$$ because it's continuous and it has values both greater and lesser than $$500$$, which means the curve connecting those two point must necessarily cross $$500$$ at some point. For this problem, we don't need to know the point, but we do know for a fact that it exists.

Isn't that interesting?
