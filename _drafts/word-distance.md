---
layout: post
title: Levenshtein Distance
---

Suppose we want to transform one string into another. How might we describe the distance between the two words mathematically? The most common form of distance metric for strings is the [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance) distance between the first $$i$$ characters of $$a$$ and the first $$j$$ characters of $$b$$, given by

$$\operatorname{lev}_{a, b} (i, j) = \begin{cases} \max (i, j) & \text{if} \min (i, j) = 0, \\ \min\begin{cases}\operatorname{lev}_{a, b} (i-1, j) + 1 \\ \operatorname{lev}_{a, b} (i, j - 1) + 1 \\ \operatorname{lev}_{a, b} (i-1, j-1) + \operatorname{1}_{(a_i \neq b_j)}\end{cases} & \text{otherwise.} \end{cases}$$

where $$\operatorname{1}_{(a_i \neq b_j)}$$ is the indicator function equal to $$0$$ when $$a_i = b_j$$ and equal to $$1$$ otherwise. The Levenshtein distance corresponds to three possible operations on a string to transform it into another:

1. The *insertion* of a single character
2. The *deletion* of a single character
3. The *substitution* of one character for another

We can compute the Levenshtein distance as follows

{% highlight python %}
def levenshtein(source, target):
    ''' From Wikipedia article; Iterative with two matrix rows.'''
    if source == target:
        return 0
    elif len(source) == 0:
        return len(target)
    elif len(target) == 0:
        return len(source)

    v0 = [None] * (len(target) + 1)
    v1 = [None] * (len(target) + 1)

    for i in range(len(v0)):
        v0[i] = i

    for i in range(len(source)):
        v1[0] = i + 1

        for j in range(len(target)):
            cost = 0 if source[i] == target[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)

        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(target)]
{% endhighlight %}

and use it like so

{% highlight python %}
In [2]: levenshtein('philosophy', 'mathematics')
Out[2]: 11

In [3]: %timeit levenshtein('philosophy', 'mathematics')
10000 loops, best of 3: 62.1 us per loop
{% endhighlight %}

Note that this does not require that the intermediate words in the transformation be valid, this merely calculates the length of the shortest path between two words under the insertion, deletion, and substitution operations.
