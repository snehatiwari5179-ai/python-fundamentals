# A list tracking processing tools in a data stream pipeline
data_tools=["SQL","Spark","Kafka","SQL","Airflow"]
# Deleting the first occurrence of a specific value
data_tools.remove("SQL")
print(data_tools)                                                       # (notice the second SQL remains)
# Deleting by specific index position
popped_item=data_tools.pop(1)
print(f"Popped item was = {popped_item}")
print(data_tools)                                                       # first SQL is deleted so index 1 is Kafka
# Deleting the absolute last item when index is omitted
data_tools.pop()
print("After empty pop() = ", data_tools)                       #  Now, the list only has 2 items left "Spark" & "SQL"
# del keyword
del data_tools[0]
print("After del item [0] = ",data_tools)    
# Flushing the list empty without destroying container
data_tools.clear()
print(data_tools)                                                   # All items in basket dumped out.