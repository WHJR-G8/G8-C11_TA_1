dict1={"Name":"Tom","Age":12,"Grade":8}
print("The original dictionary is:\n", dict1)

dict1["Name"]="Sam"
print("\nThe dictionary after updating the name is :\n", dict1)

dict1["RollNo"]=1
print("\nThe dictionary after adding roll number is :\n", dict1)

dict1.pop("Grade")
print("\nThe dictionary after removing the name is :\n", dict1)
