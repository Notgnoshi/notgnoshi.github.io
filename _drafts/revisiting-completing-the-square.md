---
layout: post
title: Completing the Square Revisited
---

<link rel="stylesheet" href="{{ "/assets/styles/square.css" | prepend: site.baseurl }}">

A few posts ago, I talked about the intuition behind [completing the square]({% post_url 2015-05-22-completing-the-square %}). In this post I want to (mostly for myself) work through the basic algebraic steps necessary.

Let's start with the example I used in my first post.

$$x^2 + 10x - 39 = 0 $$

First off, let's move the free number, or constant term, over to the right hand side.

$$x^2 + 10x = 39$$

Now we're going to divide the $$x$$ term's coefficient by $$2$$, square it, and add it to both sides.

$$ (\frac{10}{2})^2 = 5^2 = 25 \\$$

$$ x^2 + 10x + 25 = 39 + 25 $$

Pay close attention to the left hand side. If we squint hard enough, we can see that it's easily factorable. Yay.

$$ (x+5)(x+5) = 64 \\$$

$$ (x+5)^2 = 64 $$

This means that we can take the square root of both sides to get our answer. Now of course, we're super sophisticated and we realize that when we take the square root of a number we get two answers, one positive and one negative.

$$ \sqrt{(x+5)^2} = \sqrt{64} \\$$

$$ x+5 = \pm 8 \\$$

$$ x = -5 \pm 8 \\$$

$$ x_1 = 3, \, x_2 = -13 $$

Cool, these are the same answers as the original post! Let's work through a slightly more complicated example.

$$ 4x^2 – 2x – 5 = 0 $$

First off, we're going to move the constant term over to the right hand side.

$$ 4x^2 - 2x = 5 $$

Then we're going to divide both sides by $$4$$ so we have a shiny beautiful unmolested $$x^2$$ term to work with.

$$ x^2 - \frac{2x}{4} = \frac{5}{4} \\$$

$$ x^2 - \frac{x}{2} = \frac{5}{4} $$

Now we can divide the $$x$$ coefficient by two and square it.

$$ (\frac{1}{2} \cdot \frac{1}{2})^2 = (\frac{1}{4})^2 = \frac{1}{16} $$

We then add this number to both sides.

$$ x^2 - \frac{x}{2} + \frac{1}{16} = \frac{5}{4} + \frac{1}{16} \\$$

$$ x^2 - \frac{x}{2} + \frac{1}{16} = \frac{20}{16} + \frac{1}{16} \\$$

$$ x^2 - \frac{x}{2} + \frac{1}{16} = \frac{21}{16} $$

Again, if we squint hard enough we can see that the left hand side "easily" factors into $$ (x - \frac{1}{4})^2 $$. So now our equation is

$$ (x - \frac{1}{4})^2 = \frac{21}{16} $$

I think you can see where I'm going with this. Let's take the square root of both sides and solve for $$x$$.

$$ x - \frac{1}{4} = \sqrt{\frac{21}{16}} = \pm \frac{\sqrt{21}}{4} $$

So we get $$ x = \frac{1}{4} \pm \frac{\sqrt{21}}{4} $$.

I'd like to note a few things here. One is that knowing how to complete the square isn't just for finding quadratic roots. It's especially helpful in Calculus I & II when you have to simplify ridiculously complicated looking functions in order to differentiate or integrate them. This as also comes up in Differential Equations when you have to quickly solve a quadratic equation to get the solutions for a second order homogeneous linear differential equation. It's just another tool in your toolbelt. You don't use it all the time, but man does it suck to need a hammer when all you have is a wrench. Eventually I might write about completing the square in multiple variables (yay), but not right now because my eyes are glossing over, and I'm sure yours are too.
