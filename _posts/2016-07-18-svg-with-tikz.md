---
layout: post
title: Producing SVG images with Tikz
---
<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

It's a fairly simple process as long as you're using Linux. This process requires `pdflatex` and [`pdf2svg`](https://github.com/dawbarton/pdf2svg), installable with `sudo apt install pdf2svg`.

First, make a Tikz image:

{% highlight latex %}
{% raw %}
\documentclass[tikz]{standalone}

\newcommand{\tikzAngleOfLine}{\tikz@AngleOfLine}
    \def\tikz@AngleOfLine(#1)(#2)#3{%
        \pgfmathanglebetweenpoints{%
        \pgfpointanchor{#1}{center}}{%
        \pgfpointanchor{#2}{center}}
    \pgfmathsetmacro{#3}{\pgfmathresult}%
    }

\newcommand{\tikzMarkAngle}[3]{
    \tikzAngleOfLine#1#2{\AngleStart}
    \tikzAngleOfLine#1#3{\AngleEnd}
    \draw #1+(\AngleStart:0.4cm) arc (\AngleStart:\AngleEnd:0.4cm);
}

\begin{document}
    \begin{tikzpicture}
        \coordinate (O) at (0, 0);
        \coordinate (z) at (3, 3);
        \coordinate (a) at (3, 0);

        \draw [->, thick] (-1, 0) -- (5, 0);
        \draw [->, thick] (0, -1) -- (0, 5);

        \draw (O) -- (z);
        \draw (O) -- (z) node[midway, label=above:$r$]{};
        \draw (a) -- (z) node[midway, label=right:$a$]{};
        \draw (O) -- (a) node[midway, label=below:$b$]{};

        \draw (z) node[circle, fill, inner sep=1pt, label=right:$z$]{};
        \draw (O) node[label={[xshift=-0.3cm, yshift=-0.7cm]$O$}]{};
        \draw (O) node[label={[xshift=0.55cm, yshift=-0.15cm]$\phi$}]{};

        \tikzMarkAngle{(O)}{(z)}{(a)}
    \end{tikzpicture}
\end{document}
{% endraw %}
{% endhighlight %}

Then compile it with `pdflatex polar.tex`. Then convert the PDF to SVG with `pdf2svg polar.pdf polar.svg`.

The above code produces the following SVG image:

<img class="centered-full" src="{{ "/assets/posts/geometry/polar/polar.svg" | prepend: site.baseurl }}" alt="polar coordinates">
