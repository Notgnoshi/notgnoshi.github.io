---
layout: post
title: "Error in Numerical Computation"
subtitle: "A.K.A. `Fun with Taylor Series'"
meta: A description of error using the Taylor Series in numerical computation
redirect_to: https://agill.xyz/blog/error-in-numerical-computation
---
<!-- Custom styles for the binary_word -->
<link rel="stylesheet" href="{{ "/assets/styles/binary_word.css" | prepend: site.baseurl }}">

## Error

Often in Numerical Analysis we have to make approximations to numerically compute things. That's the thing; in Calculus we can take limits and arrive at exact results, but when we use a computer to calculate, say something simple like a derivative, we can't take an infinite limit so we have to approximate the answer, and therefore, it has error. Computers are limited in their capacity to store and calculate the precision and magnitude of numbers.

We can characterize error in measurements and computations with respect to their **accuracy** and their **precision**. Accuracy refers to how closely a calculated value agrees with the *true* value. Precision refers to how closely calculated values agree with each other. **Inaccuracy** (also called *bias*) is a systematic deviation from the true values. **Imprecision** (also called *uncertainty*) refers to how close together calculated results are to each other. We use the term **error** to represent both inaccuracy and imprecision in our results.

The relationship between the exact result and the approximation can be formulated as

$$\text{true value} = \text{approximation} + \text{error}$$

We can rearrange the above equation to find an expression for the **absolute** or **true error** ($$E_t$$)

$$E_t = \text{true value} - \text{approximation}$$

This definition of error is flawed however, as it doesn't normalize the error with respect to the magnitude of the values in question. A better definition, called  **relative error** ($$\varepsilon_t$$) can be defined as follows

$$\varepsilon_t = \frac{\text{true value} - \text{approximation}}{\text{true value}}$$

Note that this value will be between 0 and 1 and can be expressed as a percent by multiplying by 100%.

---

However, we live in the real world; we oftentimes do not know the true value of a computation, so the above formulas become useless. For these situations, we can normalize the error with respect to the approximation itself

$$\varepsilon_a = \frac{\text{approximate error}}{\text{approximation}}$$

This is relatively useless however, as we don't really have a way to calculate the approximate error.

Oftentimes, when performing numerical computation, we use an **iterative** process. Hopefully, when performing these iterations, the **approximate relative error** as follows

$$\varepsilon_a = \frac{\text{current approximation} - \text{previous approximation}}{\text{current approximation}}$$

can be used to determine if we are performing successively better computations.

The signs of these errors can be either positive or negative dependent on the situation, so it is customary to take the absolute value of the error calculations as it's only the magnitude of error that we are concerned with.

One last thing before moving on is the **stopping condition** or **criterion** $$\varepsilon_s$$ defined as the amount of error below which we don't care about. In other words, we repeat an iterative computation until $$\mid\varepsilon_a\mid \lt \varepsilon_s$$. It can be shown that if the following criterion in terms of $$n$$ is met, we know the result is correct to at least $$n$$ significant figures.

$$\varepsilon_s = 0.5 \times 10^{2-n}$$

## Roundoff Error

**Roundoff error** occurs because computers cannot represent some quantities exactly. Knowledge of roundoff error is important because they can lead to incorrect results. In some cases even, they can lead to a calculation becoming unstable and yielding obviously erroneous results. These calculations are called **ill-conditioned**.

There are two major facets of roundoff error often involved with numerical calculations.

* Computers have magnitude and precision limits on the numbers they can store and calculate.
* Certain numerical calculations are very sensitive to roundoff errors. This can be from the mathematical structure of the calculations as well as how the computers perform the operations.

### Computer Representation of Integers

Numbers (and other data) are stored in *bit*strings consisting of 0's and 1's. Because we only have two digits to store our numbers with (represented inside the computer as high and low voltages) this is called a **binary** (or base-2) number system.

The number system we use in everyday language is called the base-10 or **decimal** number system. We use ten digits (0-9) to represent numbers. Note that the symbol we use to represent a number is independent of the number itself. So conceivably, we could represent any number with a combination of symbols as long as we agree what the symbols mean beforehand.

