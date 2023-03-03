#!/usr/bin/env python
# encoding: utf-8
"""
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- WellCloud                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : openai-quickstart-python                 
#                                                                   
#                   @File Name    : initdb.py                      
#                                                                   
#                   @Programmer   : zhanglu                          
#                                                                     
#                   @Start Date   : 2023/3/3 21:17                 
#                                                                   
#                   @Last Update  : 2023/3/3 21:17                 
#                   
#                   @Description  : 
#                                                                   
#-------------------------------------------------------------------
# Classes:                                                          
#                                                                   
#-------------------------------------------------------------------
"""
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username
