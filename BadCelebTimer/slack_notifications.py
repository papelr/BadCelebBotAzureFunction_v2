#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:42:59 2021

@author: robertpapel
"""

import json
import sys
import requests
from .all_keys import slackhook


# Scrape SUCCESS notification function ----
def scrape_worked():

    # slack hook set-up
    url = slackhook
    # message = ("Image scrape DONE")
    title = ("Image Scraped Successfully!")

    # data sent to slack hook
    slack_data = {
        # "username": "",
        'icon_emoji' : ':ok_woman:',
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#3DFB00", #color: bright green
                "fields": [
                    {
                        "title": title,
                        # "value": message,
                        "short": "false",
                    }]}]}

    # posting to slack
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


# Scrape FAILED notification function ----
def scrape_failed():

    # slack hook set-up
    url = slackhook
    # message = ("Image scrape DONE")
    title = ("Image Scraped Failed!")

    # data sent to slack hook
    slack_data = {
        # "username": "",
        'icon_emoji' : ':skull:',
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#FB1B00", #color: bright red
                "fields": [
                    {
                        "title": title,
                        # "value": message,
                        "short": "false",
                    }]}]}

    # posting to slack
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)



# Twitter Post SUCCESS notification function ----
def post_worked():

    # slack hook set-up
    url = slackhook
    # message = ("Twitter Notification Bot")
    title = ("Tweet Posted Successfully!")

    # data sent to slack hook
    slack_data = {
        # "username": "Twitter Post SUCCESS",
        'icon_emoji' : ':thumbsup:',
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#3DFB00", #color: bright green
                "fields": [
                    {
                        "title": title,
                        # "value": message,
                        "short": "false",
                    }

                    ]}]}

    # posting to slack
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

# Twitter Post FAILURE notification function ----
def post_failed():

    # slack hook set-up
    url = slackhook
    # message = ("Twitter Notification Bot")
    title = ("Tweet Posted Failed!")

    # data sent to slack hook
    slack_data = {
        # "username": "Twitter Post SUCCESS",
        'icon_emoji' : ':thumbsdown:',
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#FB1B00", #color: bright red
                "fields": [
                    {
                        "title": title,
                        # "value": message,
                        "short": "false",
                    }

                    ]}]}

    # posting to slack
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

# Main function ----
if __name__ == '__main__':
    scrape_worked()
    scrape_failed()
    post_worked()
    post_failed()






##### Detritus


    # if this function gets a positive return from the scrape function
    # if this function gets any error from the scrape function
    # try:
    #     function(*args)
    #     print(function + ' worked!')
    # except:
    #     print(function + ' failed')
    # finally:
    #     pass
