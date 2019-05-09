# -*- coding: utf-8 -*-
"""
This is a template program for generating a research report for a quantitative 
trading strategy. The backtest of the factors and trading strategies are based 
on zipline in Python. The report generation relies on reportlab.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import A4 #595.27, 841.89

"""
Define format specifications of the report.
"""
x0=100
y0=800
w0=400 #Default width of text blocks
h0=20 #Space between lines

fontz_title=20
fontz_body=12

intro_file='/home/hao/Documents/trading_strats/inputs/strat_intro.txt'
factor_return_image='/home/hao/Documents/trading_strats/inputs/factor_returns_plot.jpg'
factor_return_comment='/home/hao/Documents/trading_strats/inputs/factor_returns_comment.txt'
return_image_1='./inputs/return_chart_1.jpg'
return_image_2='/home/hao/Documents/trading_strats/inputs/return_chart_2.jpg'
return_image_3='/home/hao/Documents/trading_strats/inputs/return_chart_3.jpg'


def drawBodyText(filename, canvas_to_draw, x, y, w, h):
    
    my_file=open(filename)
    my_text=my_file.read()
    my_file.close()
    
    temp=20
    temp_text=simpleSplit(my_text, canvas_to_draw._fontname, canvas_to_draw._fontsize, w)
    
    for line in temp_text:
        if line=='v':
            canvas_to_draw.drawString(x, y-h-temp, '')
        else:
            canvas_to_draw.drawString(x, y-h-temp, line)
        temp+=h0
    
    return

#my_canvas=canvas.Canvas('C:\\Users\\leo_s\\Documents\\Git Projects\\trading_strats\\paper.pdf')
my_canvas=canvas.Canvas('/home/hao/Documents/trading_strats/paper.pdf', pagesize=A4)

# Page One
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, '1. Strategy Introduction')
my_canvas.drawString(x0, y0-360, '2. Factor Return')

my_canvas.setFontSize(fontz_body, leading=h0)
drawBodyText(intro_file, my_canvas, x0, y0, w0, h0)
drawBodyText(factor_return_comment, my_canvas, x0, y0-570, w0, h0)

my_canvas.drawImage(factor_return_image, x0, y0-640-h0, width=300, preserveAspectRatio=True, anchor='l')
my_canvas.showPage()

# Page Two
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, '3. Factor Return Analysis')

my_canvas.setFontSize(fontz_body, leading=h0)
my_canvas.drawString(x0, y0-30-h0, 'Mean Period Return by Factor Quantile')
my_canvas.drawString(x0, y0-270-h0, 'Factor Weighted L/S Portfolio Return')
my_canvas.drawString(x0, y0-510-h0, 'Cumulative Return by Factor Quantile')

my_canvas.drawImage(return_image_1, x0, y0-240-h0, width=400, height=200)
my_canvas.drawImage(return_image_2, x0, y0-480-h0, width=400, height=200)
my_canvas.drawImage(return_image_3, x0, y0-720-h0, width=400, height=200)
my_canvas.showPage()

my_canvas.save()