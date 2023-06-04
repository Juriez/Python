# creating new dictionary
x = ('Batsman','Bowler','Wicket keeper')
y = "Mahir Faisal"
dictionary = dict.fromkeys(x,y)
print("Creat new dictionary :")
for w,z in dictionary.items():
    print(w,z)
# to update the dictionary
dictionary.update({"Umpire" : "Rod Tuccer"})
print("After updating dictionary :")
for w,z in dictionary.items():
    print(w,z)