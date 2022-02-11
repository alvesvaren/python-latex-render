from . import render_to_file
import argparse

parser = argparse.ArgumentParser(description="Process some integers.")

parser.add_argument("latex", type=str, help="LaTeX code to render")
parser.add_argument("--output", "-o", type=str, help="Output file")
parser.add_argument("--font-size", "-s", type=int, default=24, help="Font size")
parser.add_argument("--color", "-c", type=str, default="black", help="Color")
parser.add_argument("--border", "-b", type=int, default=8, help="Border")

args = parser.parse_args()

render_to_file(args.latex, args.output, args.font_size, args.color, args.border)
