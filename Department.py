import csv
p=open("Department.csv","w",newline='')

data=csv.writer(p)
data.writerow(["DepartmentID","DepartmentName","ListofBatches"])
for i in range (2):
    DepartmentID=input("Enter Department ID")
    DepartmentName=input("Enter Name")
    ListofBatches=input("Enter Class Roll Number")

    info=[DepartmentID,DepartmentName,ListofBatches] 
    data.writerow(info)
p.close() 