# -*- coding: utf-8 -*-
"""
This file provides useful utilities to be used in the report generation process.
"""
from reportlab.pdfgen import canvas, textobject

def read_text(filename, c, x, y, fontz, leading):
    
    my_text=c.beginText()
    my_text.setTextOrigin(x, y)
    my_text.setFont(c._fontname, fontz, leading)
    
    my_file=open(filename)
    for line in my_file:
        my_text.textLine(line.rstrip())
    my_file.close()
    
    return my_text
