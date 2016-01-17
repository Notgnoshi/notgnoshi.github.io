---
layout: post
title: 03 Development of the Integrating Factor Method
categories: [notes, diff]
---

Given a differential equation $$y' + 3y = e^{2x}$$ we can see that it is not **separable**. Purely by magic we are going to multiply through by $$e^{3x}$$ to find the solution.

$$e^{3x}y' + 3ye^{3x} = e^{5x}$$

Note that the expression on the left might look familiar if you squint at it hard enough. It's a **product rule** $$fy' + f'y$$. We can replace the left hand side with the expression $$(e^{3x}y)'$$ and solve it by integrating both sides.

$$ \int{ (e^{3x}y)' } = \int{ e^{5x} } $$

$$ e^{3x}y = \frac{1}{5}e^{5x} + C $$

$$ y = \frac{1}{5}e^{2x} + Ce^{-3x} $$

Great, we've solved it, and it wasn't that hard. But how did we know to multiply by the *factor* $$e^{3x}$$ in order to make *integrating* easier?

In general, given a **first order linear** differential equation of the form $$a_1(x)y' + a_0(x)y = g(x)$$ we reduce it to the **standard form** for first order linear DEs assuming that $$a_1(x) \ne 0$$ for all $$x$$.

$$y' + \frac{a_0(x)}{a_1(x)}y = \frac{g(x)}{a_1(x)} $$

$$y' + P(x)y = f(x) $$

We multiply this standard form by some unknown function $$u(x)$$

$$u(x)y' + u(x)P(x)y = u(x)f(x)$$

We attempt to find a $$u(x)$$ such that $$u'(x) = u(x)P(x)$$. The differential equation $$\frac{du}{dx} = uP(x)$$ is separable. Solving for $$u$$

$$\int{\frac{du}{u}}= \int{P(x)\,dx}$$

$$ \ln u = \int{P(x)\,dx} $$

$$ u = e^{\int{P(x)\,dx}} $$

This factor $$u$$ is called the **Integrating Factor**. Note that no constant of integration $$C$$ is given, because it so works out that if it is given, it cancels out.

Taking the above example $$y' + 3y = e^{2x}$$ again we find the integrating factor to find the solution to the differential equation.

$$y' + 3y = e^{2x}$$

$$P(x) = 3$$

$$u = e^{\int{3\,dx}} = e^{3x}$$

$$uy' + 3uy = ue^{2x}$$

$$e^{3x}y' + 3e^{3x}y = e^{5x}$$

$$(e^{3x}y)' = e^{5x}$$

$$e^{3x}y = \frac{1}{5}e^{5x} + C$$

$$ y = \frac{1}{5}e^{2x} + Ce^{-3x} $$

#### Notes About First Order Linear Differential Equations:

* Standard form: $$y' + P(x) = f(x)$$
* Integrating factor $$u(x) = e^{\int{P(x)\,dx}}$$
* Multiplying the standard form by the integrating factor always produces $$(u(x)y)' = u(x)f(x)$$
* The integrating factor produces the general solution to the differential equation. Every choice of constant produces a solution, and every solution can be represented by an appropriate constant.
* The **largest interval $$I$$ over which the solution is defined** is the largest interval over which $$P(x)$$ and $$f(x)$$ are continuous
* Continuity: A function is **discontinuous** where the denominator is zero for most functions. Or where the functions are undefined. Think about the domains of functions.
* **Transient Terms**: $$e^{-x}$$ is transient because as $$x \to \infty, e^{-x} \to 0$$. $$T(x)$$ is a **transient term** if $$\displaystyle{\lim_{x \to \infty} T(x) = 0}$$.
