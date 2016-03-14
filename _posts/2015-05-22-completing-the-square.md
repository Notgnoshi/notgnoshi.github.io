---
layout: post
title: Completing the Square
tags:
  - Algebra
  - Geometry
---
<link rel="stylesheet" href="{{ "/assets/styles/square.css" | prepend: site.baseurl }}">

I've had a lot of math since the idea of completing the square was first introduced to me, and while comparatively a simple matter, I've always found it a difficult concept to grasp and a difficult process to perform.

I was reading [*The Joy of X*](http://www.amazon.com/Joy-Guided-Tour-Math-Infinity/dp/0544105850/) by Steven Strogatz yesterday when I got to his chapter on algebra and the quadratic formula. He explained geometrically how completing the square works, and for the first time, I feel like I understand not just the process, but how and why it works. At least in its base case.

Suppose we have $$x^2 + 10x = 39$$. We want to find $$x$$, but our equation doesn't factor easily, and we can't really move things around to make it easier to work with. We need to do something else.

&ensp;&ensp;Before we get to solving it, let's look at how we might represent $$x^2$$ geometrically. Purely for the hell of it (not really) let's represent $$x^2$$ as a square with dimensions $$x$$ by $$x$$. We'll display the dimensions next to their corresponding sides for clarity.

<div class="unit" id="small-unit">
    <table id="one">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
        </tr>
        <tr>
            <td class="side">$$x$$</td>
            <td class="box">$$x^2$$</td>
        </tr>
    </table>
</div>

&ensp;&ensp;Similarly, let's represent $$10x$$ as a rectangle with dimensions $$10$$ by $$x$$.

<div class="unit">
    <table id="two">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
        </tr>

        <tr>
            <td class="side">$$10$$</td>
            <td class="box">$$10x$$</td>
        </tr>
    </table>
</div>

&ensp;&ensp;Note that this $$10x$$ rectangle is equivalent with two $$5$$ by $$x$$ rectangles. Splitting this rectangle into two pieces is a <strike>frivolously contrived</strike> ingenious move that will allow us to do what's called "completing the square."

<div class="unit">
    <table id="three">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
        </tr>

        <tr>
            <td class="side">$$10$$</td>
            <td class="box">$$10x$$</td>
        </tr>
    </table>

    <table class="opr">
        <tr>
            <td>$$=$$</td>
        </tr>
    </table>

    <table id="four">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
        </tr>

        <tr>
            <td class="side">$$5$$</td>
            <td class="box">$$5x$$</td>
        </tr>
    </table>

    <table class="opr">
        <tr>
            <td>$$+$$</td>
        </tr>
    </table>

    <table id="five">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
        </tr>

        <tr>
            <td class="side">$$5$$</td>
            <td class="box">$$5x$$</td>
        </tr>
    </table>
</div>

&ensp;&ensp;Using this, let's represent $$x^2 + 10x = 39$$ geometrically by attaching the corresponding rectangles to each other. We lay the left hand side out in this manner for the hell of it, totally not knowing that doing so is a key maneuver for what's next.

<div class="unit">
    <table id="six">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
            <td class="top">$$5$$</td>
        </tr>

        <tr>
            <td class="side">$$x$$</td>
            <td class="box">$$x^2$$</td>
            <td class="box" id="top-five-x">$$5x$$</td>
        </tr>

        <tr>
            <td class="side">$$5$$</td>
            <td class="box" id="bottom-five-x">$$5x$$</td>
            <td class="partial"></td>
        </tr>
    </table>

    <table class="opr">
        <tr>
            <td>$$=$$</td>
        </tr>
    </table>

    <table id="seven" class="shift-down">
        <tr>
            <td class="box thirty-nine">$$39$$</td>
        </tr>
    </table>
</div>

&ensp;&ensp;This ugly representation of our equation tantalizingly suggests our next step. Let's **complete the square** by adding the missing part of the square on the left. It feels natural, right? From the dimensions displayed on the outside edge of our rectangles we know the size of the missing square to be $$5$$ by $$5$$, or $$25$$.

<div class="unit">
    <table id="eight">
        <tr>
            <td></td>
            <td class="top">$$x$$</td>
            <td class="top">$$5$$</td>
        </tr>

        <tr>
            <td class="side">$$x$$</td>
            <td class="box">$$x^2$$</td>
            <td class="box">$$5x$$</td>
        </tr>

        <tr>
            <td class="side">$$5$$</td>
            <td class="box">$$5x$$</td>
            <td class="box twenty-five">$$25$$</td>
        </tr>
    </table>

    <table class="opr">
        <tr>
            <td>$$=$$</td>
        </tr>
    </table>

    <table id="nine" class="shift-down">
        <tr>
            <td class="box thirty-nine">$$39$$</td>
        </tr>
    </table>

    <table class="opr">
        <tr>
            <td>$$+$$</td>
        </tr>
    </table>

    <table id="ten" class="shift-down">
        <tr>
            <td class="box twenty-five">$$25$$</td>
        </tr>
    </table>
</div>

&ensp;&ensp;The square we've just created has dimensions of $$(x+5)$$ by $$(x+5)$$, and we know its area to be $$39+25$$, or $$64$$. We can therefore set up the equation $$(x+5)^2 = 64$$ as an algebraic representation of our squares.

<div class="unit">
    <table id="eleven">
        <tr>
            <td></td>
            <td class="top">$$x+5$$</td>
        </tr>

        <tr>
            <td class="side">$$x+5$$</td>
            <td class="box sixty-four"></td>
        </tr>
    </table>

    <table class="opr">
        <tr>
            <td>$$=$$</td>
        </tr>
    </table>

    <table id="twelve" class="shift-down">
        <tr>
            <td class="box sixty-four">$$64$$</td>
        </tr>
    </table>
</div>

&ensp;&ensp;We can use this much easier to solve equation to find $$x$$.

$$(x+5)^2 = 64$$

&ensp;&ensp;Taking the square root of both sides, and being sophisticated students of mathematics we realize that both positive *and* negative $$8$$ will satisfy $$\sqrt{64}$$. This gives us

$$(x+5)=\pm8$$

&ensp;&ensp;Breaking this down into its two component equations, we get

$$x+5=8 \text{ and } x+5=-8$$

&ensp;&ensp;It's a simple matter to solve these. We add $$-5$$ to both sides of both equations to get our answers of $$x=3$$ and $$x=-13$$.

Now of course we could have used our <strike>diabolic enemy</strike> friend, the quadratic formula, which would have spat our solutions right out in our faces. This probably would have been much easier, but that would remove the *fun* of thinking through how we can solve our simple example equation by completing the square, and definitely remove the satisfaction I got when it "clicked."

<br>

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
