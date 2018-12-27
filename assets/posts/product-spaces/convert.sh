#!/bin/bash

# Compile each Asymptote image to a PDF
asy ./*.asy

# Convert each PDF to SVG
for f in *.pdf; do
    pdf2svg "${f}" "${f%.pdf}.svg"
done
