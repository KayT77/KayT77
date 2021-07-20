#This is a love calculator, logic = the number of times a letter appears in "TRUELOVE"  

print("Welcome to the love calculator:")
his_name = input("What is his name?")
her_name = input("what is her name?")

#both names are added together as combined_names eg Tim and Elle = "timelle" and compared to TRUELOVE for a count
combined_names = his_name.lower() + her_name.lower() 
T = int(combined_names.count("t"))
R = int(combined_names.count("r"))
U = int(combined_names.count("u"))
E = int(combined_names.count("e"))
L = int(combined_names.count("l"))
O = int(combined_names.count("o"))
V = int(combined_names.count("v"))
E = int(combined_names.count("e"))


#count is based on the number of times a letter from "combined_names" appears in TRUELOVE
 
Total1 = T + R + U + E
Total2 = L + O + V + E
score = int(str(Total1) + str(Total2))


if score < 10 or score > 90:
    print(f'Your score is {score},you two go together like milk and honey')

elif score < 40 or score > 50:
    print(f'Your score is {score}, you two are just ok!')

else :
    print(f'Your score is {score}')