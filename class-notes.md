---
layout: page
title: Notes
permalink: /notes/
---

This semester, I'm in a handful of math courses, and I thought I would rewrite and post my notes as a part of my studying process. This page will be a list of links to all my class notes.

<p>
    Differential Equations:
</p>
<ul>
{% for post in site.categories.diff %}
    <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>

<p>
    Finite Structures:
</p>

<ul>
{% for post in site.categories.finite %}
    <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>

<p>
    Linear Algebra:
</p>

<ul>
{% for post in site.categories.linear %}
    <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>

<p>
    Numerical Analysis:
</p>

<ul>
{% for post in site.categories.numerical %}
    <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>

<p>
    Probability and Statistics:
</p>

<ul>
{% for post in site.categories.stats %}
    <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>

<p>
    Miscellaneous:
</p>

<ul>
{% for post in site.categories.misc %}
    <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>
