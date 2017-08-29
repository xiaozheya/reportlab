# -*- coding: utf-8 -*-
import docx
from docx import Document
component_data=[]
def parse_docx(f):
    d = Document(f)
    table = d.tables[0]
    title = table.cell(0,0).text
    row=[title, '', '', '','','']
    #标题和表格传入不同，要传入['巨灵数据库相关表缺失数据明细', '', '', '','','']这样的格式
    component_data.append(row)
    for row, obj_row in enumerate(table.rows):#横向以row遍历
        test = []
        for col, cell in enumerate(obj_row.cells):#纵向用cell遍历而不是col，cell代表每一格
            temp=cell.text
            test.append(temp)
            #print test
        if row!=0:
            component_data.append(test)       #去掉标题行，接下来的加入list
if __name__ == '__main__':
    parse_docx('Excel.docx')