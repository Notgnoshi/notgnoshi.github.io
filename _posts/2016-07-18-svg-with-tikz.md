---
layout: post
title: Producing SVG images with Tikz
---
<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

It's a fairly simple process, if you're using Linux. This process requires `pdflatex` and [`pdf2svg`](https://github.com/dawbarton/pdf2svg), installable with `sudo apt install pdf2svg`.

First, make a Tikz image:

{% highlight latex %}
\documentclass[tikz]{standalone}
\usetikzlibrary{patterns, decorations.pathreplacing}

\begin{document}
    \begin{tikzpicture}[scale=1]
        \draw (-8, 0) -- (-1, 0);
        \draw (-8, -0.5) -- (-8, 0.5) node[black, below, yshift=-1.1cm]{$ -9.9 \times 10^9$};
        \draw (-1, -0.5) -- (-1, 0.5) node[black, below, yshift=-1.1cm, xshift=-0.5cm]{$ -1.0 \times 10^{-9}$};

        \draw (1, 0) -- (8, 0);
        \draw (1, -0.5) -- (1, 0.5) node[black, below, yshift=-1.1cm, xshift=0.5cm]{$ 1.0 \times 10^{-9}$};
        \draw (8, -0.5) -- (8, 0.5) node[black, below, yshift=-1.1cm]{$ 9.9 \times 10^9$};

        \draw[
            very thick,
            decorate,
            decoration={
                brace,
                amplitude=8pt
            }
        ] (-1, 0.6) -- (1, 0.6) node[midway, yshift=0.6cm]{Underflow};

        \draw[
            very thick,
            decorate,
            decoration={
                brace,
                amplitude=8pt
            }
        ] (-10, 0.6) -- (-8, 0.6) node[midway, yshift=0.6cm]{Overflow};

        \draw[
            very thick,
            decorate,
            decoration={
                brace,
                amplitude=8pt
            }
        ] (8, 0.6) -- (10, 0.6) node[midway, yshift=0.6cm]{Overflow};

    \end{tikzpicture}
\end{document}
{% endhighlight %}

Then compile it with `pdflatex error.tex`. Then convert the PDF to SVG with `pdf2svg error.pdf error.svg`.

The above code produces the following SVG image:

<img class="centered-full" src="{{ "/assets/posts/floating-point-math/error.svg" | prepend: site.baseurl }}" alt="number line holes">

Feel free to zoom in as much as you'd like to enjoy the vector graphics!
