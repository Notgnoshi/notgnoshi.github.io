---
layout: post
title: Exploring Linear Transformations with Python
meta: Animating linear transformations using matplotlib and numpy in a Jupyter Notebook.
---

Every undergraduate math student knows that matrices are *linear transformations.* That's all well and good, but what is a transformation, and what does it mean for one to be linear?

Essentially, a transformation is a function $$T$$ that takes in stuff and transforms it into new stuff

<img class="centered" src="{{ "/assets/posts/linear-transformations/transformation.svg" | prepend: site.baseurl }}" alt="A mock transformation">

More specifically, a transformation $$T$$ is a function $$T : X \to X$$. That is, it's a function that maps a set onto itself. For example, when you multiply a matrix by a vector, you get another vector.

$$A \vec x = \vec b$$

Here's an example. Note that in Python, the `@` operator means matrix multiplication, where the `*` operator means elementwise (Hadamard) product.

```python
In [1]: import numpy as np
In [2]: A = np.matrix([[2, -1], [1, 1]])
In [3]: v = np.array([3, 4])  # A row vector
In [4]: A @ v.T  # we right multiply by column vectors
Out[4]:
matrix([[2],
        [7]])
In [5]: v @ A  # we left multiply by row vectors
Out[5]:
matrix([[10,  1]])
```

Now what about a *linear* transformation? In a word, a linear transformation $$L : W \to V$$, where $$W$$ and $$V$$ are vector spaces, is a transformation that preserves the vector space operations of addition and scalar multiplications. If you want more theory than that, go pick up a linear algebra textbook. It'll explain things quite a bit better than I can.

Otherwise, a good way to think about linear transformations is that things that started parallel end up parallel, and things that started perpendicular end up perpendicular. These are harder to visualize in higher dimensions, but here we'll be sticking with 2D.

There are several different kinds of 2D linear transformations that we can describe using matrices.

* Shear transformations
    <img class="centered-real" src="{{ "/assets/posts/linear-transformations/shear.svg" | prepend: site.baseurl }}" alt="A shear transformation">

* Scale transformations
    <img class="centered-real" src="{{ "/assets/posts/linear-transformations/scale.svg" | prepend: site.baseurl }}" alt="A scale transformation">

* Reflection transformations
    <img class="centered-real" src="{{ "/assets/posts/linear-transformations/reflection.svg" | prepend: site.baseurl }}" alt="A reflection transformation">

* Projection transformations
    <img class="centered-real" src="{{ "/assets/posts/linear-transformations/projection.svg" | prepend: site.baseurl }}" alt="A projection transformation">

* Rotation transformations
    <img class="centered-real" src="{{ "/assets/posts/linear-transformations/rotation.svg" | prepend: site.baseurl }}" alt="A rotation transformation">
* And others!

Each of these transformations can be fully represented as a matrix. Further, every (square) matrix encodes a linear transformation. Interestingly, if you want to apply two transformations, you can multiply the transformation matrices, and the result will be the same as applying one transformation and then the other. Note that this process is *not* commutative.

---

