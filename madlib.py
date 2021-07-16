
#This is a personal project, applying the principles of string concatenations(adding strings) and variables to produce a madlib.

#variables 
noun = input("noun :")
verb = input("verb :")
verb_ending_in_ing = input("verb_ending_in_ing :")
verb2 = input("verb :")
adjective = input("adjective :")


#Madlib on soccer
madlib = f"The Game of football does not specify player positions other than goalkeeper,but a number of player specialisations has evolved.\
There are  three main {noun}: strikers or forwards,whose main task is to {verb}; defenders,who specialise in preventing their opponents from \
{verb_ending_in_ing}; and midfielders,who {verb2} the opposition and keep possession of the ball in order to pass it to the forwards;\
players in these positions are referred to as {adjective},in order to discern them from the single goalkeeper!"

print(madlib)
