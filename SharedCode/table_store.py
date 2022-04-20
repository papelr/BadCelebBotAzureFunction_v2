# Packages
from datetime import datetime
import os
from azure.data.tables import TableClient
from azure.core.exceptions import ResourceExistsError, HttpResponseError

# Class lifted from Auzre Table Docs
class InsertDeleteEntity(object):

    def __init__(self):
        # self.access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        # self.endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        # self.account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        # self.endpoint = "{}.table.{}".format(self.account_name, self.endpoint_suffix)
        self.connection_string = (
            "DefaultEndpointsProtocol=https;AccountName=badcelebbotazurefunction;AccountKey=z27QhooGOWMiJ6sGONKgc2TPuilPPuv7YF6Y3pvFqtkcrcFrrBs7kaBgZfZsQ80OOUdR3CJiZy3a+AStSBCPHA==;EndpointSuffix=core.windows.net"
            )
        
        # self.connection_string = (
        #     "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
        #         self.account_name, self.access_key, self.endpoint_suffix
        #     )
        # )
        self.table_name = "SampleInsertDelete"

        self.entity = {
            "PartitionKey": "color",
            "RowKey": "brand",
            "text": "Marker",
            "color": "Purple",
            "price": 4.99,
            "last_updated": datetime.today(),
            "product_id": (),
            "inventory_count": 42,
            "barcode": b"135aefg8oj0ld58"
        }

    # create entity (or a record?)
    def create_entity(self):

        with TableClient.from_connection_string(self.connection_string, self.table_name) as table_client:

            # Create a table in case it does not already exist
            try:
                table_client.create_table()
            except HttpResponseError:
                print("Table already exists")

            # [START create_entity]
            try:
                resp = table_client.create_entity(entity=self.entity)
                print(resp)
            except ResourceExistsError:
                print("Entity already exists")
        # [END create_entity]


if __name__ == "__main__":
    ide = InsertDeleteEntity()
    ide.create_entity()
