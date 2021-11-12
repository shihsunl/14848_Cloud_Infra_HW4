from util.google_storage_util import GoogleStorageUtil 
from flask import Flask, json, session, request, redirect, url_for, send_from_directory, render_template
from datetime import datetime
import time
import random
import os

#export GOOGLE_APPLICATION_CREDENTIALS="/Users/bensonlin/Project/CMU/14848_Cloud_Infra/A4/key_for_uploading/splendid-timer-325505-704081761152.json"
LOCAL_FILE_FOLDER = './upload'
BUCKET_NAME = 'dataproc-staging-us-central1-361451194369-hvvm1kp0'
folder_list = ['download', 'upload']
for folder_name in folder_list:
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

api = Flask(__name__, template_folder='./templates', static_folder='./static')
api.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
google_storage_util = GoogleStorageUtil()
DEFAULT_HOST = '0.0.0.0'

@api.route('/', methods=['GET'])
def index():
    return render_template("index.html", success_section='')

@api.route('/list', methods=['GET'])
def list_object():
    
    return

@api.route('/download', methods=['GET'])
def download_object():
    
    return

@api.route('/upload', methods=['POST'])
def upload_object():
    success_msg = 'Remote file path: '
    uploaded_files = request.files.getlist("file")
    print("upload_object: ", uploaded_files)
    for file in uploaded_files:
        filename = os.path.basename(file.filename)
        print("file.filename: ", filename)
        file.save(os.path.join(LOCAL_FILE_FOLDER, filename))

        source_file_name = '{}/{}'.format(LOCAL_FILE_FOLDER, filename)
        destination_blob_name = filename
        remote_file_path = google_storage_util.upload_blob(BUCKET_NAME, source_file_name, destination_blob_name)

        success_msg += '{} '.format(remote_file_path)
    return render_template("index.html", success_section=success_msg)

if __name__ == "__main__":
    api.run(host=DEFAULT_HOST)
