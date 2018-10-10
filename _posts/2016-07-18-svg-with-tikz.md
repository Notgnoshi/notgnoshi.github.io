---
layout: post
title: Producing SVG images with Tikz
meta: A tutorial on producing vector graphics from a Tikz LaTeX image.
---

It's a fairly simple process as long as you're using Linux. This process requires `pdflatex` and [`pdf2svg`](https://github.com/dawbarton/pdf2svg), installable with `sudo apt install pdf2svg`.

First, make a Tikz image:

```latex {% raw %}
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
        \draw (O) -- (z) node[above, midway]{$r$};
        \draw (a) -- (z) node[right, midway]{$a$};
        \draw (O) -- (a) node[below, midway]{$b$};

        \draw (z) node[circle, fill, inner sep=1pt]{} node[right]{$z$};
        \draw (O) node[left, yshift=-0.25cm]{$O$};
        \draw (O) node[xshift=0.55cm, yshift=0.2cm]{$\phi$};

        \tikzMarkAngle{(O)}{(a)}{(z)}
    \end{tikzpicture}
\end{document}
{% endraw %}```

Then compile it with `pdflatex polar.tex`. Then convert the PDF to SVG with `pdf2svg polar.pdf polar.svg`.

The above code produces the following SVG image:

<img class="centered-full" src="{{ "/assets/posts/geometry/polar/polar.svg" | prepend: site.baseurl }}" alt="polar coordinates">

If you compile with the `-shell-escape` flag, you can tell $$\LaTeX$$ to compile both a PDF file and an SVG image as so:

```latex {% raw %}
\documentclass[tikz, convert={outext=.svg, command=\unexpanded{pdf2svg \infile\space\outfile}}, multi=false]{standalone}

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
        \draw (O) -- (z) node[above, midway]{$r$};
        \draw (a) -- (z) node[right, midway]{$a$};
        \draw (O) -- (a) node[below, midway]{$b$};

        \draw (z) node[circle, fill, inner sep=1pt]{} node[right]{$z$};
        \draw (O) node[left, yshift=-0.25cm]{$O$};
        \draw (O) node[xshift=0.55cm, yshift=0.2cm]{$\phi$};

        \tikzMarkAngle{(O)}{(a)}{(z)}
    \end{tikzpicture}
\end{document}
{% endraw %}```

If you need to do this more often, you can create a `standalone.cfg` file in the same directory with this inside:

```latex
% Local standalone.cfg file
\input{standalone/standalone.cfg}% Load main standalone.cfg file
\standaloneconfig{convert={outext=.svg, command={pdf2svg \infile\space\outfile}}}
```

And then use `\documentclass[tikz]{standalone}` for your `documentclass` just like the first example.
