---
layout: post
title: Delegates
subtitle: A Python implementation
meta: A Python implementation of delegates. A delegate is an object to which a task is delegated. The purpose of delegation is to decouple code and add flexibility.
---

At my work this summer I've had the privilege to work on a code base that was very well-designed. As a result, I feel I have substantially grown as a developer. One of the neatest parts of the project I've been working on is that there are these magical things called *delegates* that glue the code together. These magical entities are what I want to talk about here.

Before we begin however, I want to define something called a *functor*. For our purposes, a functor is any kind of callable object: a function, class method, or even a class with the `__call__()` magic method defined.

Suppose you have a piece of software that looks like the following:

<img class="centered" src="{{ "/assets/posts/delegates/software.svg" | prepend: site.baseurl }}" alt="Software layout.">

Delegates are what handle the flow of data from one component to the next. All we do with the implementation here is set up each individual component and then choose who is subscribed to what. Then all we do is pipe data in and watch it come out the other side.

To be sure, delegates have other use cases, but this is what I was exposed to, and it was nifty enough that I wanted to take a crack at my own implementation. It was simple enough that, not including the substantial amount time I spent on a trivial misunderstanding, I only spent an hour on the implementation, plus another for some polish.

Before I show you the implementation, I want to show you how it's used. Here's a simple example that calculates the squares of the first ten even numbers. Delegates are overkill for such a simple task, but I wanted something easy to understand. Here's a diagram of what exactly is happening:

<img class="centered" src="{{ "/assets/posts/delegates/example-layout.svg" | prepend: site.baseurl }}" alt="Software layout.">

The end result is that of applying the function $$\displaystyle f(n) = \left(2(n + 1)\right)^2$$. [Here's](https://github.com/Notgnoshi/notgnoshi.github.io/blob/master/_includes/snippets/delegates/main-simple.py) the code

```python
{% include snippets/delegates/main-simple.py %}
```

I've included an `Observer` object in the chain because we need some way to view the result of our calculations, which are as follows:

```
~ $ ./main-simple.py
Observed value(s): 4
Observed value(s): 16
Observed value(s): 36
Observed value(s): 64
Observed value(s): 100
Observed value(s): 144
Observed value(s): 196
Observed value(s): 256
Observed value(s): 324
Observed value(s): 400
```

Now, as it stands, each of the modifier classes are implemented as callable objects. This is not necessary, I chose to do so for the convenience. We could do something like the [following](https://github.com/Notgnoshi/notgnoshi.github.io/blob/master/_includes/snippets/delegates/main-advanced.py):

```python
{% include snippets/delegates/main-advanced.py %}
```

Now for the implementation. I think we'll start with the simplest object: the [`Observer`](https://github.com/Notgnoshi/notgnoshi.github.io/blob/master/_includes/snippets/delegates/observer.py) class. `Observer` inherits from `Delegated`, which provides a base constructor, `subscribe()`, and `unsubscribe()`. We call the base class constructor, and then we define the `__call__()` method. `__call__()` takes in arbitrary arguments, prints them, and the passes them on unchanged to the delegate.

```python
{% include snippets/delegates/observer.py %}
```

The next thing to look at is the [modifier](https://github.com/Notgnoshi/notgnoshi.github.io/blob/master/_includes/snippets/delegates/modifiers.py) classes:

```python
{% include snippets/delegates/modifiers.py %}
```

These are fairly self explanatory: instead of passing on what they are given unchanged, they modify their input somehow before calling their delegates in the values.

Now for the implementation of the [`Delegated`](https://github.com/Notgnoshi/notgnoshi.github.io/blob/master/_includes/snippets/delegates/delegate.py) base class. A `Delegated` class has a `self.delegate` member, and two methods: `subscribe()` and `unsubscribe()`.

```python
{% include snippets/delegates/delegate.py %}
```

The `Delegate` class is where the magic happens. What I've defined a `Delegate` to be is a list of functors, all of which will be called on the given value(s) when the delegate is called. This way a `Delegated` class has *one* delegate, but an *arbitrary* number of subscribers. I overload `+=` and `-=` for convenience to subscribe functors to a delegate, doing some sanity checks along the way.

---

I've shown how delegates can be used in a very simple manner, but please realize, the magic between the input and the output could be *extremely* complex. Perhaps each *component* in a piece of software is in fact complex enough to require *subcomponents* glued together with delegates.

One of the neat things about delegates is it allows you to insert an arbitrary component in the middle of a complex system with minimal wrangling.

---

I hope you enjoyed reading this, I certainly enjoyed writing it!
