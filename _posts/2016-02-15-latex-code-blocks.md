---
layout: post
title: Syntax Highlighting with LaTeX
---

Here's the basics:

{% highlight latex %}
\documentclass[12pt]{article}

\usepackage{minted}

\begin{document}

\begin{minted}{matlab}
epsilon = 1;
while 1 + epsilon > 1
    epsilon = epsilon / 2;
end
epsilon = 2 * epsilon;

if epsilon == eps
    fprintf('Calculated and internally defined values of machine epsilon match\n');
end
\end{minted}

\end{document}
{% endhighlight %}

This will produce:

{% highlight matlab %}
epsilon = 1;
while 1 + epsilon > 1
    epsilon = epsilon / 2;
end
epsilon = 2 * epsilon;
if epsilon == eps
    fprintf('Calculated and internally defined values of machine epsilon match\n');
end
{% endhighlight %}

This requires [`minted.sty`](https://github.com/gpoore/minted/blob/master/source/minted.sty) to be in the same directory as the `.tex` document, and it also requires Python Pygments to be installed with `pip install pygments`. Additionally, for Minted to be able to access Pygments, it needs to be ran with the `-shell-escape` flag. In [Texmaker](http://www.xm1math.net/texmaker/), you can add this flag in `Options > Configure Texmaker > PdfLaTeX`. On my Windows install of Texmaker, my PdfLaTeX commandline options are `pdflatex -shell-escape -synctex=1 -interaction=nonstopmode %.tex`. This also works on Ubuntu as far as I know.

In other news, Sublime Text 3 is awesome.