# empty tupple
my_tupple=()
print(my_tupple)

#tupple with integers
my_tupple=(3,5,2)
print(my_tupple)

#tupple with mixed datatype
my_tupple=("box",2,0.3)
print(my_tupple)

#nested tupple
my_tupple=("box",[1,7,2],(11,4,7))
print(my_tupple)

#excess tupple elements using indexing
my_tupple=('b','l','a','c','k','b','o','x')
print(my_tupple[0])
print(my_tupple[5])

#nested tupple
my_tupple=("box",[1,7,2],(11,4,7))
print(my_tupple[0][3])
print(my_tupple[1][1])
print("Scliced " ,my_tupple[1:4])

#etrating tupple
for letter in (my_tupple):
    print("Hello",letter)