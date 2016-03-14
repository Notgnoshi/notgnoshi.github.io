---
layout: post
title: Implementing GPIO on an Odroid-XU
---

I'm a part of the Robotics team at [SDSMT](www.sdsmt.edu) and one of the projects that I've been working on is getting pin I/O up and running on the Odroid-XU for our upcoming competition. I spent maybe 25 hours working on finding a library that makes working with GPIO easier, but was unable to find one for the Odroid-XU. I did end up finding [one](https://github.com/mlinuxguy/odpygpio) (it even works!). However, it exposed some details the user doesn't need to know, and, at least for me, doesn't care about. So I wrote a small Python wrapper to cover all the ugly stuff.

Here's what the end result looks like.

{% highlight python %}
from gpiolib import *

sys_init()

pinMode(27, OUTPUT)
digitalWrite(27, ON)

pinMode(24, INPUT)
val = digitalRead(24)

sys_clean()
{% endhighlight %}

I'm not sure how fast/responsive it is, but all we need to do is monitor a single pin to start up the code that handles the state machine and autonomous navigation for our robot, so it doesn't have to be fast.

Here's my wrapper for [mlinuxguy](https://github.com/mlinuxguy)'s code. I've removed all my error checking for clarity.

{% highlight python %}
import gpio as g

XU_GPIO_ADDR = 0x13400000  # Odroid-XU base GPIO address

OUTPUT = 1
INPUT = 0
ON = 1
OFF = 0

PULLDS = 0  # disable pull up/down
PULLUP = 1  # enable pull up
PULLDN = 2  # enable pull down

gpio_addresses = {13: [0x0c24, 5], 14: [0x0c44, 3], 15: [0x0c24, 2],
                  16: [0x0c24, 0], 17: [0x0c24, 6], 18: [0x0c24, 3],
                  19: [0x0c44, 6], 20: [0x0c44, 4], 21: [0x0c44, 5],
                  22: [0x0c44, 7], 23: [0x0c44, 2], 24: [0x0c44, 1],
                  25: [0x0c24, 7], 26: [0x0c44, 0], 27: [0x0c64, 1]}

def sys_init():
    """Initialize everything"""
    g.sys_init()

def sys_clean():
    """Cleans up mmap"""
    g.sys_clean()

def pinMode(pin, mode=INPUT):
    """Set `pin` to `mode` INPUT or OUTPUT. Defaults to INPUT."""
    g.pinMode(gpio_addresses[pin][0], gpio_addresses[pin][1], PULLDS, mode)

def digitalWrite(pin, state=OFF):
    """Write ON or OFF to `pin`. Defaults to OFF."""
    g.digitalWrite(gpio_addresses[pin][0], gpio_addresses[pin][1], state)

def digitalRead(pin):
    """Read ON or OFF from `pin`. Returns integer 0 or 1."""
    return g.digitalRead(gpio_addresses[pin][0], gpio_addresses[pin][1])
{% endhighlight %}

The downside of this approach is the complexity of my solution. It would have been much better to just rewrite mlinuxguy's library to hide the memory addresses and bit offsets, and require only the pin numbers and modes to function.
