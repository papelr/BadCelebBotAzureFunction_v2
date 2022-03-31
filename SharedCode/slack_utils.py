# Packages
import json
import os
import sys
import requests

# NEED to figure out how to put the auth part in the __init__ method

# Class for Slack notifications ----
class SlackNotifications():

    """
    Slack notification class - a few methods to post notifications to a slack 
    channel dedicated to showing post success or failure. Simple, but I think
    a separate Slack class is the way to go...
    """

    def __init__(self):
        
        # Slack hook from Azure Key Vault
        self.slackhook = os.getenv('SlackhookKey')
        

    # [TIMELINE] Twitter Post SUCCESS notification function ----
    def timeline_post_win(self):

        # Slack hook set-up
        url = self.slackhook
        message = ("Success")
        title = ("Tweet Posted Successfully!")

        # build the message
        slack_data = {
            'icon_emoji' : ':thumbsup:',
            "channel" : "#timeline-post",
            "attachments": [
                {"color": "#3DFB00", #color: bright green
                "fields": [
                        {"title": title,
                         "value": message,
                         "short": "false", }]}]}

        # Slack authorization
        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(url, data=json.dumps(slack_data), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)


    # [TIMELINE] Twitter Post FAILURE notification function ----
    def timeline_post_loss(self):

        # Slack hook set-up
        url = self.slackhook
        message = ("Fail")
        title = ("Tweet Post Failed!")

        # build the message
        slack_data = {
            'icon_emoji' : ':thumbsdown:',
            "channel" : "#timeline-post",
            "attachments": [
                {"color": "#FB1B00", #color: bright red
                "fields": [
                        {"title": title,
                         "value": message,
                         "short": "false", }]}]}

        # posting to slack
        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(url, data=json.dumps(slack_data), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)


    # [REPLY] Twitter Post SUCCESS notification function ----
    def reply_post_win(self):

        # Slack hook set-up
        url = self.slackhook
        message = ("Success")
        title = ("Tweet Posted Successfully!")

        # build the message
        slack_data = {
            'icon_emoji' : ':grinning:',
            "channel" : "#reply-post",
            "attachments": [
                {"color": "#3DFB00", #color: bright green
                "fields": [
                        {"title": title,
                         "value": message,
                         "short": "false", }]}]}

        # Slack authorization
        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(url, data=json.dumps(slack_data), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)      


    # [REPLY] Twitter Post FAILURE notification function ----
    def reply_post_loss(self):

        # Slack hook set-up
        url = self.slackhook
        message = ("Fail")
        title = ("Tweet Post Failed!")

        # build the message
        slack_data = {
            'icon_emoji' : ':confused:',
            "channel" : "#reply-post",
            "attachments": [
                {"color": "#FB1B00", #color: bright red
                "fields": [
                        {"title": title,
                         "value": message,
                         "short": "false", }]}]}

        # posting to slack
        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(url, data=json.dumps(slack_data), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)          



