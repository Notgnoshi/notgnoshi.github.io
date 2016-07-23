---
title: Partial Integration
layout: post
meta: A development of partial integration applying intuition from single variable calculus to two and three variable calculus
---

### Purpose:

Finding a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$ was one of the ideas introduced in Calculus III that was not explained as clearly to me as I would have liked. First off, it wasn't called "partial integration", which I think would have helped clue me in to what it was all about. The instructor went through an example problem and numbered a bunch of equations, then gave us an instruction list of what to do based on those numbered equations. We'd integrate $$1$$ with respect to $$x$$, and call the result $$2$$, then differentiate $$2$$ with respect to $$y$$, and call this $$3$$, then compare $$3$$ with $$4$$. While she was telling us how to do this, when asked, the only explanation we got was something along the lines of "Well, that's just what you do." It turns out that while yes, that is how you do it, there's a reason *why*, and understanding that reason I believe helps me to understand *how* to solve the problem.

Somewhere along the way it clicked what she was doing, and now I don't have to memorize what equations to number in what order, and what kind of operations or comparisons to apply to whichever equation. Now, with an understanding of what she was trying to teach us, I believe that I understand the concept now, and that I can in fact find a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$ provided such a function exists.

Maybe part of the problem was that I took Calculus III before Differential Equations, but in my current differential equations course we skipped the part on partial integration.

However, the day before our final exam, some students and I got together to study. We stayed in one our school's study rooms around a conference table for over 8 hours (7:30am - 4:30pm) and pounded out problems. One of the students present had trouble with this problem, and while she was able to blindly follow the instruction list our instructor gave us, she expressed frustration with not understanding the process. Naturally being the knight in shining armor that I am, I jumped to the rescue and attempted to explain the deep insight I had on the matter. While she claimed my attempts helped, in hindsight I believe I only muddied the water. My purpose here will be to explain the matter to the best of my ability as clearly as I can. I will do it twice, once in two variables, and once in three.

### Two Variables:

**Problem:** *Given a vector function $$\boldsymbol{F}(x, y) = (3+2xy)\boldsymbol{\hat \imath} \, + \, (x^2 - 3y^2) \boldsymbol{\hat \jmath} $$, find a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$.*

If $$\boldsymbol{F}$$ wasn't a vector function, and $$\nabla f$$ was the same as saying $$\frac{d}{dx} f$$ we'd have no problem finding such a function $$f$$. I want to draw attention to the similarities between $$\nabla f$$ and $$\frac{d}{dx} f$$, and the vector function $$\boldsymbol{F}$$ and a scalar function $$F$$. Using these similarities, I hope to explain the problem at hand.

Just to refresh our memories, let's first take a simpler problem, say given some function $$F(x) = 3x^2$$, find a function $$f(x)$$ such that $$\frac{d}{dx} f(x) = F(x)$$. So let's think. The problem is asking not for the derivative of the function $$F$$, but the function for which $$F$$ is the derivative of. Are you thinking antiderivative yet? Making this mental connection, while seemingly trivial, is essential for understanding the issue at hand. We know that integrating a function is how we go backwards from a derivative of a function to the function itself, so let's take the indefinite integral of $$F$$.

The indefinite integral of $$3x^2$$ with respect to $$x$$ is simply $$x^3$$ plus some constant $$C$$. The constant of integration is quite important to remember here. Therefore we get $$f(x) = x^3 + C$$.

Now let's work backwards on our problem from a function $$f(x, y)$$ to find $$\nabla f$$, a vector containing the partial derivatives of our function $$f$$. Let's take a function $$f(x, y) = 3x + x^2 y - y^3 + 57$$ and find $$\nabla f$$ (which is equal to $$\boldsymbol{F}$$). This is simple enough; these partial derivatives aren't too bad to find.

$$f_x = 3 + 2xy$$

$$f_y = x^2 + 3y^2$$

Therefore, we have a function $$\boldsymbol{F}(x, y) = (3+2xy)\boldsymbol{\hat \imath} \, + \, (x^2 - 3y^2) \boldsymbol{\hat \jmath} $$.

How do we go *backwards* from a function $$\boldsymbol{F}(x, y)$$ to $$f(x, y)$$ though? To go from $$f$$ to $$F$$ we took partial derivatives, so does that mean we do "partial" integration to go backwards? Yes, let's try it out!

Given a function $$\boldsymbol{F}(x, y) = (3+2xy)\boldsymbol{\hat \imath} \, + \, (x^2 - 3y^2) \boldsymbol{\hat \jmath} $$, let's finally work on finding a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$. We know $$f_x$$  to be $$3 + 2xy$$, and $$f_y$$ to be $$x^2 - 3y^2$$, so let's start there. Integrating $$f_x$$ with respect to $$x$$ gives us $$\int 3 + 2xy \, \mathrm{d}x = 3x + x^2 y$$. This is part of our function $$f$$, but not all of it. Remember there could still be a constant $$C$$ if we were doing single variable calculus, or in this case, some function of $$y$$ tacked onto the end of $$f$$. So we can now say more formally that $$f(x, y) = 3x + x^2y + g(y)$$.

Remember that $$f_y$$ was $$x^2 - 3y^2$$. Now, if we took the partial derivative with respect to $$y$$ of the function $$f(x, y) = 3x + x^2y + g(y)$$ above, we would get precisely the second component of $$F$$, which is $$x^2 - 3y^2$$. However, we don't know what $$g(y)$$ is, so we'll represent $$f_y$$ of $$f(x, y) = 3x + x^2y + g(y)$$ simply as $$x^2 + g_y(y)$$.

Now, we *know* that $$f_y$$ is $$x^2 - 3y^2$$! We can use this to figure out what $$g(y)$$ is. If we set the known value of $$f_y$$ equal to the calculated value we get $$x^2 + 3y^2 = x^2 + g_y(y)$$. Using this, we can find $$g'(y)$$ to be $$-3y^2$$, so the value of $$g(y)$$ is therefore $$-y^3$$ plus some constant $$C$$. We can plug $$g(y) = -y^3 + C$$ into what we found earlier for $$f(x, y)$$. Finally we get $$f(x, y) = 3x + x^2 y - y^3 + C$$.

This is the final answer to our problem! If we were given a three variable function $$\boldsymbol{F}$$, could we still find the answer? Yes, and by using the same process! Let's see how this works with a little less commentary. Hopefully it will be a little easier to understand.

### Three Variables:

**Problem:** *Given a function $$\boldsymbol{F}(x, y, z) = (y^2) \boldsymbol{\hat \imath} + (2xy + e^{3z}) \boldsymbol{\hat \jmath} + (3ye^{3z}) \boldsymbol{\hat k}$$, find a function $$f$$ such that $$\nabla f = \boldsymbol{F}$$.*

If such a function $$f$$ exists, then:

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

We can confirm that $$\nabla f = \boldsymbol{F}$$ by simply finding the partial derivatives of the calculated function $$f(x, y, z)$$!

That's a simple refresher on partial integration. I hoped it helped!
