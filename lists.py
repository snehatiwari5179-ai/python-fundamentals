#standard declaration with duplicates & mixed DT.
sample_lists=["Spark", 45, True, 45, "Spark"]
print("Full lists contents:", sample_lists)
print("Total Item Count :",len(sample_lists)) #duplicates counted distinctly
print("Data Architecture:", type(sample_lists)) 

#Deep under-the-hood DT. mixing
#constructing a list containing distinct types to show memory flexibility
int_element = 100
str_element = "Database"
bool_element = False
pipeline_registry= [int_element,str_element,bool_element]
print("Registry Items:",pipeline_registry)

#Utilizing the list() constructor
explicit_list = list(("AWS","Azure","GCP"))
print("Constructor Output :", explicit_list)
print("Contructor Type:",type(explicit_list))

