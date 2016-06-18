---
layout: post
title: Test Post
author: Me
meta: Meta-info
subtitle: to test things
---
<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

<!-- Custom styles for the truth tables -->
<link rel="stylesheet" href="{{ "/assets/styles/truth_tables.css" | prepend: site.baseurl }}">

<!-- Custom styles for the binary_word -->
<link rel="stylesheet" href="{{ "/assets/styles/binary_word.css" | prepend: site.baseurl }}">


<img class="centered" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/False_position_method.svg/351px-False_position_method.svg.png" alt="false position">
<img class="centered-full" src="{{ "/assets/floating-point-math/roundoff-error.png" | prepend: site.baseurl }}" alt="number line holes">

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


{% highlight python %}
import this

def main():
    pass

if __name__ == '__main__':
    main()
{% endhighlight %}

![Clone URL]({{ "/assets/clone-url.png" | prepend: site.baseurl }})

{% highlight python %}
{% raw %}{% highlight python %}
import this

def main():
    pass

if __name__ == '__main__':
    main()
{% endhighlight %}{% endraw %}
{% endhighlight %}
