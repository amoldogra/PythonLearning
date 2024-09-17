#Python program to find the sum of all items in a dictionary

Input = {"a": 100, "b":200, "c":300}
def sum_of_values(dict):
  lst=[]    
  for i in dict:
    lst.append(dict[i])
  final = sum(lst)  
  return final
        

print(sum_of_values(Input))