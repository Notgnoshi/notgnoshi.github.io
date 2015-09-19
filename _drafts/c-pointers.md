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
            <td>'s'</td>
            <td>'t'</td>
            <td>'u'</td>
            <td>'f'</td>
            <td>'f'</td>
            <td>' '</td>
            <td>'h'</td>
            <td>'e'</td>
            <td>'r'</td>
            <td>'e'</td>
            <td>' '</td>
            <td>' '</td>
        </tr>
        <tr>
            <td>0x0001</td>
            <td>0x0002</td>
            <td>0x0003</td>
            <td>0x0004</td>
            <td>0x0005</td>
            <td>0x0006</td>
            <td>0x0007</td>
            <td>0x0008</td>
            <td>0x0009</td>
            <td>0x000A</td>
            <td>0x000B</td>
            <td>0x000C</td>
        </tr>
    </table>
</div>

What are those funny looking numbers? Well, they're hexadecimal numbers which are in base 16. We don't really need to know how they work for right now, so I'm going to pretty much ignore them. In computer science we tend to represent hexadecimal numbers with `0x` as the first two digits. These two digits mean nothing more than "Hey, what follows me is in base 16." In this post, and as a rule of thumb, hex numbers are used to refer to memory locations. In this post, that will be the only thing they are used for. We refer to these locations as memory addresses.

These addresses refer to locations which hold values. Each memory location can hold exactly one of what are called integral data types.

Let's create an integer variable `x`, and give it a value of `13`. Our variable will have an address, because it will change every time we run our code I'll just pick a random address `0xF04D`.

``` cpp
    int x = 13;
```

When we want to access the address of a variable, we use the `&` operator, called the *dereferencing* operator. The following will output `13` and then `0xF04D` to the console.

``` cpp
    cout << x << endl;
    cout << &x << endl;
```

When we have an address and want to do something to the value that exists at that address, we use the `*` operator. So if I say `*&x += 1`, I add `1` to the value that exists at the address of the variable `x`, which happens to be `13`.

Let's use this idea to create a *pointer* that points to `x`'s address.

``` cpp
    int* ptr_to_x = &x;
```

Let's talk this through, because I got lost once my instructors started throwing `*`'s and `&`'s at me. `ptr_to_x` is a variable that has a value of `x`'s address. `ptr_to_x` has an address too, but let's not worry about that so much. I'll give you a small memory diagram below to help you make sense of this.

<div class="mem_array">
    <table>
        <tr>
            <td class="bold">Variable</td>
            <td>x</td>
            <td>ptr_to_x</td>
        </tr>
        <tr>
            <td class="bold">Value</td>
            <td>13</td>
            <td>0xF04D</td>
        </tr>
        <tr>
            <td class="bold">Address</td>
            <td>0xF04D</td>
            <td>0xF2E9</td>
        </tr>
    </table>
</div>

We can use `*ptr_to_x` in place of `x` anywhere in our code. The two represent the same thing. If we change `*ptr_to_x`, `x` will change, because `ptr_to_x` points to the address of `x`!

That's really all there is to understand about pointers. There are a ton of cool things we can do with this. We can have pointers to pointers to pointers to variables. Arrays are actually pointers (so we can actually use `[i]` type syntax with pointers, but what's the point?). We can pass pointers to functions. We can pass variable addresses to functions.

In C/C++ you can't return an array from a function, but you *can* return a *pointer* to an array.
