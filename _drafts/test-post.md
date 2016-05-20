---
layout: post
title: Test Post
---
<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

<!-- Custom styles for the truth tables -->
<link rel="stylesheet" href="{{ "/assets/styles/truth_tables.css" | prepend: site.baseurl }}">


<img class="centered" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/False_position_method.svg/351px-False_position_method.svg.png" alt="false position">


<!-- Custom styles for the truth tables -->
<link rel="stylesheet" href="{{ "/assets/styles/truth_tables.css" | prepend: site.baseurl }}">

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
