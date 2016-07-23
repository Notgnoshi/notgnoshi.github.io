---
layout: post
title: What is Abstract Algebra?
meta: A definition of algebraic structures and abstract/modern algebra
---

If someone were to ask you what "algebra" was, most people would answer something to the effect of "It's the process of solving equations". Indeed, this is most people's experience with algebra. It's even how the discipline began, but it's not all there is to it.

---

Somewhere along the line in grade school, basic properties of addition and multiplication were introduced. Things like **associativity**, **commutativity**, the **distributivity** of multiplication over addition, and so on. We all got somewhat comfortable with these things, and they enabled us to solve algebraic equations  $$ax = b$$ or $$x^2 + 1 = 0$$.

### Matrix Algebra

However, the proverbial wrench appears in the works when we try to apply these same properties to more sophisticated structures like matrices. Recall that we add two matrices element-wise. That is,

$$\left(\begin{array}{cc} a & b \\ c & d \end{array}\right) + \left(\begin{array}{cc} p & q \\ r & s \end{array}\right) = \left(\begin{array}{cc} a + p & b + q \\ c + r & d + s\end{array}\right)$$

Recall that the "zero matrix" $$\boldsymbol{0} = \left(\begin{array}{cc} 0 & 0 \\ 0 & 0 \end{array}\right)$$ (sometimes denoted by $$\underline{0}$$) acts like the **neutral**, or **identity** element under matrix addition.

Matrix multiplication is more sophisticated. It's similar to the dot product of two vectors given by $$(a, b) \cdot (a', b') = a a' + b b'$$, that is, we multiply corresponding elements and then add the results together. If we want to multiply two matrices $$\boldsymbol{A}$$ and $$\boldsymbol{B}$$, to get the element in the first row, first column of $$\boldsymbol{AB}$$ we multiply the elements of the first row of $$\boldsymbol{A}$$ with the elements in the first column of $$\boldsymbol{B}$$ and add the results together. To get the first row, second column of $$\boldsymbol{AB}$$, we take the first row of $$\boldsymbol{A}$$ and the second column of $$\boldsymbol{B}$$.

The rules for matrix algebra are quite different from that of ordinary algebra in some respects. For example, matrix multiplication is not commutative, that is, the identity $$\boldsymbol{AB} = \boldsymbol{BA}$$ is simply not true. Additionally, we can multiply whatever two real numbers we like, but we can only multiply compatibly sized matrices, and if we want to be able to multiply in both directions ($$\boldsymbol{AB}$$ and $$\boldsymbol{BA}$$) the matrices have to be equally sized square matrices.

In normal algebra, if $$ab = ac$$ and $$a \neq 0$$, we can conclude that $$b = c$$. In matrix algebra we cannot make this conclusion. For example, take the following matrices:

$$\underbrace{\left(\begin{array}{cc} 0 & 0 \\ 0 & 1 \end{array}\right)}_{\boldsymbol{A}} \cdot \underbrace{\left(\begin{array}{cc} 1 & 1 \\ 1 & 1 \end{array}\right)}_{\boldsymbol{B}} = \left(\begin{array}{cc} 0 & 0 \\ 1 & 1 \end{array}\right) = \underbrace{\left(\begin{array}{cc} 0 & 0 \\ 0 & 1 \end{array}\right)}_{\boldsymbol{A}} \cdot \underbrace{\left(\begin{array}{cc} 0 & 0 \\ 1 & 1 \end{array}\right)}_{\boldsymbol{C}}$$

That is, we have $$\boldsymbol{AB} = \boldsymbol{AC}$$ but $$\boldsymbol{B} \neq \boldsymbol{C}$$. I'm not going to say much more, just that matrix algebra is obviously a somewhat different beast than "normal" algebra.

### Boolean Algebra

Boolean algebra, the famous **AND**, **OR**, and **NOT** from computer science is also formally the same as the algebra of sets. In particular, we may consider a set $$S$$ and the operations of **union** and **intersection** on arbitrary subsets of $$S$$. You might often see $$+$$ denote the union of two sets and $$\cdot$$ denote the intersection of two sets. I've seen this most in books dealing with Boolean algebra in the context of computer science, but as a convention, it is not unusual.

If we agree to use this notation, we might be tempted to check if the laws Boolean algebra obeys are the same as the laws of ordinary algebra. And indeed, some laws are the same. We have, for example, the following.

$$A + B = B + A \text{ and } A \cdot B = B \cdot A$$

$$A \cdot (B + C) = A \cdot B + A \cdot C$$

$$A + \emptyset = A \text{ and } A \cdot \emptyset = \emptyset$$

However, there are some identities that while true, have no counterpart in "normal" algebra.

$$A + (B \cdot C) = (A + B) \cdot (A + C)$$

$$A + A = A \text{ and } A \cdot A = A$$

$$ (A + B) \cdot A = A \text{ and } (A \cdot B) + A = A$$

This is not meant to dive deep into Boolean algebra, only to point out that there are multiple **algebras** out there that behave differently than our "normal" algebra.

---

This takes the general study of algebra past the study of solving equations. Broadly, the study of algebra is the study of the general principles that apply equally to *all possible algebras.*

In the most general sense (and I mean that quite literally), an algebra consists of a **set** and one or more **operations** on that set, where the operation is simply a method of combining two elements of that set to produce a third member of the same set. This structure, a set and its operations, is called an **algebraic structure**, and it's a quite abstract idea (hence the name *abstract* algebra).

It's important to note that these sets can truly be sets of anything, as long as we can define operations on them. For example, we could have a set of colors, where one of our operations is combining two colors to produce a third. This toy algebraic structure, under the color combination operation, is commutative. That is, it doesn't matter what order we combine two colors in, the end result is the same. This commutativity is an example of one of the properties of algebraic structures that algebraists study.

What we're doing is abstracting away the details of the individual objects at play and their properties, and instead focusing on how certain operations combine the objects together. This is essentially what abstraction is; selecting what is essential and throwing away the rest.

---

This is a simplistic view of abstract algebra, but at its heart, this is what it really boils down into. I find it fascinating.
