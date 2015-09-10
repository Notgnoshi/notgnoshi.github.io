---
title: Finding a Function f Such that Del f Equals F
layout: post
tags:
  -Multivariable calculus
  -partial derivatives
  -calculus
  -integration
---

### Purpose

Finding a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$ was one of the ideas introduced in Calculus III that was not explained as clearly to me as I would have liked. The instructor went through an example problem and numbered a bunch of equations, then gave us an instruction list of what to do based on those numbered equations. We'd integrate $$1$$ with respect to $$x$$, and call the result $$2$$, then differentiate $$2$$ with respect to $$y$$, and call this $$3$$, then compare $$3$$ with $$4$$. While she was telling us how to do this, when asked, the only explanation we got was something along the lines of "Well, that's just what you do." It turns out that while yes, that is how you do it, there's a reason *why*, and understanding that reason I believe helps me to understand *how* to solve the problem.

Somewhere along the way it clicked what she was doing, and now I don't have to memorize what equations to number in what order, and what kind of operations or comparisons to apply to whichever equation. Now, with an understanding of what she was trying to teach us, I believe that I understand the concept now, and that I can in fact find a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$ provided such a function exists.

However, the day before our final exam, some students and I got together to study. We stayed in one our school's study rooms around a conference table for over 6 hours and pounded out problems. One of the students present had trouble with finding such a function, and while she was able to blindly follow the instruction list our instructor gave us, she expressed frustration with not understanding the process. Naturally I jumped to the rescue and attempted to explain the revelations I had on the matter. While she said my attempts helped, in hindsight I believe I only muddied the water. My purpose here will be to explain the matter to the best of my ability as clearly as I can.

### Two Variables

**The Problem:** Given a vector function $$\boldsymbol{F}(x, y) = (3+2xy)\boldsymbol{\hat \imath} \, + \, (x^2 - 3y^2) \boldsymbol{\hat \jmath} $$, find a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$.

If $$\boldsymbol{F}$$ wasn't a vector function, and $$\nabla f$$ was the same as saying $$\frac{d}{dx} f$$ we'd have no problem finding such a function $$f$$. I want to draw attention to the similarities between $$\nabla f$$ and $$\frac{d}{dx} f$$, and the vector function $$\boldsymbol{F}$$, and a scalar function $$F$$. Using these similarities, I hope to explain the problem at hand.

Just to refresh our memories, let's first take a simpler problem, say given some function $$F(x) = 3x^2$$, find a function $$f(x)$$ such that $$\frac{d}{dx} f(x) = F(x)$$. So let's think. The problem is asking not for the derivative of the function $$F$$, but the function for which $$F$$ is the derivative of. Making this mental connection, while trivial, is essential for understanding the issue at hand. We know that integrating a function is how we go backwards from a derivative of a function to the function itself, so let's take the indefinite integral of $$F$$.

The indefinite integral of $$3x^2$$ with respect to $$x$$ is simply $$x^3$$ plus some constant $$C$$. The constant of integration is important to remember here. Therefore we get $$f(x) = x^3 + C$$.

Now let's work backwards from a function $$f(x, y)$$ to find $$\nabla f$$, or rather, a vector of the partial derivatives of our function $$f$$. So, given a function $$f(x, y) = 3x + x^2 y - y^3 + 57$$, we'll find $$\boldsymbol{F} = \nabla f$$. Well this is simple enough; these partial derivatives aren't too bad to find. $$f_x = 3 + 2xy$$ and $$f_y = x^2 + 3y^2$$. Therefore, we have a function $$\boldsymbol{F}(x, y) = (3+2xy)\boldsymbol{\hat \imath} \, + \, (x^2 - 3y^2) \boldsymbol{\hat \jmath} $$.

How do we go backwards from a function $$\boldsymbol{F}(x, y)$$ to $$f(x, y)$$ though? To go from $$f$$ to $$F$$ we took partial derivatives, so does that mean we do partial integration to go backwards? Well I'm not sure if "partial" integration is precisely the correct term to use, but it helped me to think of it in that way.

