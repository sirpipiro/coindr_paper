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
fontz_disclaimer=8

intro_file='./inputs/strat_intro.txt'
factor_return_image='./inputs/factor_returns_plot.jpg'
factor_return_comment='./inputs/factor_returns_comment.txt'
return_image_1='./inputs/return_chart_1.jpg'
return_image_2='./inputs/return_chart_2.jpg'
return_image_3='./inputs/return_chart_3.jpg'
ic_image_1='./inputs/ic_chart_1.jpg'
ic_image_2='./inputs/ic_chart_2.jpg'
ic_image_3='./inputs/ic_chart_3.jpg'
turn_image_1='./inputs/turn_chart_1.jpg'
turn_image_2='./inputs/turn_chart_2.jpg'
turn_image_3='./inputs/turn_chart_3.jpg'
conclusion_file='./inputs/strat_conclusion.txt'
disclaimer_file='./inputs/disclaimer.txt'

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
my_canvas=canvas.Canvas('./paper.pdf', pagesize=A4)

# Cover


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

# Page Three
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, '4. Information Coefficient Analysis')

my_canvas.setFontSize(fontz_body, leading=h0)
my_canvas.drawString(x0, y0-30-h0, 'Forward Return IC')
my_canvas.drawString(x0, y0-270-h0, 'Historical IC Distribution')
my_canvas.drawString(x0, y0-510-h0, 'IC Heatmap by Month')

my_canvas.drawImage(ic_image_1, x0, y0-240-h0, width=400, height=200)
my_canvas.drawImage(ic_image_2, x0, y0-480-h0, width=400, height=200)
my_canvas.drawImage(ic_image_3, x0, y0-720-h0, width=400, height=200)
my_canvas.showPage()

# Page Four
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, '5. Turnover Analysis')

my_canvas.setFontSize(fontz_body, leading=h0)
my_canvas.drawString(x0, y0-30-h0, 'Mean Turnover by Factor Quantile')
my_canvas.drawString(x0, y0-270-h0, 'Top vs Bottom Quantile Turnover')
my_canvas.drawString(x0, y0-510-h0, 'Factor Rank Autocorrelation')

my_canvas.drawImage(turn_image_1, x0, y0-240-h0, width=400, height=200)
my_canvas.drawImage(turn_image_2, x0, y0-480-h0, width=400, height=200)
my_canvas.drawImage(turn_image_3, x0, y0-720-h0, width=400, height=200)
my_canvas.showPage()

# Page Five
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, '6. Conclusion')

my_canvas.setFontSize(fontz_body, leading=h0)
drawBodyText(conclusion_file, my_canvas, x0, y0, w0, h0)
my_canvas.showPage()

# Disclaimer
my_canvas.setFontSize(fontz_title, leading=h0)
my_canvas.drawString(x0, y0, 'Disclaimer')

my_canvas.setFontSize(fontz_disclaimer, leading=h0)
drawBodyText(disclaimer_file, my_canvas, x0, y0, w0, h0)
my_canvas.showPage()

my_canvas.save()