While the above pictures are nice, I wanted to animate the transformation to get a more intuitive feel for how they work. My Python code to do so is heavily influenced by [@dododas](https://github.com/dododas)'s work [here](https://dododas.github.io/linear-algebra-with-python/posts/16-12-29-2d-transformations.html).

Here's a function to animate a transformation:

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation, rc

# Display matplotlib animations as HTML5 videos in a Jupyter Notebook
rc('animation', html='html5')

def animate_transform(A, grid=None, num_steps=50, repeat=False):
    """
        Animates the effect a transform has on a given grid.
        If no grid is given, one will be generated.

        You can expect a small delay while the function generates the animation.
    """
    def colorizer(x, y):
        """Map x-y coordinates to a unique rgb color"""
        r = min(1, 1 - y/3)
        g = min(1, 1 + y/3)
        b = 1/4 + x/16
        return r, g, b

    def stepwise_transform(A, grid, num_steps):
        """
            Returns a list of transformed grids,
            stepping slowly from the given `grid` to
            the grid `A @ grid`.
        """
        # create empty array of the right size
        transgrid = np.zeros((num_steps + 1, ) + np.shape(grid))
        # compute intermediate transforms
        for i in range(num_steps + 1):
            intermediate = np.eye(2) + i / num_steps * (A - np.eye(2))
            # apply intermediate matrix transformation
            transgrid[i] = intermediate @ grid
        return transgrid

    if grid is None:
        # Create a grid of points in x-y space
        xvals = np.linspace(-4, 4, 9)
        yvals = np.linspace(-3, 3, 7)
        grid = np.column_stack([[x, y] for x in xvals for y in yvals])

    # Map grid coordinates to colors. Done only for xygrid, not all grids.
    colors = list(map(colorizer, grid[0], grid[1]))
    intermediate_transforms = stepwise_transform(A, grid, num_steps)
    fig = plt.figure(figsize=(6, 6))

    xmin = min(min(grid[0]), min(intermediate_transforms[-1][0]))
    xmax = max(max(grid[0]), max(intermediate_transforms[-1][0]))
    ymin = min(min(grid[1]), min(intermediate_transforms[-1][1]))
    ymax = max(max(grid[1]), max(intermediate_transforms[-1][1]))

    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
    scatter = ax.scatter([], [], c=colors)
    # Prevent `%matplotlib inline` from displaying the above scatter plot.
    plt.close()

    def update(i):
        """Draws the ith intermediate transform"""
        scatter.set_offsets(intermediate_transforms[i].T)
        return scatter,

    return animation.FuncAnimation(fig,
                                   update,
                                   interval=50,
                                   frames=num_steps,
                                   blit=True,
                                   repeat=repeat)
```

Note that this code is meant to be ran in a Jupyter Notebook.

---

Here are some examples.

* A [shear](https://en.wikipedia.org/wiki/Shear_matrix) transform:

    ```python
    A = np.column_stack([[1, 0], [2, 1]])
    anim = animate_transform(A, repeat=True)
    anim.save('shear.mp4')
    anim
    ```

    <video class="centered" autoplay loop>
        <source src="{{ "/assets/posts/linear-transformations/shear.mp4" | prepend: site.baseurl }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>

* A [projection](https://en.wikipedia.org/wiki/Projection_(linear_algebra)) onto the $$x$$ axis:

    ```python
    A = np.column_stack([[1, 0], [0, 0]])
    anim = animate_transform(A, repeat=True)
    anim.save('projection.mp4')
    anim
    ```

    <video class="centered" autoplay loop>
        <source src="{{ "/assets/posts/linear-transformations/projection.mp4" | prepend: site.baseurl }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
* A [rotation](https://en.wikipedia.org/wiki/Rotation_matrix) by $$\frac{\pi}{6}$$ radians:

    A rotation matrix $$A$$, that rotates space by $$\theta$$ radians is given by

    $$A = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$$

    ```python
    theta = np.pi / 6 # 30 degree clockwise rotation
    A = np.column_stack([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    anim = animate_transform(A, repeat=True)
    anim.save('rotation.mp4')
    anim
    ```

    <video class="centered" autoplay loop>
        <source src="{{ "/assets/posts/linear-transformations/rotation.mp4" | prepend: site.baseurl }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
* A [permutation](https://en.wikipedia.org/wiki/Permutation_matrix) matrix:
    ```python
    A = np.column_stack([[0, 1], [1, 0]])
    anim = animate_transform(A, repeat=True)
    anim.save('permutation.mp4')
    anim
    ```

    <video class="centered" autoplay loop>
        <source src="{{ "/assets/posts/linear-transformations/permutation.mp4" | prepend: site.baseurl }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>

    Note that this is different than a matrix transpose. Interestingly, you cannot represent the transpose as a matrix multiplication.

* A [scale](https://en.wikipedia.org/wiki/Scaling_(geometry)) matrix:
    ```python
    A = np.column_stack([[2, 0], [0, 5]])
    anim = animate_transform(A, repeat=True)
    anim.save('scale.mp4')
    anim
    ```

    <video class="centered" autoplay loop>
        <source src="{{ "/assets/posts/linear-transformations/scale.mp4" | prepend: site.baseurl }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>

---

Now we can visualize combining different transformations!

```python
theta = np.pi / 6 # 30 degree clockwise rotation
A = np.column_stack([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
B = np.column_stack([[2, 0], [0, 1]])  # A scale by 2 units in the x direction
anim = animate_transform(A @ B, repeat=True)
anim.save('combination.mp4')
anim
```

<video class="centered" autoplay loop>
    <source src="{{ "/assets/posts/linear-transformations/combination.mp4" | prepend: site.baseurl }}" type="video/mp4">
    Your browser does not support the video tag.
</video>

---

The notebook all of this is taken from can be found [here]({{ "/assets/posts/linear-transformations/linear-transformations.ipynb" | prepend: site.baseurl }})
