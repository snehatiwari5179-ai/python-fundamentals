# A list tracking data streaming sources currently active
data_streams=["Kafka","RabbitMQ"]
# Appending a new data stream tool to the end
data_streams.append("Kinesis")
print(data_streams)
# Using the .insert() Method
data_streams.insert(1, "MQTT")
print(data_streams)
# Using the .extend() Method
batch_tools=["Spark","Flink"]
data_streams.extend(batch_tools)
print(data_streams)
# Creating a tuple (uses standard parentheses) to demonstrate  type unpacking
cloud_storage_tuple=("AWS_S3","Azure_Blob")
data_streams.extend(cloud_storage_tuple)
print(data_streams)