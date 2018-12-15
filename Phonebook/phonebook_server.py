#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:29:38 2018

@author: efrancois
"""

#%%
#Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.
    

from flask import Flask, jsonify

server = Flask("Contacts")

contacts = {"John": "9394843003",
            "Boss": "8494948383",
            "Mama": "4938394940",
            "Ex-GF": "94490303203"}


@server.route("/contacts")
def get_contacts():
    return jsonify(contacts)


@server.route("/add_contact/<name>/<number>", methods=["PUT"])
def add_contact(name, number):
    contacts.append({name: number})
    return jsonify(name, ':' , number, 'added')

@server.route("/get_contact/<name>/")
def get_contact(name):
    return jsonify(name + ':', contacts[name])

@server.route("/delete_contact/<name>", methods=["DELETE"])
def delete_contact(name):
    if name in contacts:        
        contacts.remove(name)
    else:
        return jsonify("contact doesn't exist")
    
    return jsonify(name, "has been deleted")

@server.route("/update_contact/<name>/<number>", methods=["POST"])
def update_contact(name, number):
    if name not in contacts:
        return jsonify("contact does not exist")
    
    else:
        contacts[name] = number
        return jsonify("contact " + name + "has been updated to: ", number)
    
server.run()




        


