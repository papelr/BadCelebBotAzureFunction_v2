# Packages
import os
from azure.data.tables import TableClient
from azure.data.tables import TableServiceClient
from datetime import datetime


# Class for Azure Table Storage - sending each tweet to a table
class TweetStorage():

    """
    Text
    """

    def __init__(self):

        # Twitter keys from Azure Key Vault
        self.connx_str = os.getenv('TweetTableConnectionString')

        # Table Service Client
        self.table_service_client = TableServiceClient.from_connection_string(conn_str = self.connx_str)
        self.table_client = self.table_service_client.get_table_client(table_name="myTable")

        # set datetime object
        self.tweet_date = datetime.today()

    def create_or_insert(self, ):

        table_service_client.create_table_if_not_exists()    

    def create_entity_and_push(self, twitter_handle, tweet_id, tweet_text, reply_text):

        # get relevant variables for table
        TWEET_ID = tweet_id
        TWEET_HANDLE = twitter_handle
        TWEET_TEXT = tweet_text
        REPLY_TEXT = reply_text
        # date? + time would be useful
        TWEET_DATE = self.tweet_date


        my_entity = {
            u'Tweet ID': TWEET_ID,
            u'Celeb Handle': TWEET_HANDLE,
            u'Tweet Text': TWEET_TEXT,
            u'Reply Tweet Text': REPLY_TEXT,
            u'Tweet DateTime': TWEET_DATE
        }

        entity = table_client.create_entity(entity=my_entity)

#test
