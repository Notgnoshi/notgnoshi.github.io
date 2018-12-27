---
layout: post
title: LaTeX, SVG, and Jupyter Notebooks
meta: A rant in ill-taste on my struggle to convert Jupyter notebooks containing SVG images to a PDF
---

This post is a (revised) copy of a frustrated email sent at 1:05 in the morning to the course TA, and good friend of mine. I was mistakenly working on a homework assignment on the day it was due.

I use Jupyter notebooks for mathematical and scientific programming because they rock. They're especially handy for course homework that requires PDF submissions, because you can convert them to a *large* number of other formats, like HTML, ReStructured Text, PDF, LaTeX, etc.

One of the nice things about Jupyter notebooks is that you can specify that Matplotlib should generate higher quality SVG vector images rather than a PNG. This is especially important when exporting to a PDF, because using raster images looks *terrible*. Add the following to your notebook

```python
%config InlineBackend.figure_format = 'svg'
%matplotlib inline
```

The results are especially remarkable when joined with [seaborn](https://seaborn.pydata.org/)

```python
# Apparently, SNS stands for "Samuel Norman Seaborn", a fictional character from The West Wing
import seaborn as sns

sns.set()
```

Once I got my homework to a happy place about 4 hours before the appointed time, I tried to convert it to a PDF only to find that Jupyter fails to handle SVG images properly. Now, before you ask, I've used the same process for previous homeworks, in which I have even used SVG images.

I convert to LaTeX before compiling to a PDF so I can do important things like add my name and a titlepage to the assignment, and fix a few stylistic things that drive me nuts.

```shell
jupyter nbconvert --to latex hw3.ipynb
jupyter nbconvert --to latex hw3.ipynb --debug
jupyter nbconvert --to latex hw3.ipynb --debug --ExtractOutputPreprocessor.enabled=True
jupyter nbconvert --to latex hw3.ipynb --debug --ExtractOutputPreprocessor.enabled=False
```

Crap, it crashes, stating that it cannot convert a `bytes` object to JSON... After digging a little deeper in the Output Preprocessor, it looks like it's failing to recognize that SVG images are indeed images. Weird. I'm doing nothing I've never done before, but I remembered that I had updated Jupyter a few days ago, so I go check to see if I can still successfully convert previous homeworks to LaTeX.

```shell
cd ..
jupyter nbconvert --to latex hw2/hw2.ipynb
jupyter nbconvert --to latex hw1/hw1.ipynb
```

Both worked perfectly, and *both contain SVG images!* So clearly it's the conversion to LaTeX that's broken. But there are other things I can convert to, so I tried ReStructured Text.

```shell
jupyter nbconvert --to rst hw3/hw3.ipynb
```

Awesome, that worked. Maybe I can use Pandoc to convert from ReStructured Text back to LaTeX? But that'll require converting the SVGs to PDFs. No problem, that's something I've done plenty of times before. Often enough I almost remembered the `find` incantation required to recursively convert SVGs to PDFs. Almost.

```shell
cd hw3_files/
find . -name '*.svg' -type f -exec bash -c 'convert "$0" "${0%.svg}.pdf"' {} \;
```

Shit. It works on SVGs created by my previous homeworks, but not this one... So naturally, that's not a problem with the SVG files, it's a problem with the SVG converter.

```shell
sudo apt install librsvg2-bin
find . -name '*.svg' -type f -exec bash -c 'rsvg-convert -f pdf -o "${0%.svg}.pdf" "$0"' {} \;
pandoc hw3.rst -o hw3.tex
```

Well kneel me down and shoot me in the back of the head. It worked. Let's replace the SVGs images in the LaTeX source with PDFs and try to compile! What could go wrong!?

```shell
sed -i '/\\includegraphics/{s/\.svg/\.pdf/g}' hw3.tex
latexmk -pdf -shell-escape hw3.tex
man pandoc
```

Well, it turns out that's a bust. Pandoc actually sucks at syntax highlighting (I didn't try very hard), and left out half the document!!

The next thing I notice is that `nbconvert` apparently has a dependency on a GTK module?! Now, why in the flipping hell would a document conversion utility depend on a module from a GUI toolkit? Beats me.

