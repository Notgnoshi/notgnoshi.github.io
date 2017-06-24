---
layout: post
title: Complex Derivatives
meta: A formulation of derivatives of complex-valued functions
---

$$\newcommand{\ddz}{\displaystyle \frac{d}{dz}}$$
$$\newcommand{\limdz}{\displaystyle \lim_{\Delta z \to 0}}$$
$$\newcommand{\limz}{\displaystyle \lim_{z \to z_0}}$$

**Defn.** Let $$f$$ be a function whose domain of definition contains a neighborhood $$N_\varepsilon (z_0)$$. The *derivative of $$f$$ at $$z_0$$* is the limit

$$f'(z_0) = \limz \frac{f(z) - f(z_0)}{z - z_0}$$

Or equivalently,

$$f'(z_0) = \limdz \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$

where $$\Delta z = z - z_0$$.

We call $$f$$ *differentiable at $$z_0$$* if $$f'(z_0)$$ exists.

---

We often drop the subscript on $$z_0$$ and write

$$\Delta w = f(z + \Delta z) - f(z)$$

which means the change in $$w = f(z)$$ corresponding to a change $$\Delta z$$ in $$z$$.

Then the limit is

$$f'(z) = \limdz \frac{\Delta w}{\Delta z}$$

We denote the derivative of a function $$f(z)$$ as

$$f'(z) = \frac{dw}{dz} = \ddz \Big(f(z)\Big)$$

depending on which is most convenient.

---

**Thm.** If the derivative of a function $$f$$ exists at a point $$z_0$$, then the function is continuous at $$z_0$$.

**Pf.** Let $$f'(z_0)$$ exist. Then,

$$\limz \Big[f(z) - f(z_0)\Big] = \limz \left[\frac{f(z) - f(z_0)}{z - z_0} \cdot (z - z_0)\right]$$

$$\limz\frac{f(z) - f(z_0)}{z - z_0} \cdot \limz z - z_0 = f'(z_0) \cdot 0 = 0$$

Which implies

$$\limz f(z) = f(z_0)$$

Or rather, that $$f$$ is continuous as $$z_0$$.

---

### Differentiation Rules

We have the following differentiation rules that we will derive to make differentiation of more complicated functions easier.

1. $$\ddz c = 0$$ for some complex constant $$c$$,
2. $$\ddz z = 1$$,
3. $$\ddz\big(c\cdot f(z)\big) = c \cdot f'(z)$$,
4. $$\ddz z^n = nz^{n-1}$$,
5. $$\ddz \Big[f(z) + g(z) \Big] = f'(z) + g'(z)$$,
6. $$\ddz\Big[f(z) \cdot g(z)\Big] = f'(z) \cdot g(z) + f(z) \cdot g'(z)$$,
7. $$\ddz \left[\frac{f(z)}{g(z)}\right] = \frac{g(z) \cdot f'(z) - f(z) \cdot g'(z)}{[g(z)]^2}$$, $$g(z) \neq 0$$,
8. $$\ddz\Big[(g \circ f)(z)\Big] = g'\big(f(z)\big) \cdot f'(z)$$, or rather, if $$w = f(z)$$ and $$W = g(w)$$, we have $$\displaystyle \frac{dW}{dz} = \frac{dW}{dw}\cdot\frac{dw}{dz}$$.

### Derivations

1. $$\ddz c = 0$$.

    $$\ddz c = \limdz \frac{\Delta w}{\Delta z} = \limdz \frac{f(z + \Delta z) - f(z)}{\Delta z} = \limdz \frac{c - c}{\Delta z} = 0$$.

2. $$\ddz z = 1$$.

    $$\ddz z = \limdz \frac{f(z + \Delta z) - f(z)}{\Delta z} = \limdz \frac{\cancel{z +} \Delta z \cancel{- z}}{\Delta z} = \limdz \frac{\Delta z}{\Delta z} = \limdz 1 = 1$$.

3. $$\ddz\big(c\cdot f(z)\big) = c \cdot f'(z)$$.

    $$\limdz \frac{c \cdot f(z + \Delta z) - c \cdot f(z)}{\Delta z} = \limdz c \cdot \frac{f(z + \Delta z) - f(z)}{\Delta z} = c \cdot \limdz\frac{f(z + \Delta z) - f(z)}{\Delta z} = c \cdot f'(z)$$.
