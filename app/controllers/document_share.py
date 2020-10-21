#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g

document_share = Blueprint(
    'document_share',
    __name__,
    # template_folder='templates/document_share'
)
@document_share.route('/docshare', methods=['GET', 'POST'])
def detailedu():
    return render_template('docshare.html')
