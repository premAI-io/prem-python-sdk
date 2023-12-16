from prem import Prem

api_key = "3EC9HA3EFaQgFbzE8TqsOb0OTrTfFxv2x9"
base_url = "http://localhost:8000"
client = Prem(api_key=api_key, base_url=base_url)

# Test Completions
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]
model = "gpt-3.5-turbo"
response = client.completions.create(
    project_id=1, messages=messages, model=model, stream=False
)
print(response)
response = client.completions.create(
    project_id=1, messages=messages, model=model, stream=True
)
print(f"Number of chunks: {len(response)}")

# Test Embeddings
input = "What is a transformer?"
model = "text-embedding-ada-002"
response = client.embeddings.create(project_id=1, input=input, model=model)
print(f"Embedding dimension: {len(response.data[0])}")

# Test DataPoints
input = "What is a transformer?"
# Creating 10 data points
for _ in range(10):
    data_point = client.datapoints.create(project_id=1, input=input, positive=True)
print(data_point)

# Updating the last data point
patched_data_point = client.datapoints.update(
    datapoint_id=data_point.id, data={"positive": False}
)

# Retrieving the udpated data point
print(client.datapoints.retrieve(datapoint_id=data_point.id))

# Deleting the udpated data point
print("Deleted data point with ID: " + str(data_point.id))
client.datapoints.delete(datapoint_id=data_point.id)

# List the data points
datapoints = client.datapoints.list()
print("Total number of datapoints", len(datapoints))
for datapoint in datapoints:
    print("Deleted data point with ID: " + str(datapoint.id))
    client.datapoints.delete(datapoint_id=datapoint.id)
