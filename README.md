# python-latex-render

This is a simple library and cli to render latex code to images.

It uses Pillow + KaTeX + Selenium + Chrome/Chromium (because it supports transparent screenshots) to open a website, render latex, take a screenshot and then save it

## Requirements:

-   Chrome or chromium installed

## Installation:

Run `pip install git+https://github.com/alvesvaren/python-latex-render`

## Usage (CLI):

`python -m latex-render "x^2=\frac{2}{e}" -o filename.png -c "#abcdef"`
