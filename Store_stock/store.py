#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:58:43 2018

@author: efrancois
"""
#%%
#Imagine you’re creating an application for handling the stock
#of a small shop, and controlling when things go bad in the warehouse.
#Given the following class:


class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
    
 
                    
#We have a function that calculates the degrading quality of different
#products in a shop.
#Create all the tests you find meaningful for the following function.
        


def recalculate_quality(product):
    
    if product.name == "potato":
        product.quality = product.quality - 0.5
        return product.quality
    elif product.name == "cheese":
        product.quality = product.quality - 2
        return product.quality
    else:
        if product.quality < 5:
            product.quality -= 3
            return product.quality


item0 = Product("potato", 10)
item1 = Product("potato", 5)
item2 = Product("potato", 0.5)
item3 = Product("potato", 0)
  
item4 = Product("cheese", 12)
item5 = Product("cheese", 0)
item6 = Product("cheese", 2)

item7 = Product("milk", 1)
item8 = Product("milk", 7)      
    
        
    



    
































