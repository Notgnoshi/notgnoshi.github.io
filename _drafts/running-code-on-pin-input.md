---
layout: post
title: Running C Executables on GPIO Input
---

So last [post]({% post_url 2016-02-09-odroid-gpio %}) I talked about turning GPIO pins on and off on an Odroid-XU. A few hours after I figured out how to do pin I/O, I found out that the only thing we needed it for was monitoring for a button press to start up the robot's autonomous functions. That started a whole new round of research and script iterations. This time was a lot easier though.

Here's the barebones of how you monitor for a button press. Note that there is no need for allowing other code to execute while this script is monitoring a pin because this is only a power button.

{% highlight python %}
#!/usr/bin/env python
import subprocess
import sys
from gpiolib import *

pinMode(pin, INPUT)

while True:
    if digitalRead(pin):
        # [1:] strips off `sudo ./run.py`
        output = subprocess.check_output(sys.argv[1:])
        sys_clean()
        sys.exit()
{% endhighlight %}

One thing to note is that `subprocess.check_output` *checks* the *output* of whatever subprocess it starts. This can be used to do stuff. For example, we write this information to a log file once the executable exits.

I thought about using the Python `logging` module, but it wasn't immediately obvious if I could log stuff from the C executable with it. Part of the reason we need to log this information is because we cannot connect over SSH while the robot is running (it's supposed to be autonomous).

Another thing that crossed my mind is that our script writes all the output to a log file all at once after the process quits. For large programs, it would be much more efficient to write this information out as the script receives it, but once again, for our purposes, this method works fine.

The last thing to mention is that because `run.py` has to be ran as root for pin I/O, the log files it writes are owned by the root user. It would be preferable if they were not.
