---
layout: post
title: Drawing Logic Gates with Tikz
meta: A basic tutorial on drawing digital circuit diagrams with Tikz
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

Tikz is an extremely powerful tool, but it can be hard to get a grasp of. Here's a few examples of drawing digital circuit diagrams using the `shapes.gates.logic` Tikz library. Each of these examples uses the <a href="{{ "/assets/posts/drawing-logic-gates-with-tikz/standalone.cfg" | prepend: site.baseurl }}">`standalone.cfg`</a> file introduced in [this]({% post_url 2016-07-18-svg-with-tikz %}) post.

### Basic gates and wiring

<!-- symlink to /assets/posts/drawing-logic-gates-with-tikz/ex1.tex -->
{% highlight latex %}
\documentclass[tikz, border=1mm]{standalone}

\usetikzlibrary{arrows, shapes.gates.logic.US, calc}

\begin{document}
\begin{tikzpicture}
    \node (x) at (0, 1) {$x$};
    \node (y) at (0, 0) {$y$};

    \node[not gate US, draw] at ($(x) + (0.8, 0)$) (notx) {};
    \node[not gate US, draw] at ($(y) + (0.8, 0)$) (noty) {};

    \draw (x) |- (notx.input);
    \draw (y) |- (noty.input);


    \node[or gate US, draw, rotate=0, logic gate inputs=nn] at ($(noty) + (1.5, 0.5)$) (xory) {};

    \draw (notx.output) -- ([xshift=0.2cm]notx.output) |- (xory.input 1);
    \draw (noty.output) -- ([xshift=0.2cm]noty.output) |- (xory.input 2);

    \draw (xory.output) -- node[above]{$\bar x + \bar y$} ($(xory) + (1.5, 0)$);
\end{tikzpicture}
\end{document}
{% endhighlight %}

which produces

<img class="centered-full" src="{{ "/assets/posts/drawing-logic-gates-with-tikz/ex1.svg" | prepend: site.baseurl }}" alt="not x or not y">

### More complicated wiring

{% highlight latex %}
\documentclass[tikz, border=1mm]{standalone}

\usetikzlibrary{arrows, shapes.gates.logic.US, calc}
\tikzstyle{branch}=[fill, shape=circle, minimum size=3pt, inner sep=0pt]

\begin{document}
\begin{tikzpicture}
    \node (x) at (0, 2) {$x$};
    \node (y) at (0, 1) {$y$};
    \node (z) at (0, 0) {$z$};

    \node[not gate US, draw] at ($(x) + (0.8, 0)$) (notx) {};
    \node[not gate US, draw] at ($(y) + (0.8, 0)$) (noty) {};

    \draw (x) |- (notx.input);
    \draw (y) |- (noty.input);

    \node[nor gate US, draw, rotate=0, logic gate inputs=nnnn] at ($(noty) + (2, 0.085)$) (xory) {};

    \path ($(notx.input) + (0.2, 0)$) -- coordinate (puntx) (x |- notx);
    \draw (x) |- (puntx) node[branch] {} |- ($(notx.output) + (0.4, 0.4)$) |- (xory.input 1);

    \draw (notx.output) -- ([xshift=0.2cm]notx.output) |- (xory.input 2);
    \draw (noty.output) -- ([xshift=0.2cm]noty.output) |- (xory.input 3);
    \draw (z) -| ($(noty.output) + (0.2, -0.5)$) |- (xory.input 4);

    \draw (xory.output) -- node[above]{$\overline{x + \bar x + \bar y + z}$} ($(xory) + (3, 0)$);
\end{tikzpicture}
\end{document}
{% endhighlight %}

which produces

<img class="centered-full" src="{{ "/assets/posts/drawing-logic-gates-with-tikz/ex2.svg" | prepend: site.baseurl }}" alt="useless circuit">

While not a very good circuit to diagram, it shows many of the capabilities of Tikz.

### Graphing functions

Just because it's useful and I have nowhere else to put it, here's how you graph functions with Tikz

{% highlight latex %}
\documentclass[tikz]{standalone}

\begin{document}
\begin{tikzpicture}
    % axes
    \draw[->](-3.5, 0) -- (4.2, 0) node[right] {$x$};
    \draw[->](0, -pi) -- (0, 4.2) node[above] {$y$};

    % graphs
    \draw[scale=0.5, domain=-3:3, smooth, variable=\x, blue]
        plot ({\x}, {\x*\x});
    \draw[domain=-pi:pi, smooth, variable=\x, red]
        plot ({\x}, {sin(deg(\x))});
\end{tikzpicture}
\end{document}
{% endhighlight %}

<img class="centered-full" src="{{ "/assets/posts/drawing-logic-gates-with-tikz/ex3.svg" | prepend: site.baseurl }}" alt="graphing functions">

Something more advanced:

{% highlight latex %}
\documentclass[tikz]{standalone}

\usepackage{pgfplots}
\usetikzlibrary{patterns}

\begin{document}
\begin{tikzpicture}
% diagonal fill pattern
\pgfdeclarepatternformonly{north east lines wide}%
   {\pgfqpoint{-1pt}{-1pt}}%
   {\pgfqpoint{10pt}{10pt}}%
   {\pgfqpoint{9pt}{9pt}}%
   {
        \pgfsetlinewidth{0.4pt}
        \pgfpathmoveto{\pgfqpoint{0pt}{0pt}}
        \pgfpathlineto{\pgfqpoint{9.1pt}{9.1pt}}
        \pgfusepath{stroke}
    }

    \begin{axis}[
        grid=major,
        axis lines=middle,
        xmin=-1.75,
        xmax=1.75,
        ymin=-9,
        ymax=2.5,
        width=14cm,
        height=8cm
    ]

    \addplot[color=red, domain=-1.6:1.6] {x^2 + 2*x - 7};

    \addplot+[
        mark=none,
        domain=-1:1,
        pattern=north east lines wide,
        pattern color=red!50!yellow
        ] {x^2 + 2*x - 7} \closedcycle;
    \end{axis}
\end{tikzpicture}
\end{document}
{% endhighlight %}

$$\int_{-1}^{1} (x^2 + 2x - 7) \mathrm{d}x$$

<img class="centered-full" src="{{ "/assets/posts/drawing-logic-gates-with-tikz/ex4.svg" | prepend: site.baseurl }}" alt="graphing functions">