```shell
jupyter nbconvert --stdout --to latex hw3/hw3.ipynb
sudo apt install libcanberra-gtk-module
jupyter nbconvert --stdout --to latex hw3/hw3.ipynb
```

That fixed the warning messages, but it still failed to convert the notebook to LaTeX, so that's nice. The next thing to futilely try is the `nbconvert` help page. It turns out there's two of them, and neither are helpful, contrary to their names.

```shell
jupyter nbconvert --help
jupyter nbconvert --help-all
```

So I settled on a solution. Sort of.

I can export as ReStructured Text with the SVG outputs. This saves each of the Matplotlib outputs as SVG images. I can successfully export as LaTeX with PNG outputs. So all I should need to do is convert the exported SVG images to PDFs, do a batch rename (newer versions of Nautilus have a fantastic batch renaming utility, by the way), and then replace all `*.png` in the LaTeX source with `*.pdf`.

At this point I should have known better than to ask what could go wrong.

```shell
# Run all cells with SVG turned on
jupyter nbconvert --to rst hw3.ipynb
# Run all cells with PNGs turned on
jupyter nbconvert --to latex hw3.ipynb
find hw3-rst/ -name '*.svg' -type f -exec bash -c 'rsvg-convert -f pdf -o "${0%.svg}.pdf" "$0"' {} \;
cp *.pdf hw3-tex
# There's one hand made SVG to convert
sed -i '/\\includegraphics/{s/\.svg/\.pdf/g}' hw3.tex
# Also convert all the automagically included PNGs
sed -i '/\\includegraphics/{s/\.png/\.pdf/g}' hw3.tex
```

But exporting to RST and LaTeX apparently saves the SVG and PNG images with different filenames! Oh well, it's only about 10 files to rename by hand.

```shell
latexmk -pdf hw3.tex
```

But when I attempt to compile, `latexmk` tells me the LaTeX source code is erroneous. Apparently `nbconvert` is smart enough to syntax highlight Python source code, but somehow isn't aware you're not supposed to put an `align*` environment inside of math mode?!

So I fix that by hand and try again.

```shell
cd hw3-tex
vim hw3.tex
latexmk -pdf hw3.tex
```

What do you think happened next? If you guessed a successful compilation, you'd be horribly horribly wrong. It turns out, `nbconvert` doesn't use `\includegraphics` when including a PNG, but does for every other image format? So my awesome use of `sed` a little while ago was entirely unfounded.

```shell
sed -i 's/\.png/\.pdf/g' hw3.tex
latexmk -pdf hw3.tex
```

Boom. Halle-frickin-lujah. It compiled. What's more, all the images are in their correct place, and are high quality vector graphics. Except one.

One of my original troubleshooting steps was to comment out things in the markdown cells of the Jupyter notebook and do a rudimentary bisective search to try to figure out what exactly was going wrong. Well, I forgot to uncomment one of the images. So I had to repeat the whole process again.

Export as RST, export as LaTeX. Convert SVGs to PDFs. Use `sed` to replace `.png` and `.svg` (both, because one of the images was created by hand and saved as SVG) with `.pdf`. Fix the `align*` in math mode. Batch rename the PDF files to match the PNG filenames by hand again. Recompile.

Then I realized that one of my troubleshooting steps was to disable the LaTeX [template](https://github.com/t-makaro/nb_pdf_template) I like to use. So rinse and repeat.

---

After going through this entire process, I found a way to get Jupyter to save the matplotlib plots as PDFs after about 2 minutes of Duck-Duck-Going, which only made me angrier.

```python
# %config InlineBackend.figure_format = 'svg'
%config InlineBackend.figure_format = 'pdf'
%matplotlib inline

# Apparently, SNS stands for "Samuel Norman Seaborn", a fictional character from The West Wing
import seaborn as sns

sns.set()
```

It's not optimal, because it uses `PDF.js` to render the PDFs in an iframe in the web client, which can slow it down and cause scrolling issues, but it *does* work flawlessly to generate a PDF of your notebook.
