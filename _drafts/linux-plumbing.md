---
layout: post
title: Linux Plumbing
subtitle: A summary of piping
meta: A summary of file redirection, piping, tee, sponge, /dev/null, stdin, stdout, stderr, and linux plumbing in deneral
---

* Suppressing `stderr` while piping:

  `~ $ command 2>/dev/null | command`
* `tee`
* `sponge`
