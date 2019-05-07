# -*- coding: utf-8 -*-
"""
This file provides useful utilities to be used in the report generation process.
"""
from reportlab.platypus import Paragraph, KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet

def get_intro_textframe(filename):
    
    my_file=open(filename)
    my_text=my_file.read()
    my_file.close()
    
    styles=getSampleStyleSheet()
    my_text_in_frame=KeepInFrame(420, 150, [Paragraph(my_text, styles['BodyText'])])
    
    return my_text_in_frame
