# Basic Unpacking
server_data = ("127.0.0.1",8080,"HTTP")
# unpacking into 3 variables
host,port,protocol = server_data
print("1.Standard Unpacking:")
print("Host:", host)
print("Port:", port)
print("Protocol:", protocol)

# Using Asterisk * at the end
sales_record= ("Mumbai Branch",50000, 62000, 48000, 71000)
# Unpack branch name into 'branch', & all sales figure into 'monthly_sales'
branch,*monthly_sales=sales_record
print("2.Asterisk at End:")
print("Branch Name:", branch)
print("Sales List:", monthly_sales)

# Using Asterisk in the Middle
emp_info= (101,"Python","SQL","Spark","Data Engineer")
# unpack ID into 'emp_id',Role into 'job_title',& skills into 'skills'
emp_id,*skills,job_title = emp_info
print("3.Asterisk in Middle:")
print("Employee ID:", emp_id)
print("Skills List:",skills)  # everything left in mid ( * on skills) will be gathered into list & placed inside skills
print("Job Title:",job_title)