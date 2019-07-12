# Let's add key:value to a dictionary, the functional way 
# Create your dictionary class 
class my_dictionary(dict): 
		# __init__ function 
		def __init__(self): 
			self = dict() 	
		# Function to add key:value 
		def add(self, key, value): 
			self[key] = value 
	# Main Function 
dict_obj = my_dictionary() 
limit = int(input("Enter the no of key value pair in a dictionary"))
c=0
while c < limit :	
	dict_obj.key = input("Enter the key: ") 
	dict_obj.value = input("Enter the value: ") 
	dict_obj.add(dict_obj.key, dict_obj.value) 
	c += 1
print(dict_obj) 
