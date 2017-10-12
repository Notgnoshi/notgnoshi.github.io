---
layout: post
title: Automatically reloading imported libraries with IPython
meta: IPython has an autoreload extension to reload libraries automatically for faster prototyping and testing code.
---

IPython has an [autoreload](http://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) extension to reload imported modules before executing code. This can be very handy when prototyping and testing code.

* `%load_ext autoreload` - Load the `autoreload` IPython extension
* `%autoreload` - Reload all modules now
* `%autoreload 0` - Disable automatic reloading
* `%autoreload 1` - Reload all modules imported with `%aimport` automatically
* `%autoreload 2` - Reload all modules automatically
* `%aimport` - List modules to be automatically reloaded
* `%aimport foo, bar` - Import modules `foo` and `bar`, and mark them for autoreloading with `%autoreload 1`
* `%aimport -foo` - Mark module `foo` to *not* be automatically reloaded
