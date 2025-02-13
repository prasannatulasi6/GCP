from google.cloud import storage

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket."""
    bucket = event['bucket']
    file = event['name']
    print(f"Processing file: {file} in bucket: {bucket}")
