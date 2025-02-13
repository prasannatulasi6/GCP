from apache_beam.io import ReadFromBigQuery, WriteToBigQuery
import apache_beam as beam

def run_pipeline():
    pipeline = beam.Pipeline()

    query = "SELECT * FROM `my_project.my_dataset.my_table`"
    (pipeline
        | 'Read from BigQuery' >> ReadFromBigQuery(query=query)
        | 'Process Data' >> beam.Map(process_data)
        | 'Write to BigQuery' >> WriteToBigQuery('my_project.my_dataset.new_table')
    )

    pipeline.run()

def process_data(row):
    # Transform the data
    return row
