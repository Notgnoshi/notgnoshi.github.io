---
layout: post
title: I Want My 2x2 Workspaces Back!
subtitle: My Constant Opposition to Change
meta: A short explanation of how to install and configure the workspace-grid Gnome Shell Extension for Ubuntu 17.10
---

I installed Ubuntu 17.10 yesterday, which has abandoned Unity in favor of Gnome. So far it has been a smooth transition. However, one of the things I really liked about Unity over other desktop managers was the workspaces. It just clicked with my existing mental model of how to use software.

I am a very visual person, and get lost very quickly if I cannot think about the physical layout of a piece of software, algorithm, or mathematical idea.

## My Mental Model

### One big layered workspace

Before using Linux, my mental model of my computer workspace was that of layered applications, where each application's depth was defined by when it was last used.

<img class="centered" src="{{ "/assets/posts/workspace-grid/layered-workspace.svg" | prepend: site.baseurl }}" alt="A layered workspace">

Before using Unity, this was all I had known. If I had a large number of applications open, Alt-Tabbing between them became harder and harder as I struggled to form a visual picture in my mind of where things were.

### Horizontal workspaces

I was very hesitant to try Gnome at first, so I spent some time test driving different window managers before the big release. One of the window managers I tried was Budgie, which offered four workspaces laid out horizontally

<img class="centered-full" src="{{ "/assets/posts/workspace-grid/horizontal-workspace.svg" | prepend: site.baseurl }}" alt="A horizontal workspace">

However, I found myself replicating one giant layered workspace with high priority applications on the left and low priority applications on the right. Instead of Alt-Tabbing between applications, I find myself switching workspaces to get from one application to the next.

<img class="centered-full" src="{{ "/assets/posts/workspace-grid/horizontally-layered-workspace.svg" | prepend: site.baseurl }}" alt="A horizontally layered workspace">

### Vertical workspaces

I've used Gnome before, and found its vertical workspaces interesting, but still essentially the same idea as the horizontally layered workspace. Again, every time I've used the workspaces, I've found myself using each workspace for one application, and sorting them vertically by importance.

<img class="centered-full" src="{{ "/assets/posts/workspace-grid/vertical-workspace.svg" | prepend: site.baseurl }}" alt="A vertical workspace">

Gnome is different however, in that the workspaces are dynamic. This means that closing the last application in a workspace between two others gets rid of the workspace.

<img class="centered-full" src="{{ "/assets/posts/workspace-grid/vertical-workspace-removal.svg" | prepend: site.baseurl }}" alt="The removal of a vertical workspace">

I've found this frustrating when compared to the trusty 2x2 grid Unity provided.

### The 2x2 workspace

Oddly enough, I do not find myself using the 2x2 workspaces as one giant workspace with four layers. Instead, I tend to

## Installing `workspace-grid`
