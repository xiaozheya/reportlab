# -*- coding: utf-8 -*-
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))
pdfmetrics.registerFont(TTFont('msyhbd', 'msyhbd.ttc'))
from reportlab.lib import colors
from reportlab.platypus import TableStyle

table_style=TableStyle([
    ('FONTNAME',(0,2),(-1,-1),'msyh'),#字体
    ('FONTNAME', (0,0),(-1,1), 'msyhbd'),
    ('FONTSIZE',(1,2),(-1,-1),9),#字体大小
    ('FONTSIZE', (0,0),(-1,0), 12),  # 字体大小
    ('FONTSIZE', (0, 1), (-1, 1), 11),  # 字体大小
    ('SPAN',(0,0),(-1,0)),#合并第一行前五列
    ('BACKGROUND',(0,0),(-1,0), colors.standardbg),#设置第一行背景颜色
    ('ALIGN',(3,1),(5,-1),'RIGHT'),   #右对齐
    ('ALIGN',(0,0),(-1,1),'CENTER'),  #居中
    ('ALIGN',(0,0),(0,-1),'CENTER'),  #居中
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 对齐
    ('TEXTCOLOR', (0, 1), (-1, 1), colors.standardfl),  # 设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.standardl),#设置表格框线为红色，线宽为0.5
    ('LINEABOVE', (0, 0), (-1, 0), 1.5, colors.standardl),#双线设置
    ('LINEABOVE', (0, 0), (-1, 0), 0.5, colors.white),
    ('LINEBELOW', (0, -1), (-1, -1), 1.5, colors.standardl),
    ('LINEBELOW', (0, -1), (-1, -1), 0.5, colors.white),
    ('LINEBEFORE', (0, 0), (0, -1), 1.5, colors.standardl),
    ('LINEBEFORE', (0, 0), (0, -1), 0.5, colors.white),
    ('LINEAFTER', (-1, 0), (-1, -1), 1.5, colors.standardl),
    ('LINEAFTER', (-1, 0), (-1, -1), 0.5, colors.white),
    ])