We learned in grade school (maybe earlier, I can't remember) how to count 1, 2, 3, ... But what happens when we get to 9? We've run out of symbols, so obviously we need more symbols, right? Well, thankfully someone smarter than me devised the decimal number system. We know that the collection of symbols "437" represents the number "four hundred and thirty-seven". We can deconstruct the number into 4 100's, 3 10's, and 7 1's ($$4\times100 + 3\times10 + 7\times1$$).

We can do the same thing with 1's and 0's, but it'll just take a longer string of symbols to represent the same number. With just 1 digit, (1 and 0) we can represent two values (0 and 1). With 2 digits (00, 01, 10, 11), we can represent four numbers (0, 1, 2, 3). It turns out that if we have $$n$$ digits, we can represent $$2^n$$ numbers in the binary number system. This is no different than the decimal number system. With $$n$$ digits, we can represent $$10^n$$ numbers. With 1 digit, we can represent 10 numbers (0-9), with two, we can represent 100 numbers (0-99)!

Things get more complicated when we try to do floating-point numbers like 32.4, but we'll get there. In the mean time, let's look more at representing integers in base-2.

In decimal, we can represent signed numbers with the "-" symbol, but in binary, we're going to reserve one of the **bits** (binary digit) in a word who's only job is to tell us whether the number is positive or negative. Typically this is the very first bit in a word, (1 for negative) and it's called the **sign bit**.

For example, using a 16-bit word size (typically computers currently use 32 or 64 bits), the following is how a computer would store -173

$$1000000010101101_2$$

Note we use a subscript 2 to remind ourselves it's a binary number (though the 1's and 0's kind of give it away). This is equivalent to saying the following

$$1000000010101101_2 = -(2^7 + 2^5 + 2^3 + 2^2 + 2^0) = -(128 + 32 + 8 + 4 + 1) = -137_{10}$$

The 1 in the very first location tells us it's a negative number, and the 1's in the 7th, 5th, 3rd, 2nd, and 0th spot tell us to sum together 2 raised to the power of their respective indices. The following is a 16-bit table with the position indices underneath.

<table class="binary_word">
    <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>15</td>
        <td>14</td>
        <td>13</td>
        <td>12</td>
        <td>11</td>
        <td>10</td>
        <td>9</td>
        <td>8</td>
        <td>7</td>
        <td>6</td>
        <td>5</td>
        <td>4</td>
        <td>3</td>
        <td>2</td>
        <td>1</td>
        <td>0</td>
    </tr>
</table>

If we use 1 bit for the sign, that leaves us with 15 others to represent binary numbers 0 to 111111111111111. This upper limit in decimal is 32,767. Note that this value can be found by simply evaluating $$2^{15} - 1$$. Therefore, a 16-bit word can represent integers ranging from -32,767 to 32,767. However, because 0 and -0 are really the same, we can use 1000000000000000 to denote an additional negative number, extending our range by one.

For an $$n$$-bit word, we can represent values in the range $$-2^{n-1}$$ to $$2^{n-1} - 1$$.

This isn't exactly how computers typically represent signed numbers however. A technique called the **2s Complement** directly incorporates the sign into the numbers magnitude rather than reserving a bit just for the sign. Regardless, the number ranges are exactly the same as described above.

### Computer Representation of Floating-Point Numbers

Fractional quantities are typically represented very similar to how we think about scientific notation.

$$\pm s \times b^e$$

where $$s$$ is the **significand** or **mantissa**, $$b$$ is the **base** of the number system being used, and $$e$$ is the **exponent**. Prior to using this form however, the number is **normalized** by shifting the decimal place so that there is only one significant digit left of the decimal point. This is done so the computer doesn't store needless zeros.

---

Let's create a toy system in base-10 with a 5-digit word size.

We use one digit for the sign, two for the exponent and two for the mantissa. Note that the exponent can be both positive and negative, so we have one digit for the sign, and one for the magnitude. This gives us the following generalization

$$s \cdot d_1.d_2 \times 10^{s_e d_e}$$

Let's play around with this toy system. What's the largest value it can represent? That would be $$+9.9 \times 10^{+9}$$. which is just a little less than 10 billion.

What's the smallest (positive) value we can represent? That would be $$+1.0 \times 10^{-9}$$ We can represent the smallest and largest representable negative numbers similarly.

How bad is the roundoff error in this toy system? Well, it's pretty bad. There is a "hole" around zero, and there are also "holes" between numbers that we can represent. For example, the number 0.03125 would have to be stored as $$3.1 \times 10^{-2}$$, or 0.031. This introduces error, and in this case it represents a true relative error of

$$\varepsilon_t = \frac{0.03125 - 0.031}{0.03125} = 0.008$$

The following is the number line showing some of the limitations of our toy system

<img class="centered-full" src="{{ "/assets/posts/floating-point-math/error.svg" | prepend: site.baseurl }}" alt="number line holes">

A more subtle limitation is the gaps between the representable numbers. Note that the gap size is relative to the magnitude of the numbers being represented. For numbers with an exponent of -1 (between 0.1 and 1), the number spacing is on intervals of 0.01. For ever increase in exponent, the gap size decreases by a factor of ten. For example, with an exponent of 1, the spacing increases to a gap size with width 0.1. This means roundoff error is proportional to a number's magnitude. It also means that the relative error *has an upper bound*. This upper bound is called the **machine epsilon**.

---

We talked just a bit earlier about normalizing numbers in scientific notation, that is, taking $$0.0034 \times 10^{0}$$ and converting it to $$3.4 \times 10^{-3}$$. Because binary numbers consist of *only* 1s and 0s, we know for a fact that if a number is normalized the leading digit is a 1. This means that we don't even have to store it!

Therefore, nonzero floating point numbers in base-2 can be represented as

$$\pm (1 + f) \times 2^e$$

where $$f$$ is the mantissa and $$e$$ is the exponent.

---

The standard **IEEE Double-Precision Format** uses 8 *bytes* (64 bits) to represent floating-point numbers. You can read about it in more detail [here](https://en.wikipedia.org/wiki/IEEE_floating_point). The following is how those 64 bits are broken up into the exponent and mantissa.

<table class="floating_point">
    <tr>
        <td>1 bit</td>
        <td>11 bits</td>
        <td>52 bits</td>
    </tr>
    <tr>
        <td>Sign</td>
        <td>Signed Exponent</td>
        <td>Mantissa</td>
    </tr>
</table>

The largest representable value is $$1.7977 \times 10^{308}$$ (let's call it `realmax`) and the smallest positive representable value is $$2.2251 \times 10^{-308}$$ (let's call it `realmin`). The **machine epsilon** of this format is $$2^{-52} = 2.2204 \times 10^{-16}$$ (let's call it `eps`). Numbers occurring in computations larger than the max value `realmax` **overflow**, and numbers smaller than `realmin` **underflow**. Different languages handle overflow and underflow differently. in MATLAB overflows are set to `inf` and underflows are set to `0`. In C, they are handled similarly for floating point numbers. For integers in C, exceeding `realmax` will reset to the other end of the spectrum (`-realmax`)

One way to calculate the machine epsilon on your system is to find the smallest number $$\varepsilon$$ such that $$0 + \varepsilon \ne 0$$ (i. e. the smallest possible gap between two numbers). In Python, an easy way of getting the machine epsilon is with NumPy:

```python
import numpy as np

print(np.finfo(float).eps)       # 2.22044604925e-16
print(np.finfo(np.float32).eps)  # 1.19209e-07
print(np.finfo(np.float64).eps)  # 2.22044604925e-16
```

You can also calculate the machine epsilon for a given data type using the following Python snippet

```python
def machineEpsilon(func=float):
    eps = func(1)
    while func(1) + func(eps) != func(1):
        eps_last = eps
        eps = func(eps) / func(2)
    return eps_last
```

```python
>>> import numpy as np
>>> machineEpsilon(float)
2.220446049250313e-16
>>> machineEpsilon(np.float64)
2.2204460492503131e-16
>>> machineEpsilon(np.float32)
1.1920929e-07
```

## Truncation Error

**Truncation error** arises when you use an approximation in place of an exact expression in a mathematical procedure. One of the best (and frequently used) examples of truncation errors is the Taylor Series approximation of a function.

Essentially, **Taylor's Theorem** states that any smooth function can be approximated by a polynomial. The **Taylor Series Expansion** of $$f(x)$$ at $$a$$ is

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)\cdot(x-a)^2}{2!} + \frac{f'''(a)\cdot(x-a)^3}{3!} + \cdots = \sum_{n=0}^\infty \frac{f^{(n)}(a) \cdot (x-a)^n}{n!}$$

Note that the equals signs are $$=$$ and not $$\approx$$. However, computers are discrete, finite machines. They can't perform infinite calculations like these, so we have to cut off the calculations somewhere. This results in truncation error (we truncate the expression).

When we truncate the Taylor series expansion to $$n$$ terms, there's some error left over, and we can include a remainder term $$R_n$$ to keep the $$=$$ signs exact.

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)\cdot(x-a)^2}{2!} + \frac{f'''(a)\cdot(x-a)^3}{3!} + \cdots + \frac{f^{(n)}(a)\cdot(x-a)^n}{n!} + R_n$$

where

$$R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!} \cdot h^{n+1}$$

