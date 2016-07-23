---
layout: post
title: C/C++ Preprocessor Macros
meta: Useful preprocessor macros
---

A few days ago, I came across a nifty little [Gist](https://gist.github.com/aras-p/6224951) of things to commit just before leaving your job. As you can imagine, most of the things listed are pretty devious. Some of them caught my eye, particularly  `#define true ((__LINE__&15)!=15)`.

Here's a small list of the more useful macros that I found.

* `__DATE__` is the date the executable was compiled on.
* `__TIME__` is the compilation time.
* `__FILE__` is the file name.
* `__FUNCTION__` will only work inside a function, and gives the name of the current function.
* `__FUNCSIG__` Gives the current function signature. For example, in `main()` the function signature is `int __cdecl main(int,int *[])`.
* `__COUNTER__` Is a counter (haha, clever) that starts at 0, and increments every time it's used.
* `__LINE__` Is the line number of the line on which it's used.

Also, you can use `#line n` to set the very next line number to `n` and the next to `n + 1`, and so on.

Other useful macros might include

* `#define SHOW(X) cout << # X " = " << (X) << endl`, useful for debugging.
* For simplified logging, we can do
  {% highlight c %}
#define LOG(log)                                            \
if (!log.enabled()) {}                                      \
else log.getStream() << __FILE__ << "@" << __LINE__ << ": "

log_t errorlog;
...

LOG(errorlog) << "This doesn't look good:" << somedata;
  {% endhighlight %}

There are many, many more use cases. If you're interested, look [here](http://jhnet.co.uk/articles/cpp_magic) for some more magic.

I recently had to write a logger for a project I'm involved with, and I found `#define LOG(...) log_print(__FILE__, __LINE__, __FUNCTION__, __VA_ARGS__ )` inside. It's a bit more complicated than the macros above, but much more awesome. With an appropriate `log_print` function defined, you can simply `#define printf LOG` when you want to log `printf` statements in C/C++. I'll have to write up a post on it sometime in the near future.
