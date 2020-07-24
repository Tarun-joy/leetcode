import pymongo
from pymongo import MongoClient
import traceback
import logging
import json
import sys
import os

from utils import get_logger

# Setup Logging (python logging)
# Setup Logging (python logging)
_log = None
try:
    _log_level = os.getenv('LOG_LEVEL')
    if not _log_level:
        _log_level = 'error'

    _log = get_logger(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.json'), logLevel=_log_level)
    _log.debug(type(_log))

except TypeError as e:
    print(traceback.format_exc())
    sys.exit(1)


# Accessing the environment variable API_KEY
config = {'MDB_URL': os.environ.get('MDB_URL'),'DATABASE':os.environ.get('DATA_RET_DATABASE'),'COLLECTION':os.environ.get('DATA_RET_COLLECTION')}
mongo_conn = pymongo.MongoClient(config['MDB_URL'])
mongo_db = mongo_conn['AR_SCRAPE']
mongo_coll = mongo_db['MOBILE']

def get_product_feature_info(device_name,device_feature,details):
    """
    given a device_name,device_feature and details this function makes a database read call to retrieve detailed product information
    :param product_id_input: {"device_name":The name of the devce we want the result for,
                              "device_feature": The name of the feature you want information for,
                              "details": 0 for short info and 1 for long info}
    :return: feature data for the device
    """
    if mongo_coll.find_one({"device_name":device_name}):
        document = mongo_coll.find_one({"device_name":device_name})
        if device_feature == "camera" and details == 0:
            camera_details = {}
            camera = document["cleaned_output"]["camera"]
            camera_details["device_name"] = device_name
            camera_details["device_feature"] = device_feature
            front_count = 0
            rear_count = 0
            for i in camera:
                for index in range(len(i)):
                    nxt_len = index + len("front")
                    if i[index:nxt_len] == "front":
                        front_count += 1
                    rear_nxt_len = index + len("rear")
                    if i[index:rear_nxt_len] == "rear":
                        rear_count += 1
            camera_details["number_of_front_cameras"] = front_count
            camera_details["number_of_rear_cameras"] = rear_count
            camera_details["front_camera_features"] = camera["front_camera"]["features"]
            camera_details["rear_camera_features"] = camera["rear_camera"]["features"]
            return camera_details
        elif device_feature == "camera" and details == 1:
            camera_details = {}
            camera_details["device_name"] = device_name
            camera_details["device_feature"] = device_feature
            camera = document["cleaned_output"]["camera"]
            camera_details["Camera_details"] = camera
            return camera_details
        else:
            return "Details not available"
    else:
            return "Details not available"


