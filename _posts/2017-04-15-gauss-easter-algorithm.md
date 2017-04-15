---
layout: post
title: The Easter Algorithm
meta: How to determine the date Easter occurs on given the year
---

As per [this](http://www.staff.science.uu.nl/~gent0113/hovo/downloads/text1_08b.pdf) paper, you can determine what the date of Easter will be on a given year with the following Python snippet. There are other algorithms outlined in the given paper. Some are better than others. This is Gauss's. Note that the given paper also outlines *when* this algorithm is valid.

```python
def gauss_easter(year):
    k = year // 100
    p = (13 + 8*k) // 25
    q = k // 4
    M = (15 + k - q - p) % 30
    N = (4 + k - q) % 7
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + M) % 30
    e = (2*b + 4*c + 6*d + N) % 7

    # special cases:
    if d is 28 and e is 6:
        return "April 19"
    elif d is 28 and e is 6 and (11*M + 11) % 30 < 19:
        return "April 18"
    # In general
    elif (d + e) <= 9:
        return "March {}".format(22 + d + e)
    elif (d + e) > 9:
        return "April {}".format(d + e - 9)
    else:
        return None
```
