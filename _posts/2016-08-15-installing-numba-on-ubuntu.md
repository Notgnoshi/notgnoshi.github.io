---
layout: post
title: Installing Numba on Ubuntu
meta: A brief description of how to install Numba 0.27.0 on Ubuntu 16.04
---

There are several ways to speed up your Python code, and using Numba's Just-In-Time (JIT) compilation is one of the easiest. However, it can be a pain to install Numba.

Briefly, here's how I installed Numba 0.27.0 on Ubuntu 26.04 LTS for Python 3.

```shell
 $ sudo apt install llvm-3.7 libedit-dev
 $ sudo -H LLVM_CONFIG=/usr/bin/llvm-config-3.7 pip3 install llvmlite numba
```

Note that `llvm-3.7` is *not* the latest version. `llvmlite` fails to install when using `llvm-3.8` (the latest `llvm` version as of right now). We also have to set the `LLVM_CONFIG` environment variable for `pip` to successfully install `llvmlite`.

This was all I had to do to install Numba, but if this doesn't work for you, take a look at [this](http://stackoverflow.com/a/28922702) Stack Overflow post for help. Numba's [GitHub](https://github.com/numba/numba) repository states that its dependencies are:

* `llvmlite`
* `numpy` (1.7+)
* `funcsigs` (Python 2)

We can check that Numba successfully installed like so

```python
In  [1]: import numba
In  [2]: numba.__version__
Out [2]: '0.27.0'
```

Even though there are tons of customizations, basic usage is quite simple:

```python
from numba import jit
import numpy as np

@jit
def sum2d(arr):
    m, n = arr.shape
    result = 0.0
    for i in range(m):
        for j in range(n):
            result += arr[i, j]
    return result

def main():
    matrix = np.arange(25).reshape(5, 5)
    print(sum2d(matrix))

if __name__ == '__main__':
    main()
```

Read the Numba [Docs](http://numba.pydata.org/numba-doc/latest/index.html) for details.
