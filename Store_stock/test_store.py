#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 18:12:10 2018

@author: efrancois
"""

from store import item0, item1, item2, item3, item4, item5, item6, item7, item8
from store import recalculate_quality

def test_recalculate_quality():
    
    assert recalculate_quality(item0) == 9.5
    assert recalculate_quality(item1) == 4.5
    assert recalculate_quality(item2) == 0
    assert recalculate_quality(item3) == -0.5
    
    assert recalculate_quality(item4) == 10
    assert recalculate_quality(item5) == -2
    assert recalculate_quality(item6) == 0
    
    assert recalculate_quality(item7) == -2
    assert recalculate_quality(item8) == None
   
    
    
    
def test_recalculate_quality_again():
        
    assert recalculate_quality(item0) == 9
    assert recalculate_quality(item1) == 4
    assert recalculate_quality(item2) == -0.5
    assert recalculate_quality(item3) == -1
    
    assert recalculate_quality(item4) == 8
    assert recalculate_quality(item5) == -4
    assert recalculate_quality(item6) == -2
    
    assert recalculate_quality(item7) == -5
    assert recalculate_quality(item8) == None
    
    
    