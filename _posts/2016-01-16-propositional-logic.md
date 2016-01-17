---
layout: post
title: 01 Intro to Propositional Logic
categories: [notes, finite]
---

At first blush there seems to be several types of logic. There's logic that's all about **AND**s, **OR**s, quantifiers, mathematics, Boolean Algebra, and all that other jazz. There's also that logic that liberal arts majors take, which is all about syllogisms, debates, and the English language. These are the same type of logic though, and they follow the same rules. And they're both useful.

The first term to define is the **Proposition**. A proposition is a declarative statement that is either **true** or **false**, but not both. $$1 + 2 = 42$$ is a proposition. "It is raining" is also a proposition. An example of a statement that is *not* a proposition would be $$x + 1 = 2$$. This statement's **truth value** is dependent on the value of $$x$$.

Mathematicians and computer scientists are a lazy breed, and prefer to use symbols to denote statements rather than writing out the same statement multiple times. We use letters $$p, q, r, s,...$$ as **propositional variables** to represent a particular proposition.

Many (if not most) mathematical statements are constructed by combining multiple propositions together. These new **compound propositions** are formed by linking together existing propositions using **logical operators**.

Let $$p$$ be a proposition. The **negation** of $$p$$, denoted by $$\neg p$$ (also $$\bar p$$) is the statement "It is not the case that $$p$$." The proposition $$\bar p$$ is read "note $$p$$." The truth value of $$\bar p$$ is the opposite of the truth value of $$p$$.

For example, the negation of the proposition "Will's computer has a sticker on the lid." is the statement "It is not the case that Will's computer has a sticker on the lid.", or more simply, "Will's computer does not have a sticker on the lid."

Let $$p$$ and $$q$$ be propositions. The **conjunction** of $$p$$ and $$q$$, denoted by $$p \land q$$, is the proposition "$$p$$ *and* $$q$$". The conjunction $$p \land q$$ is true only when both $$p$$ and $$q$$ are true, and is false otherwise.

Let $$p$$ and $$q$$ be propositions. The **disjunction** of $$p$$ and $$q$$, denoted by $$p \lor q$$, is the proposition "$$p$$ *or* $$q$$". The conjunction $$p \lor q$$ is false when both $$p$$ and $$q$$ are false, and is true otherwise.

The use of the disjunction in ordinary English corresponds to one of two meanings, and deserves careful consideration. The disjunction corresponds to the **inclusive or**. The disjunction is true when at least one of the two propositions is true. On the other hand, the **exclusive or** is true when one or the other proposition is true, but *not* both.

Let $$p$$ and $$q$$ be propositions. The **exclusive** of $$p$$ and $$q$$, denoted by $$p \oplus q$$, is the proposition that is true when exactly one of $$p$$ and $$q$$ is true, and is false otherwise.

Let $$p$$ and $$q$$ be propositions. The **conditional statement**  $$p \to q$$ is the proposition "if $$p$$ then $$q$$." The conditional statement $$p \to q$$ is false when $$p$$ is true and $$q$$ is false, and true otherwise. In the conditional statement $$p \to q$$, $$p$$ is called the **hypothesis** and $$q$$ is called the **conclusion**.

The conditional statement is also often called an **implication**. The conditional statement plays a vital role in mathematical reasoning, and a wide variety of phrasing is used to mean $$p \to q$$. A small sampling is given below.

* "If $$p$$, then $$q$$."
* "$$p$$ implies $$q$$"
* "$$p$$ is sufficient for $$q$$."
* "$$q$$ is necessary for $$p$$."
* "$$p$$ only if $$q$$."
* "$$q$$ if $$p$$."
* "$$q$$ when $$p$$."
* "A necessary condition for $$p$$ is $$q$$."
* "$$q$$ unless $$\neg p$$."
* "$$p$$ only if $$q$$."

An important thing to note is that $$p$$ might not be the *only* condition that is sufficient for $$q$$, so if $$q$$, we cannot necessarily infer $$p$$.

The **converse** of the conditional statement $$p \to q$$ is $$q \to p$$. The **inverse** of $$p \to q$$ is the proposition $$\neg p \to \neg q$$. The **contrapositive** of $$p \to q$$ is $$\neg q \to \neg p$$. The converse and inverse are logically identical, and so are the contrapositive and the conditional statements. When two compound propositions have the same truth value, we call them **equivalent**.

Let $$p$$ and $$q$$ be propositions. The **biconditional statement** $$p \iff q$$ is the proposition "$$p$$ if and only if $$q$$." The biconditional statement $$p \iff q$$ is true when $$p$$ and $$q$$ have the same truth values, and is false otherwise. Biconditional  statements are also called **bi-implications**.

As with the conditional statement, there are several common ways to express $$p \iff q$$ in the English language.

* "$$p$$ is necessary and sufficient for $$q$$."
* "if $$p$$ then $$q$$, and conversely."
* "$$p$$ iff $$q$$."

The last method of expressing $$p \iff q$$ is read as "$$q$$ if and only if $$p$$." Note that $$p \iff q$$ is equivalent to $$ (p \to q) \land (q \to p)$$.

What about logical operator precedence? The following is a list of logical operators in descending precedence: $$(), \neg, \land, \lor, \to, \iff$$.

The very last portion of propositional logic breaks away from purely logical statements and brings the topic back closer to computer science. I'm sure you've heard that computers run using ones and zeroes. In fact, computers store data at the lowest level of abstraction using **bits** (*b*inary dig*it*). A **1** is represented inside the computer as an electrical signal past some threshold voltage, and a **0** is a signal below that threshold. Computer scientists represent **True** with **1** and **False** with **0**. As is typical, in the context of computer **bit operations** we will use the notation **OR**, **AND**, **XOR**, and **NOT** to represent the operators $$\lor, \land, \oplus,$$ and $$\neg$$.

Often, a single bit, or even a **bit string** (a series of bits) is represented by a variable called a **Boolean variable**, ($$A, B, C...$$) and this study of logic is often called **Boolean Algebra**.

As a last note, [DeMorgan's Laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) are an important part of Boolean Algebra. In short, they say

$$\neg (p \land q) \equiv \neg p \lor \neg q$$

$$\neg (p \lor q) \equiv \neg p \land \neg q$$

The symbol $$\equiv$$ means two propositions are **logically equivalent**, and is *not* a logical connective.
