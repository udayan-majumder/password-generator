import random as r
#elements of password
pass_element=["@","!","#","$","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list_len=len(pass_element)
#password storage
new_pass=""
#loop for creating password
pass_len=int(input("password length:"))
for i in range(pass_len):
    pass_data=pass_element[r.randint(0,list_len)]
    new_pass+=pass_data
print(new_pass)    