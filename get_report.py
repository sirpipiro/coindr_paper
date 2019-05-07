# -*- coding: utf-8 -*-
"""
This is a template program for generating a research report for a quantitative 
trading strategy. The backtest of the factors and trading strategies are based 
on zipline in Python. The report generation relies on reportlab.
"""
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame
from utils_for_report import get_intro_textframe

intro_file='C:\\Users\\leo_s\\Documents\\Git Projects\\trading_strats\\inputs\\strat_intro.txt'
intro_frame=Frame(100, 640, 420, 150, showBoundary=0)

my_canvas=canvas.Canvas('C:\\Users\\leo_s\\Documents\\Git Projects\\trading_strats\\paper.pdf')
my_canvas.drawString(100, 800, '1.Strategy Introduction')
intro_frame.addFromList([get_intro_textframe(intro_file)], my_canvas)
my_canvas.showPage
my_canvas.save()