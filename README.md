# python-latex-render

This is a simple library and cli to render latex code to images.

It uses Pillow + KaTeX + Selenium + Chrome/Chromium (because it supports transparent screenshots) to open a website, render latex, take a screenshot and then save it

## Requirements:

-   The python packages listed in requirements.txt
-   Chrome or chromium installed

## Usage (CLI):

`python -m latex-render "x^2=\frac{2}{e}" -o filename.png -c "#abcdef"`
