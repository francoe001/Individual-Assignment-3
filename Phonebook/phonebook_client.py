#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:31:30 2018

@author: efrancois
"""

import requests

def get_contacts_client():
    url = 'http://127.0.0.1:5000/contacts'
    response = requests.get(url)
    return response.json()


def add_contact_client(name, number):
    url = "http://127.0.0.1:5000/add_contact/{}/{}".format(name, number)
    response = requests.put(url)
    return response.json()
    
def get_contact_client(name):
    url = "http//127.0.0.1:5000/get_contact/{}".format(name)
    response = requests.get(url)
    return response.json()

def delete_contact_client(name):
    url = "http//127.0.0.1:5000/delete_contact/{}".format(name)
    response = requests.delete(url)
    return response.json()


def update_contact_client(name, number):
    url = "http//127.0.0.1:5000/update_contact/{}/{}".format(name, number)
    response = requests.post(url)
    return response.json()





