---
layout: post
title: 04 More Logical Rules
categories: [notes, finite]
---

Today's class was spent covering a bunch of properties similar to the **Associative Property** and **commutativity** we learned in grade school. Logical connectives have similar rules, and that's what we spent today's lecture on.

A compound proposition that is *always* true regardless of its input is called a **tautology**. A proposition that is *always* false is a **contradiction**. Everything else is a **contingency**.

The compound propositions $$p$$ and $$q$$ are called **logically equivalent** if $$p \iff q$$ is a tautology. The notation $$p \cong q$$ denotes that $$p$$ and $$q$$ are logically equivalent.

The following is a list of logical equivalences.

There are the **Identity Laws**

$$p \land T \cong p$$

$$p \lor F \cong p$$

The **Domination Laws**, which can be used to the programmer's advantage in so called "short circuits" to increase efficiency. If you have a conditional statement that checks something computationally intensive, sometimes you can take advantage of these forms so that much of the time the code runs it will recognize that it doesn't have to check the intensive part of the conditional statement.

$$p \lor T \cong T$$

$$p \land F \cong F$$

There are the **Idempotent Laws**

$$p \lor p \cong p$$

$$p \land p \cong p$$

The **Double Negation Law**

$$\neg ( \neg p ) \cong p$$

The **Commutative Laws**

$$p \lor q \cong q \lor p$$

$$p \land q \cong q \land p$$

The **Associative Laws**

$$(p \lor q) \lor r \cong p \lor ( q \lor r)$$

$$(p \land q) \land r \cong p \land (q \land r)$$

The **Distributive Laws**

$$p \lor (q \land r) \cong (p \lor q) \land (p \lor r)$$

$$p \land (q \lor r) \cong (p \land q) \lor (p \land r)$$

**De Morgan's Laws**

$$\neg (p \land q) \cong \neg p \lor \neg q$$

$$\neg (p \lor q) \cong \neg p \land \neg q$$

The **Absorption Laws**

$$p \lor (p \land q) \cong p$$

$$p \land (p \lor q) \cong p$$

The **Negation Laws**

$$p \lor \neg p \cong T$$

$$p \land \neg p \cong F$$

There are also many logical equivalences that involve conditional statements:

$$p \to q \cong \neg p \lor q$$

$$p \to q \cong \neg q \to \neg p$$

$$p \lor q \cong \neg p \to q$$

$$p \land q \cong \neg (p \to \neg q)$$

$$\neg (p \to q) \cong p \land \neg q$$

$$(p \to q) \land (p \to r) \cong p \to (q \land r)$$

$$(p \to r) \land (q \to r) \cong (p \lor q) \to r$$

$$(p \to q) \lor (p \to r) \cong p \to (q \lor r)$$

$$(p \to r) \lor (q \to r) \cong (p \land q) \to r$$

There are also a handful of equivalences that involve biconditional statements:

$$p \iff q \cong (p \to q) \land (q \to p)$$

$$p \iff q \cong \neg p \iff \neg q$$

$$p \iff q \cong (p \land q) \lor (\neg p \land \neg q)$$

$$\neg( p \iff q) \cong p \iff \neg q$$

Of all of these many laws, **De Morgan's** are probably the most important.

Complex compound logical propositions can often be simplified by some combination of these rules.

We say that a compound proposition is **satisfiable** if there is an assignment of truth values to its variables that makes it true. When no such assignment exists, the proposition is **unsatisfiable**. When we find a particular assignment of truth values that makes a compound proposition true, that assignment is called a **solution** to that proposition.
