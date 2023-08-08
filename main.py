#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 23:02:26 2023

@author: laksh
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sqlite3


app = FastAPI()
conn = sqlite3.connect('/Users/laksh/Desktop/precriptions1.db')

@app.get('/prescriptions1')
async def get_prescriptions(drug_name: str):
    
    cursor = conn.cursor()
    
    cursor.execute(
        f'SELECT year, COUNT(*) FROM prescribed_drug WHERE drug_name = ? GROUP BY year',
        (drug_name,),
        )
    
    result = cursor.fetchall()
    
    conn.close()
    
    return JSONResponse(result)
    