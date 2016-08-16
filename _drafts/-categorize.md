---
layout: post
title: Class Notes
date: 2015-4-31
---

As a part of my studying process, I'm going to be rewriting all of my [notes](/notes/) this semester in a bit more of a rigorous manner than I normally would. I think this will help me learn much better, and if I'm going to rewrite them (using $$\LaTeX$$) I might as well post them.

The hard part was figuring out how to best organize them. I wanted a page with a list of all my class notes, organized by class. To do this, I thought about several options, but after browsing through the Jekyll [Documentation](https://jekyllrb.com/docs/home/) the only thing I tried was setting post categories.

First things first, how do you make a page with a permalink up in the navigation bar? Well, this is actually pretty simple. I created a page `class-notes.md` in the root directory and added `permalink: /notes/` to the page's front-matter.

Next, how do you make a list of posts within a specific category? The first thing you do is add `categories: [category_1, category_2, etc]` to a post's front-matter.

Then you loop through all posts in a specific category like so:

```html
<ul>
    {% raw %}{% for post in site.categories.notes %}
        <li>
            <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </li>
    {% endfor %}{% endraw %}
</ul>
```

The hard part comes after I decided that the list of posts on the front page should not list the notes as if they were regular blog posts. I may change my mind on this, but for now I think I'll leave it the way it is.

The hardest part was figuring out how to list posts that were not a part of the `notes` category. If each post only had one category this would have been easier. If a post has one category, the front matter looks like `category: notes`, but if there are multiple, as mentioned above it's `categories: [category_1, category_2]`.

Then I had to find a way to find a syntax for `for post not in category:notes`. This was tricky, but the way to do it when your posts have multiple categories is `{% raw %}{% unless post.categories contains "notes" %}{% endraw %}`. There's probably another better way to do it, but after many repeated attempts I'm just glad I got it working.

The second problem was that this filtering broke the post limit I had set on the main page. Originally, I would just loop over the first 8 posts, but looping over 8 posts and only listing those not in a specific category isn't what I wanted. This caused issues. Liquid does not natively support math expressions with integer variables. After much Googling, I found a neglected forum post that had `{% raw %}{% assign i = i | plus: 1 %}{% endraw %}` to increment `i` by 1. After I found that, it was a simple matter to add an `if` statement to limit posts on the front page to 8.

Now what if I make a note post that I want to post be on the main page? I just added another `if` statement that checks if the post's categories contains `post`. What about if a post contains the `post` category but not `notes`? There's a better solution, but I just moved the `unless` block inside the else condition.

Here's the end result of much Googling and keyboard smashing.

```html
<ul class="posts">
    {% raw %}{% assign i = 0 %}
    {% for post in site.posts %}
        {% if post.categories contains "post" %}
            {% assign i = i | plus: 1 %}
            <li>
                <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
                <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
            </li>
        {% else %}
            {% unless post.categories contains "notes" %}
                {% assign i = i | plus: 1 %}
                <li>
                    <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
                    <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
                </li>
            {% endunless %}
        {% endif %}
        {% if i > 7 %}
            {% break %}
        {% endif %}
    {% endfor %}{% endraw %}
</ul>
```
