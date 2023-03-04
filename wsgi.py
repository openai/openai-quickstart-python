#!/usr/bin/env python
# encoding: utf-8
"""
#
#                   @Project Name : quick-chatbot
#                                                                   
#                   @File Name    : wsgi.py
#                                                                   
#                   @Programmer   : zhanglu                          
#                                                                     
#                   @Start Date   : 2023/3/3 23:23                 
#                                                                   
#                   @Last Update  : 2023/3/3 23:23                 
#                   
#                   @Description  : 
#                                                                   
#-------------------------------------------------------------------
# Classes:                                                          
#                                                                   
#-------------------------------------------------------------------
"""
from app import app

if __name__ == "__main__":
    app.run()