Given a function $$\boldsymbol{F}(x, y) = (3+2xy)\boldsymbol{\hat \imath} \, + \, (x^2 - 3y^2) \boldsymbol{\hat \jmath} $$, let's finally work on finding a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$. We know the $$x$$ partial derivative to be $$3 + 2xy$$, and the $$y$$ partial derivative to be $$x^2 - 3y^2$$, so let's start there. Integrating our $$x$$ partial derivative with respect to $$x$$ gives us $$\int 3 + 2xy \, \mathrm{d}x = 3x + x^2 y$$. This is part of our function $$f$$, but not all of it. Remember there could still be a constant $$C$$ if we were doing single variable calculus, or in this case, some function of $$y$$ tacked onto the end of our function $$f$$. So we can now say more formally that $$f(x, y) = 3x + x^2y + g(y)$$.

Remember that our $$y$$ partial derivative was $$x^2 - 3y^2$$. Now, if we took the partial derivative with respect to $$y$$ of the function $$f(x, y)$$ above, we would get precisely the second component of our vector function $$F$$, or $$x^2 - 3y^2$$. However, we don't know what $$g(y)$$ is, so we'll represent the partial derivative of $$f(x, y) = 3x + x^2y + g(y)$$ with respect to $$y$$ as $$x^2 + g_y(y)$$. Now, we *know* that the partial derivative of $$f$$ with respect to $$y$$ to be $$x^2 - 3y^2$$! We can use this to figure out what $$g(y)$$ is. If we set the two equal to each other we get $$x^2 + 3y^2 = x^2 + g_y(y)$$. Using this, we can find the value of $$g'(y)$$ to be $$-3y^2$$, so the value of $$g(y)$$ is therefore $$-y^3$$ plus some constant $$C$$. We can plug $$g(y) = -y^3 + C$$ into what we found earlier for $$f(x, y)$$. We finally get $$f(x, y) = 3x + x^2 y - y^3 + C$$.

This is the final answer to our problem! If we were given a three variable function $$\boldsymbol{F}$$, could we still find the answer? Yes, and by using the same process! Let's see how this works with a little less commentary.

### Three Variables

**Problem:** Given a function $$\boldsymbol{F}(x, y, z) = y^2 \boldsymbol{\hat \imath} + (2xy + e^{3z}) \boldsymbol{\hat \jmath} + 3ye^{3z} \boldsymbol{\hat k}$$, find a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$.

If there is such a function $$f$$, then:

$$ f_x(x, y, z) = y^2 $$

$$ f_y(x, y, z) = 2xy + e^{3z}$$

$$ f_z(x, y, z) = 3ye^{3z}$$

Integrating $$ f_x$$ with respect to $$x$$ we get

$$f(x, y, z) = xy^2 + g(y, z)$$

where $$g(y, z)$$ is constant with respect to $$x$$. We then differentiate $$f(x, y, z) = xy^2 + g(y, z)$$ with respect to $$y$$ to get

$$ f_y = 2xy + g_y(y, z)$$

Comparing this with the known value of $$f_y(x, y, z)$$ above

$$2xy + e^{3z} = 2xy + g_y(y, z)$$

therefore $$g_y(y, z) = e^{3z}$$ plus some function $$h(z)$$

$$g_y(y, z) = e^{3z} + h(z)$$

We can then rewrite $$f(x, y, z)$$ as

$$f(x, y, z) = xy^2 + ye^{3z} + h(z)$$

Finally, we differentiate $$f$$ with respect to $$z$$ to get

$$f_z = 3ye^{3z} + h_z(z)$$

Comparing this to the known value of $$f_z$$ above we can conclude that the value of $$h_z(z)$$ is $$0$$, so therefore, $$h(z)$$ is some constant number $$C$$. We can therefore say

$$f(x, y, z) = xy^2 + ye^{3z} + C$$

We can find $$\nabla f$$ to confirm that in fact $$\nabla f = \boldsymbol{F}$$!

I hoped this helped!
