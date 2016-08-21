---
layout: page
permalink: /test/
meta: This is a test page for Jekyll, Liquid, GitHub Pages, or any web-based technology I care to try.
---

This is a test page. Go away.

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

<!-- Custom styles for the truth tables -->
<link rel="stylesheet" href="{{ "/assets/styles/truth_tables.css" | prepend: site.baseurl }}">

<!-- Custom styles for the binary_word -->
<link rel="stylesheet" href="{{ "/assets/styles/binary_word.css" | prepend: site.baseurl }}">


<img class="centered" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/False_position_method.svg/351px-False_position_method.svg.png" alt="false position">

<img class="centered-full" src="{{ "/assets/posts/floating-point-math/error.svg" | prepend: site.baseurl }}" alt="number line holes">

<hr>

<hr/>

<table class="truth">
    <tr>
        <td>$$p$$</td>
        <td>$$\neg p$$</td>
    </tr>
    <tr>
        <td>T</td>
        <td>F</td>
    </tr>
    <tr>
        <td>F</td>
        <td>T</td>
    </tr>
</table>

---

<table class="binary_word">
    <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>15</td>
        <td>14</td>
        <td>13</td>
        <td>12</td>
        <td>11</td>
        <td>10</td>
        <td>9</td>
        <td>8</td>
        <td>7</td>
        <td>6</td>
        <td>5</td>
        <td>4</td>
        <td>3</td>
        <td>2</td>
        <td>1</td>
        <td>0</td>
    </tr>
</table>

Test post. `categories: [post, other]`


```python
import this

def main():
    pass

if __name__ == '__main__':
    main()
```

![Clone URL]({{ "/assets/posts/gh-pages/clone-url.png" | prepend: site.baseurl }})

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

<!-- http://www.w3schools.com/colors/colors_names.asp -->
$$\color{cornflowerblue}{\sin x}$$

$$\cancelto{1}{\frac{\sin x}{x}}$$

$$\mathtip{\sin x}{\sin x \sim x \text{ for small }x}$$

$$\toggle{\sin x}{\cos x}{\tan x}\endtoggle$$
