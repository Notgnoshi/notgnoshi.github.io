---
layout: post
title: Why I dislike Windows
meta: A list of subjective personal opinions as to why Windows sucks
redirect_to: https://agill.xyz/blog/why-i-dislike-windows
---

I dumped Windows a few years ago and I couldn't be happier. Every time it comes up in conversation however, I have a difficult time explaining why my hatred for Windows is justified. That's what I wanted to do here.

* **Installing software sucks.**

  There are no package managers; you have to browse to the software's web page and manually download and run the installer, all the while hoping that the website you're downloading from is the official site. Even if it is the official site, there's an upsetting trend of packaging suggested software/web browser toolbars with the installer.

  It's worth noting that even with Linux, your experience might vary. Some distributions have extensive repositories, but others might be out of date.

  It's just as difficult to update software, or even to be notified of available updates. Often, a software "update" installs a completely different version of whatever software you're using without removing to outdated version! Even if an updater *does* attempt to remove a previous version, it never does so completely.

* **When you purchase a Windows machine, there's a high likelihood that it comes with preinstalled garbage that's completely unnecessary and extraordinarily difficult to remove.**

  I don't understand this phenomenon; it doesn't make sense to me that someone somewhere thought "Hey, wouldn't it be cool if we forced hours of pain on our users while they try to uninstall an inordinate amount of crap before they can use our computers?"

* **"Windows Rot"**

  It's almost never possible to completely and fully uninstall software from a Windows machine. No matter what, it always leaves behind thousands of configuration files, `.dll`s, app data, and registry entries.

* **The Windows Registry**

  [Here's](https://rwmj.wordpress.com/2010/02/18/why-the-windows-registry-sucks-technically/) a technical explanation as to why the Registry sucks.

* **Windows is huge**

  A fresh install of Windows can be as large as 8-9 GB, and the `C://Windows` directory seems to grow at an astonishing rate.

  Updates are consequently huge as well. This makes it extremely difficult to download updates and/or fresh installs of Windows, *especially on rural internet connections*.

* **Windows doesn't care about other OS's installed on your hard drive**

  Windows always [overwrites the MBR](https://www.google.com/search?q=windows+overwrites+MBR) and will always set a newly installed version of Windows as the default operating system.

* **Windows 10 update practices**

  Microsoft has interpreted a click on the `X` icon (you know, the one we use to *exit* programs) of the Windows 10 update notification *as approval to initiate the Windows 10 update*. This is a common practice of *malware* installers, and is a **huge** breach of trust. Furthermore, Microsoft has begun to *automatically* update machines to Windows 10 without user approval. This is just as large of a breach of trust. Personally, this is all the reason I need to never use Windows again. When I use a computer, it's with the expectation that *I'm* the one in control of how I use my data. Microsoft is not omniscient (though they keep trying) and does **not** know what's best for me.

* **Windows 10 privacy practices**

  Microsoft's [EULA](https://www.microsoft.com/en-us/servicesagreement/), section 2, "Your Content", grants *"Microsoft a worldwide and royalty-free intellectual property license to use Your Content, for example, to make copies of, retain, transmit, reformat, display, and distribute"*

* **You have no real control over *crucial features* of Windows 10**

  - Windows 10 forces some updates, and [some](https://www.google.com/search?q=KB3081424+fail) of them have failed catastrophically.
  - You cannot access Safe Mode unless *you've already booted into the OS* which **defeats the entire purpose** of Safe Mode. Additionally, Safe Mode is difficult to access, requiring multiple steps and dialogs versus a single `F8` key press on every Windows version prior.
  - It's extremely difficult to disable Cortana.
  - Windows 10 violates basic networking principles. It ignores host files, DNS protocol, firewall rules, and sends telemetry data regardless of your settings.

* **Visual Studio 2015 Update 2 C++ compiler has been [caught](https://www.infoq.com/news/2016/06/visual-cpp-telemetry) injecting telemetry code into both Debug and Release binaries**

* **Software development sucks on Windows machines**

  Sure, Visual Studio is awesome... most of the time. But that's not what I mean. I mean the process of installing a language, libraries, and tools, is extremely lacking. Additionally, even using these things can be painful. My experience installing, learning, and using Python on Windows was what convinced me to switch. After using some of the features of Linux that make software development easier, I knew that the pain I had suffered using Windows was in vain.

* **Windows does not offer the extreme amounts of control that a Linux-based OS offers**

  This one goes without saying.

---

These are mostly personal opinions, and I openly admit to a strong pro-Linux bias. I'm sure that a devoted Microsoft follower could find reasons to ignore or refute each of the listed reasons here, but they're reasons enough for me to despise Windows.

I'm also willing to admit that no operating system, and no community of users is perfect.

One of the largest reasons using Linux isn't always viable is that there is software that is *only* available on Windows or OSX that because of school or business requirements *must* be used. There are many software packages on Windows that do not have an open-sourced alternative, and many that do are not as powerful, or lack necessary features.
