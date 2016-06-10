---
layout: post
title: "Flashing system LEDs"
subtitle: "A tutorial on /sys/class/leds/"
---

This last semester I was tasked with finding a GPIO solution for an Odroid XU. It didn't turn out to be very difficult, but it so happens to be easier than I thought. While I was looking into using `/sys/class/gpio/` to work with GPIO pins on a Linux machine, I found that Linux users have control of a few of their system LEDs by manipulating `/sys/class/leds/`.

First thing's first, here's how `/sys/class/leds/` is laid out:

```
leds
├── device1:color:led
│   ├── brightness
│   ├── device
│   ├── max_brightness
│   ├── power
│   ├── subsystem
│   ├── trigger
│   └── uevent
└── device2:color:led
    ├── brightness
    ├── device
    ├── max_brightness
    ├── power
    ├── subsystem
    ├── trigger
    └── uevent
```

I was working with my `input16::numlock` LED, you may have a variety of others to choose from.

Of the files in the `input16::numlock` directory, the ones of interest are the `trigger`, `max_brightness`, and `brightness`. The brightest possible setting is an integer found in `max_brightness`. Makes sense, right? My LEDs have two possible states `1` (on) or `0` (off), but others could have a range from `0` to `255`. The current brightness of your LED is shown in `brightness`. Changing this value should change the brightness of your LED. The interesting file here is `triggers`. This is a list of possible events that trigger an LED status change. For my numlock LED, the default trigger (indicated by brackets around the entry) was `kbd_numlock`.


{% highlight bash %}
14:48 nots@abyss /sys/class/leds/input16::numlock$ cat trigger

none kbd-scrollock [kbd-numlock] kbd-capslock kbd-kanalock kbd-shiftlock
kbd-altgrlock kbd-ctrllock kbd-altlock kbd-shiftllock kbd-shiftrlock kbd-ctrlllock
kbd-ctrlrlock usb-gadget usb-host cpu0 cpu1 cpu2 cpu3 cpu4 cpu5 cpu6 cpu7 rfkill0
phy0rx phy0tx phy0assoc phy0radio
{% endhighlight %}

You can change this value to `none` for manual control by issuing `echo none > triggers`. Note that this must be done by the root user, and that Linux handles overwriting the `triggers` file with a single entry gracefully. You can verify your change by viewing the contents of your trigger file afterwards.

{% highlight bash %}
14:53 nots@abyss /sys/class/leds/input16::numlock$ cat trigger

[none] kbd-scrollock kbd-numlock kbd-capslock kbd-kanalock kbd-shiftlock
kbd-altgrlock kbd-ctrllock kbd-altlock kbd-shiftllock kbd-shiftrlock kbd-ctrlllock
kbd-ctrlrlock usb-gadget usb-host cpu0 cpu1 cpu2 cpu3 cpu4 cpu5 cpu6 cpu7 rfkill0
phy0rx phy0tx phy0assoc phy0radio
{% endhighlight %}

After setting the trigger to `none`, you can manually change the `brightness` to update your LED state by issuing `echo 1 > brightness`

Here's a simple script to blink the LED every second.

{% highlight bash %}
#!/bin/bash

cd /sys/class/leds/input16::numlock

echo none > trigger

while true
do
    echo 1 > brightness
    sleep 1
    echo 0 > brightness
    sleep 1
done
{% endhighlight %}

The script will have to be run as root. You can give it executable permissions by issuing `sudo chmod +x led.sh`. Then you can run it simply by `sudo ./led.sh`.
