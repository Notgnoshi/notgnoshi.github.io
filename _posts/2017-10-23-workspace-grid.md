---
layout: post
title: I Want My 2x2 Workspaces Back!
subtitle: My constant opposition to change
meta: A short explanation of how to install and configure the workspace-grid Gnome Shell Extension for Ubuntu 17.10
---

I installed Ubuntu 17.10 yesterday, which has abandoned Unity in favor of Gnome. So far it has been a smooth transition. However, one of the things I really liked about Unity over other desktop managers was the workspaces. It just clicked with my existing mental model of how to use software.

I am a very visual person, and get lost very quickly if I cannot think about the physical layout of a piece of software, algorithm, or mathematical idea.

You'll probably want to skip my random musings and get on the [solution](#installing-workspace-grid) I found for getting 2x2 workspaces back in Ubuntu 17.10.

---

## My Mental Model

Here are some random musings on how I've found myself using workspaces. Note that my personal preferences are heavily skewed because I've used Unity the longest, and naturally find its solution to be the best.

### One big layered workspace

Before using Linux, my mental model of my computer workspace was that of layered applications, where each application's depth was defined by when it was last used.

<img class="centered-real" src="{{ "/assets/posts/workspace-grid/layered-workspace.svg" | prepend: site.baseurl }}" alt="A layered workspace">

Before using Unity, this was all I had known. If I had a large number of applications open, Alt-Tabbing between them became harder and harder as I struggled to form a visual picture in my mind of where things were.

### Horizontal workspaces

I was very hesitant to try Gnome at first, so I spent some time test driving different window managers before the big release. One of the window managers I tried was Budgie, which offered four workspaces laid out horizontally

<img class="centered-full" src="{{ "/assets/posts/workspace-grid/horizontal-workspace.svg" | prepend: site.baseurl }}" alt="A horizontal workspace">

However, I found myself replicating one giant layered workspace with high priority applications on the left and low priority applications on the right. Instead of Alt-Tabbing between applications, I find myself switching workspaces to get from one application (rated by some measure of importance) to the next. I'm going to call this an *antipattern* because of personal preference, but not because I have any objective reason to say one method of use is any better than another.

I think (and I have no evidence to back me up) that this linear use pattern is because humans naturally devolve into ranking things by some metric when given some method of laying things out in a linear fashion.

Another factor that contributed to this (that I didn't care enough to try to fix) was that if you pressed `ctrl+alt+T` to open a terminal in another workspace in Budgie, it would open another session *in whatever workspace an existing terminal session was open in*.

<img class="centered-full" src="{{ "/assets/posts/workspace-grid/horizontally-layered-workspace.svg" | prepend: site.baseurl }}" alt="A horizontally layered workspace">

### Vertical workspaces

I've used Gnome before, and found its vertical workspaces interesting (I have other opinions too, but they're not relevant here), but still essentially the same idea as the horizontally layered workspace. Again, every time I've used the workspaces, I've found myself using each workspace for one application, and sorting them vertically by importance.

<img class="centered-real" src="{{ "/assets/posts/workspace-grid/vertical-workspace.svg" | prepend: site.baseurl }}" alt="A vertical workspace">

Gnome is different however, in that the workspaces are dynamic. This means that closing the last application in a workspace between two others gets rid of the workspace.

<img class="centered" src="{{ "/assets/posts/workspace-grid/vertical-workspace-removal.svg" | prepend: site.baseurl }}" alt="The removal of a vertical workspace">

I've found this frustrating and counterintuitive, especially when compared to the trusty 2x2 grid Unity provided. Now, don't get me wrong, there is a setting in `gnome-tweak-tool` to change from a dynamic number of workspaces to a static number. However, the dynamic nature of the vertical workspaces is not my primary complaint. My biggest complaint is that I confuse myself because I haven't trained my brain to think about the layout of my applications in a line.

I've taught myself to think about switching to an application as a motion in 2-space, which inherently has a horizontal *and* a vertical dimension. If I do this, I can rely on my sense of geography to keep my overall confusion to a handleable level.

### The 2x2 workspace

Oddly enough, I do not find myself using the 2x2 workspaces with this antipattern of one giant workspace with four layers. I think my applications not being laid out in a linear fashion may prevent this. Instead, I tend to use each workspace to group applications together by use.

<img class="centered" src="{{ "/assets/posts/workspace-grid/2x2-workspace.svg" | prepend: site.baseurl }}" alt="A 2x2 workspace">

I often have multiple browser windows open, sometimes one window full of Stack Overflow posts alongside a text editor full of bugs. Other times (like now) I'll have a $$\LaTeX$$ IDE open in one workspace, along with any relevant file browsers and terminal sessions, an editor and browser showing a live preview of this post in another, and in a third workspace I'll have several terminal sessions open.

Over the years, I've trained my brain to think of the upper left workspace (and right monitor if I have more than one) as a text editor and documentation browser, while almost all forays into terminal land occur in the lower left workspace. If I'm working on some frustrating project that nearly everyone but me could do in their sleep and I happen to need a 2 hour Half Life 2 break (which in hindsight is probably why I find simple things so difficult), that happens in a dedicated right hand workspace. Any music players, long running terminal processes, or non project related browser windows get placed in the remaining right hand workspace.

<img class="centered-real" src="{{ "/assets/posts/workspace-grid/2x2-workspace-use.svg" | prepend: site.baseurl }}" alt="My use of a 2x2 workspace">

### Final musings

I'm sure nearly all of the problems I've mentioned so far could be fixed by some obscure (to me) setting or plugin, and I'm even more sure they wouldn't be problems if I used a tiling window manager. Mostly because I'd have a whole new set of problems, but that's neither here nor there.

I also want to be clear that these are baseless opinions that I've formed simply because I'm too stubborn to try new (possibly better, but probably much "worse") things.

I think the takeaway, if there is one, is that I've trained my brain to associate different tasks with different locations, even if they're virtual. I'm sure I could do the same thing with a vertical or horizontal workspace layout if I had enough time. Instead however, writing ill-formed blog posts for people I've never met to disagree with is apparently a better solution.

---

## Installing Workspace Grid

[Workspace Grid](https://extensions.gnome.org/extension/484/workspace-grid/) is a Gnome extension to replace the vertical workspaces with a configurable grid. See [here](https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome/Installation) for instructions on how to install Gnome extensions from the Gnome website. Otherwise, there are manual ways to install extensions that you can read about [here](https://mytechnicalthoughts.wordpress.com/2013/04/14/how-to-manually-install-a-gnome-shell-extension/). The one thing it's missing is a live preview of each workspace in the switcher as indicated by [this](https://github.com/zakkak/workspace-grid/issues/4) GitHub issue.

Note that the new version of `gnome-tweak-tool` for Ubuntu 17.10 does not allow you to install extensions from a `.zip` file any more.

---

Finally, I'd be very interested to see a proper analysis of different workspaces and how they tend to be used. But unfortunately I'm simply not willing to do so myself.
