---
layout: post
title: Class Notes
categories: [notes, misc]
---

As a part of my studying process, I'm going to be rewriting all of my [notes](/notes/) this semester in a bit more of a rigorous manner than I normally would. I think this will help me learn much better, and if I'm going to rewrite them (using $$\LaTeX$$) I might as well post them.

The hard part was figuring out how to best organize them. I wanted a page with a list of all my class notes, organized by class. To do this, I thought about several options, but after browsing through the Jekyll [Documentation](https://jekyllrb.com/docs/home/) the only thing I tried was setting post categories.

First things first, how do you make a page with a permalink up in the navigation bar? Well, this is actually pretty simple. I created a page `class-notes.md` in the root directory and added `permalink: /notes/` to the page's front-matter.

Next, how do you make a list of posts within a specific category? The first thing you do is add `categories: [category_1, category_2, etc]` to a post's front-matter.

Then you loop through all posts in a specific category like so:

{% highlight html %}
<ul>
    {% raw %}{% for post in site.categories.notes %}
        <li>
            <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </li>
    {% endfor %}{% endraw %}
</ul>
{% endhighlight %}