accounts for terms $$n+1$$ all the way to $$\infty$$ and $$\xi$$ lies somewhere between the point we're interested in $$x$$ and the point we're expanding about $$a$$, with the distance, or step size, between them $$h$$.

We have no control over the value of $$\xi$$ (it's determined by what we're approximating), but we *can* control $$h$$ and $$n$$.

This expression $$R_n$$ means that the truncation error of an $$n$$th order Taylor series approximation is proportional to the term $$h^{n+1}$$ and is often written as $$R_n = O(h^{n+1})$$, where $$O$$ is the same [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation) used in computer science, taken to mean the truncation error is "order $$h^{n+1}$$".

If our approximation is $$O(h)$$, or a **first order** approximation, halving the step size will halve the error. If our approximation is $$O(h^2)$$, halving the step size will quarter the error (**second order** approximation).

This means that there are two ways to decrease the truncation error in a Taylor series approximation: add more terms to the approximation, or decrease the step size $$h$$.

---

My Numerical Analysis professor constantly joked that the class should have been called "Fun with Taylor Series". It was no joke.

---

One final note. So far, I've talked about roundoff error and truncation error as two separate entities. In reality, the error in our system is the sum of both errors.

Due to something called **subractive cancellation**, *decreasing* truncation errors can result in *increasing* roundoff errors. This leads to a sweet spot, where the error is as low as it can get. For more information, here's a video explaining it a bit more:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ak_pxGwku0M" frameborder="0" allowfullscreen class="centered"></iframe>
