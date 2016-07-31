---
layout: post
title: Compliments of Numbers
meta: A description of the compliment of a number in different bases. Also covers subtraction using compliments
---

### Diminished radix compliment

Given a number $$N$$ in base $$r$$ with $$n$$ digits, the $$(r - 1)$$'s compliment of $$N$$, called the **diminished radix compliment**, is defined as

$$(r^n - 1) - N$$

In base 10 we would take the 9's compliment; in base 457 we would take the 456's compliment. For example, the 9's complement of 546700 (a 6-digit number) is $$\underbrace{999999}_{\text{6 digits}} - 546700 = 453299$$.

Note that $$r^n - 1$$ will always be an $$n$$ digit number (in base $$r$$) with each digit equal to $$r - 1$$.

Base 2 deserves special attention. In binary, we have $$2^n - 1 = \underbrace{11 \dots 1}_{n\text{ digits}}$$. Thus when we take $$(2^n - 1) - N$$, bitwise, regardless of what $$N$$ is, we have either $$1-0$$ or $$1-1$$, which is equivalent to flipping each bit. Thus the 1's complement of $$1011000$$ is $$0100111$$.

### Radix complement

The **$$r$$'s complement** of an $$n$$ digit number $$N$$ in base $$r$$ is defined as

$$\begin{cases}0 &\text{for } N = 0 \\ r^n - N &\text{otherwise}\end{cases}$$

Algebraically, we can see that the $$r$$'s compliment can be obtained by adding 1 to the $$(r-1)$$'s compliment:

$$r^n - N = \left[ (r^n - 1) - N\right] + 1$$

This is useful in binary, because the 1's compliment is extremely easy to calculate. For example, the 2's compliment of $$101100$$ is $$010011 + 1$$ which is easily calculated to be $$010100$$.

---

If the number $$N$$ contains a radix (decimal) point, we completely ignore it, calculate the complement, and add it back in the same relative position. We can also see that the *complement of the complement leaves the number $$N$$ unchanged:*

$$\begin{cases}r^n - (r^n - N) = N \\ \displaystyle{(r^n - 1) - \left[ (r^n - 1) - N\right] = N}\end{cases}$$

### Subtraction without subtraction

Computers can add *really* well, but subtraction is another matter. This means that engineers had to find a way to subtract two numbers without ever performing subtraction.

Here's how computers subtract $$M - S$$ (*minuend* - *subtrahend*), both $$n$$ digit unsigned numbers in base $$r$$

* Add $$M$$ to the $$r$$'s compliment of $$S$$

  $$M + (r^n - S) = M - S + r^n$$

* If $$M \geq S$$ the sum will produce a carry that can be discarded
* If $$M < S$$, the sum does not produce a carry and is equal to $$r^n - (S - M)$$, which is the $$r$$'s compliment of $$(M - S)$$. To obtain the proper answer, take the $$r$$'s compliment of the sum and place a negative sign in front.

---

What about signed numbers?

If the value $$8_{10} = 0100_2$$ in a $$4$$-bit system, then $$-8_{10} = 1100_2$$. With this convention, addition of signed binary numbers is incredibly simple; you simply add the 2's compliment of the signed numbers together, including their sign bits. If the two sign bits are both 1, (both negative numbers) we discard the sum and replace it with 0. We then take the 2's compliment of this result to get the result.
