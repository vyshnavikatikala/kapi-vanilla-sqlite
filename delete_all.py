#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import sqlite3
import random
from sqlite3 import Error

import zenv

database = zenv.DB_LOCATION

def delete_all():
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """    
    conn = None
    
    try:
        conn = sqlite3.connect(database)        
    except Error as e:
        return(e) 
    
    sql = ''' DELETE FROM MOVIE'''
    cur = conn.cursor()
    
    try:
        cur.execute(sql)       
    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    finally:        
        conn.commit()
    
    return('Deleted All!')

if __name__ == '__main__':
    delete_all()        