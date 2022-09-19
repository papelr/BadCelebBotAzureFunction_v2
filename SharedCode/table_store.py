# Packages
import os
# from azure.data.tables import TableClient
from azure.data.tables import TableServiceClient
from datetime import datetime
from azure.core.exceptions import ResourceExistsError, HttpResponseError


# Class for Azure Table Storage - sending each tweet to a table
class TweetStorage():

    """
    Connects to Azure Storage Account - specifically Table storage;

    For every bot Tweet or reply, the function below stores that Tweet in Table storage, while creating
    an entity delineated below;

    The PartitionKey and RowKey are bot type/Tweet ID. Need to build out function to ensure Tweets don't
    target the same celeb in a certain time period

    """

    def __init__(self):

        # Twitter keys from Azure Key Vault
        self.connx_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

        # Table Service Client
        self.tweet_table = 'BadCelebTweetStorage'
        self.table_service_client = TableServiceClient.from_connection_string(conn_str = self.connx_str)
        self.table_client = self.table_service_client.get_table_client(table_name=self.tweet_table)

        # set datetime object
        self.tweet_date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        # create table if not exists
        self.table_service_client.create_table_if_not_exists(self.tweet_table)  
        print('Table exists')  

    def create_entity_and_push(self, twitter_handle, tweet_id, tweet_text, reply_text, bot_type):

        # get relevant variables for table
        TWEET_ID = tweet_id
        TWEET_HANDLE = twitter_handle
        TWEET_TEXT = tweet_text
        REPLY_TEXT = reply_text
        TWEET_DATE = self.tweet_date
        BOT_TYPE = bot_type
        ROW_KEY = tweet_id

        my_entity = {
            u'TweetID': TWEET_ID,
            u'CelebHandle': TWEET_HANDLE,
            u'TweetText': TWEET_TEXT,
            u'ReplyTweetText': REPLY_TEXT,
            u'TweetDateTime': TWEET_DATE,
            u'PartitionKey': BOT_TYPE,
            u'RowKey': ROW_KEY
        }

        # create the entity
        try:
            entity = self.table_client.create_entity(entity=my_entity)
            print('Entity created - good')
            
        except ResourceExistsError:
            print("Entity already exists")

        # insert the entity into table
        # table_service.insert_entity('tasktable', task)
        
