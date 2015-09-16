---
layout: post
title: Taking a Look at Pointers
---

<link rel="stylesheet" href="{{ "/assets/styles/pointers.css" | prepend: site.baseurl }}">

I took a C++ class a long time ago. It wasn't as in-depth as my computer science this semester, but it covered far more material. One of the things that my instructor touched on was the concept of pointers. When I say touched on, I mean that she gave us an extremely brief explanation and then expected us to use them on our assigned programs as if we had mastered them. Ever since them I've had a large distaste for pointers, and every time someone mentions them I internally groan.

My purpose here will be to give an introduction to pointers in C++ to people with a working knowledge of C++. I don't intend to cover everything pointers have to offer, and I'm not pretending to be an expert. My intent is to provide a beginner's level introduction to pointers.

First off is a reminder about variables, memory, and their values. Memory holds values in a list of memory locations. There are a lot of memory spots, so each one has an address the CPU uses to lookup the values in the memory locations. Each memory slot holds a value, and each slot has an address. Additionally, we can name the values in memory so that we can meaningfully work with them. That's what variables are.

Instructors often represent computer memory like so:

<div class="mem_array">
    <table>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </table>
</div>

With each box representing a memory location, and whatever is inside being the value stored at that location. Each location has an address, so let's label our boxes with them.

<div class="mem_array">
    <table>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </table>
</div>

What are those funny looking numbers? Well, they're hexadecimal numbers which are in base 16. We don't really need to know how they work for right now, so I'm going to pretty much ignore them. In computer science we tend to represent hexadecimal numbers with `0x` as the first two digits. These two digits mean nothing more than "Hey, what follows me is in base 16." In this post, and as a rule of thumb, hex numbers are used to refer to memory locations. In this post, that will be the only thing they are used for.
