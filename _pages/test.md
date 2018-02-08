---
layout: page
permalink: /test/
meta: This is a test page for Jekyll, Liquid, GitHub Pages, or any web-based technology I care to try.
---

This is a test page. Go away.

---

# Fonts, font sizes, and header sizes

Regular. *Italic* **bold** ***bold italic*** `mono` *`mono italic`* **`mono bold`**

# H1
normal text
## H2
normal text
### H3
normal text
#### H4
normal text

---

# Image classes

Markdown

![Clone URL]({{ "/assets/posts/floating-point-math/error.svg"  | prepend: site.baseurl }})

Centered-full:

<img class="centered-full" src="{{ "/assets/posts/floating-point-math/error.svg" | prepend: site.baseurl }}" alt="number line holes">

Centered:

<img class="centered" src="{{ "/assets/posts/floating-point-math/error.svg" | prepend: site.baseurl }}" alt="number line holes">

Centered-real:

<img class="centered-real" src="{{ "/assets/posts/floating-point-math/error.svg" | prepend: site.baseurl }}" alt="number line holes">

Centered-vertical

<img class="centered-vertical" src="{{ "/assets/posts/why-jailbreak/gauss-settings.png"  | prepend: site.baseurl }}" alt="Gauss Settings"/>


```python
import this

def main():
    pass

if __name__ == '__main__':
    main()
```


```python
{% raw %}{% highlight python %}
import this

def main():
    pass

if __name__ == '__main__':
    main()
{% endhighlight %}{% endraw %}
```

$$ \begin{cases} x_1 + x_2 + x_3 + x_4 + x_5 = 1 \\ x_3 + x_4 + 2x_5 = 0 \\ x_5 = 3\end{cases}$$

$$ \left(\begin{array}{ccccc|c} 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{array}\right) $$

$$\begin{cases}a_{11} x_1 + a_{12} x_2 + \dots + a_{1n} x_n = b_1 \\ a_{21} x_1 + a_{22} x_2 + \dots + a_{2n} x_n = b_2 \\ \vdots \\ a_{m1} x_1 + a_{m2} x_2 +  \dots + a_{mn} x_n = b_m \end{cases}$$

<details>
    <summary>Spoiler</summary>
    <p>Everybody dies.</p>
</details>

Including file snippets:

```liquid
{% raw %}{% highlight python %}
{% include snippets/levenshtein.py %}
{% endhighlight %}{% endraw %}
```

with `levenshtein.py` in `/_includes/snippets/` gives the following:

```python
{% include snippets/levenshtein.py %}
```

$$\cancel{x}$$

$$\enclose{circle}[mathcolor="red"]{\color{black}{x}}$$

<!-- https://www.w3schools.com/colors/colors_names.asp -->

$$\color{cornflowerblue}{\sin x}$$

$$\cancelto{1}{\frac{\sin x}{x}}$$

$$\mathtip{\sin x}{\sin x \sim x \text{ for small }x}$$

$$\toggle{\sin x}{\cos x}{\tan x}\endtoggle$$
