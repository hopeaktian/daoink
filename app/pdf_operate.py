#!/usr/bin/env python
#coding:utf-8

import PyPDF2, subprocess, os

# 定义文件转换后保存的目录
basepath = os.path.abspath(os.path.dirname(__file__))
FileSaveDir = os.path.join(basepath, 'static/Upload_Files')

def read_pdf_pages(file):
    with open(file, 'rb') as pdfFileObj:
        try:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        except:
            return None
        else:
            return pdfReader.numPages


def switch_topdf(filename):
    cmd = "libreoffice --headless --convert-to pdf:writer_pdf_Export {} --outdir {}" .format(filename, FileSaveDir)
    try:
        returnCode = subprocess.call(cmd, shell=True)
        if returnCode != 0:
            raise IOError("{} failed to switch" .format(filename))
    except Exception:
        return 1
    else:
        return 0
