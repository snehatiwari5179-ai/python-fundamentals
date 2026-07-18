# A list tracking data formats processed by a storage layer
data_formats=["CSV","JSON","XML","Parquet","Avro"]
#changing a single specific item
data_formats[2]="Delta"
print(data_formats)
# Changing a range with matching quantities
data_formats[1:3]=["Text","ORC"]
print(data_formats)
# Replacing a range with MORE Items (Expansion)
data_formats[1:3]=["excel","tsv","BSON"]
print(data_formats)
print("new total list length :",len(data_formats))
# Replacing a range with FEWER Items (Shrinkage)
data_formats[1:4]=["YAML"]
print(data_formats)
print("new total list length :",len(data_formats))