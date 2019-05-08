# -*- coding: utf-8 -*-
"""
This is a template program for generating a research report for a quantitative 
trading strategy. The backtest of the factors and trading strategies are based 
on zipline in Python. The report generation relies on reportlab.
"""
from reportlab.pdfgen import canvas, textobject
from reportlab.lib.pagesizes import A4 #595.27, 841.89
from utils_for_report import read_text

"""
Define format specifications of the report.
"""
x0=100
y0=50
w0=400 #Default width of text blocks
h0=20 #Space between lines
temp=0 #Starting point for multi-line texts
fontz_title=20
fontz_body=12

intro_file='/home/hao/Documents/trading_strats/inputs/strat_intro.txt'

#my_canvas=canvas.Canvas('C:\\Users\\leo_s\\Documents\\Git Projects\\trading_strats\\paper.pdf')
my_canvas=canvas.Canvas('/home/hao/Documents/trading_strats/paper.pdf', pagesize=A4, bottomup=0)
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, '1. Strategy Introduction')
my_canvas.drawText(read_text(intro_file, my_canvas, x0, y0+50, fontz_body, h0))
my_canvas.showPage
my_canvas.save()