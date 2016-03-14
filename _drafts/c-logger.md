---
layout: post
title: C Logger
---

I was working on a project recently, and found myself needing to log the output of a C executable when it ran. I found the following simple [logger]() and have modified it to fit my needs. In particular, I added the `%f` format specifier, and am planning on adding the rest once I get some time. I also added `__FUNCTION__` to the `LOG` macro so that in large projects you can have more information when you attempt to read the logs.
