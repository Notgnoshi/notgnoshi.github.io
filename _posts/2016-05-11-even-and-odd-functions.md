---
layout: post
title: "Even and Odd Functions: A Reminder"
categories: [post, other]
---

I must confess that while I once knew what the terms "even" and "odd" meant in terms of describing functions, now that mastery of such basic concepts is expected of me, I seem to have forgotten much. So real quickly, I'd like to remind myself what even and odd functions are, and briefly what properties they have.

### Even Functions:

If $$f(x)$$ is a real-valued function, then $$f$$ is even if the following holds for all $$x$$ in the domain of $$f$$

$$f(x) = f(-x)$$

or

$$f(x) - f(-x) = 0$$

What this means geometrically, is that an even function is symmetric with respect to the $$y$$-axis, that is, we get the same graph if we reflect the graph about the $$y$$-axis.

### Odd Functions:

If $$f(x)$$ is a real-valued function, then $$f$$ is odd if the following holds for all $$x$$ in the domain of $$f$$

$$-f(x) = f(-x)$$

or

$$f(x) + f(-x) = 0$$

Geometrically, the graph of an odd function has *rotational* symmetry with respect to the origin, meaning that the graph is unchanged if we rotate it 180 degrees about the origin.

### Properties:

* If $$f$$ is both even and odd, then $$f(x) = 0$$ for all $$x$$.
* If $$f$$ is odd, then $$\lvert f \rvert$$ is even.
* Linear combinations of even functions are even.
* Linear combinations of odd functions are odd.
* The sum of an odd function with an even function is neither even nor odd, unless one of the functions is equal to zero over the given domain.
* The product of two even functions is an even function.
* The product of two odd functions is an even function.
* The product of an even function with an odd function is an odd function.
* The composition of two even functions is even.
* The composition of two odd functions is odd.
* The composition of an even function and an odd function is even.
* Every function $$f(x)$$ can be written uniquely as the sum of an even function and an odd function:

  $$f(x) = f_e(x) + f_o(x)$$,

  where

  $$f_e(x) = \frac{1}{2}[f(x) + f(-x)]$$

  is even and

  $$f_o(x) = \frac{1}{2}[f(x)-f(-x)]$$

  is odd.
* Odd functions are not closed under scalar multiplications, but even functions are.
* The derivative of an even function is odd.
* The derivative of an odd function is even.
* The integral of an odd function from $$-a$$ to $$a$$ is zero if there are no vertical asymptotes between $$-a$$ and $$a$$.
* The integral of an even function from $$-a$$ to $$a$$ is twice the integral from $$0$$ to $$a$$ if there are no vertical asymptotes between $$-a$$ and $$a$$.
* The Maclaurin series of an even function includes only even powers.
* The Maclaurin series of an odd function includes only odd powers.
* The Fourier series of an even periodic function includes only cosine terms.
* The Fourier series of an odd periodic function includes only sine terms.

Of these properties, I've found myself needing to use the integral properties the most.