num_list = "0123456789"
slice_num = num_list[0:5] #slicing
slice_num = num_list[0:5:2] #hopping
print(slice_num)

chai_type = "Masala"
number_of_cups = 2
print(f"I ordered {number_of_cups} cups of {chai_type} chai.") #list comprehension

chai = "Masala, Lemon, Mint"
print(chai.split(", ")) #converting string to list

chai_list = ["Masala", "Ginger", "Lemon", "Mint"]
print(", ".join(chai_list)) #converting list to string

print(len(chai)) #length of chai