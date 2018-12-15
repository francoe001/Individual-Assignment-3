#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:32:01 2018

@author: efrancois
"""
#%%
#Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its name, number
#of stars, main language, and url

import requests
import secret



secret.apikey



def list_all_repositories(user): 
    
    response = requests.get("https://api.github.com/users/" + user + "/repos")
            
    repos = response.json()
    
    
    all_repos = []
            
    for repo in repos: 
        
        items = {
                    "description": repo["description"],       
                    "title": repo["title"],    
                    "notes": repo["notes"],
                    "comments": repo["comments"],
                    "url": repo["url"] 
                }
        
        all_repos.append(items)
        
                
    return all_repos