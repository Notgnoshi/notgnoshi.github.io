---
layout: post
title: Listing outdated Python packages with Pip
meta: You can list outdated upgradeable Python packages using pip list --outdated
---

As of Pip version 1.3 you can check for package updates.

Here's how you list installed Python packages with Pip:

```
~ $ pip list -h

Usage:
  pip list [options]

Description:
  List installed packages, including editables.

  Packages are listed in a case-insensitive sorted order.

List Options:
  -o, --outdated     List outdated packages
  -u, --uptodate     List uptodate packages
  -e, --editable     List editable projects.
  -l, --local        If in a virtualenv that has global access, do not list globally-installed packages.
  --user             Only output packages installed in user-site.
  --pre              Include pre-release and development versions. By default, pip only finds stable versions.
...
```

This allows us to do

```
~ $ pip list --outdated
feedparser (5.1.3) - Latest: 5.2.1 [sdist]
html5lib (0.999) - Latest: 0.999999999 [sdist]
httplib2 (0.9.1) - Latest: 0.9.2 [sdist]
```

We can ask for confirmation and update everything with

```
~ $ pip list --outdated | awk '{print $1}' | xargs -n1 -p sudo -H pip install --upgrade
```

Or if you feel especially brave

```
~ $ pip list --outdated | awk '{print $1}' | xargs -n1 sudo -H pip install --upgrade
```
