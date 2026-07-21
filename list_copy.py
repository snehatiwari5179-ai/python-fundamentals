# Our original master data records
raw_data=["Sneha","Sweety"]
# Using .copy()
safe_copy_1=raw_data.copy()
safe_copy_1.append("Sweetu")
print("Og Data stays safe:",raw_data)
print("Safe Copy 1 updated properly:",safe_copy_1)
# Using list()
safe_copy_2=list(raw_data)
safe_copy_2.append("Puchu")
print("Safe Copy 2 updated properly:",safe_copy_2)
# Using [:] slicing
safe_copy_3=raw_data[:]
safe_copy_3.append("Laado")
print("Safe Copy 3 updated properly:",safe_copy_3)