# 14848_Cloud_Infra_HW4
14848_Cloud_Infra_HW4

### Prepare input data
![prepare_input_data](screenshot/prepare_input_data.png)

### Run mapreduce
![run_mapreduce](screenshot/run_mapreduce.png)

### List output files
![output_files](screenshot/output_files.png)

### Merge output files
![merge_output_files](screenshot/merge_output_files.png)

### Print merged output file
![print_merged_output](screenshot/print_merged_output.png)

### Copy merged output to bucket
![copy_merged_output_to_bucket](screenshot/copy_merged_output_to_bucket.png)
- Then, you can download result from the GCP bucket

### Extra Credit
- Video: https://www.youtube.com/watch?v=xA_9fQ-ouAc

- Step1: First, you need to create your GCP credentials and export the credential file path to the environment variable.
![create_key](screenshot/create_key.png)
![create_service_account](screenshot/create_service_account.png)

```
export GOOGLE_APPLICATION_CREDENTIALS="/Users/bensonlin/Project/CMU/14848_Cloud_Infra/A4/key_for_uploading/splendid-timer-325505-704081761152.json"
``` 

- Step2: Execute the API server and then you can upload a folder
```
python3 app.py
```
![UI](screenshot/ui.png)

- Here's the upload function
You can check util/google_storage_util.py to get more details.
![upload_function](screenshot/upload_function.png)

