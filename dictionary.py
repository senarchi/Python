dict={}
set1=set()
print(dict,type(dict))
print(set1,type(set1))

dict1={"English":95,"Maths":88,"Chemistry":89,"Physics":69}
print(dict1["English"])

dict1["Computer Science"]=92
print(dict1)

print(dict1.pop("Maths"))
print(dict1)
print(dict1.get("Akash")) #None
print(dict1.get("Physics"))
print(dict1.values())
print(dict1.keys())
print(dict1.items())