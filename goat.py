
#This is a personal project, applying the principles of string concatenations(adding strings) and variables to produce a madlib.

#variables 
adjective = input("adjective: ")
pronoun = input("pronoun: ")
name1 = input("name1: ")
name2 = input("name2: ")
event = input("event: ")
number= input("number: ")
sport = input("sport: ")
acronym =input("acronym: ")


#Madlib about soccer/football  (G.O.A.T debate ,Messi vs Ronaldo)
madlib = f"The football gods should be {adjective} enough to give {pronoun} what we want.{name1} versus {name2} in a/an {event}  won't just\
be epic,but will help the {number} of {sport} fans settle the debate as to who the {acronym} is!"

print(madlib)

breakpoint