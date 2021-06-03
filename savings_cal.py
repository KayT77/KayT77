#Bob wonders how much money he can save in a year. Help him figure it out by writing a Python program for him.
#The program should calculate how much a person can save in a year based on their hourly income, hours worked, and weekly cost of living.
#We'll build up your program gradually, one step at a time.


#Greet Bob 
greeting = "Helllo "
name = "Bob"
print(greeting  +  name)

#Bob Income (Full Time)
#20/hour ,40hrs/wk , 48wks/yr  

hourly_wage = 20 
hours_per_week = 40
income_per_week = hourly_wage * hours_per_week
weeks_per_year = 48 
income_per_year = income_per_week * weeks_per_year


print (name +"'s weekly income is:")
print (income_per_week)
print (name + "'s yearly income is:")
print(income_per_year)

#Spending 

spend_per_week = 400
spend_per_year = spend_per_week * 52

print( name + "'s yearly spend is:")
print(spend_per_year) 

#Savings 

savings_per_year = income_per_year - spend_per_year

print(name +  "'s yearly savings:")
print(savings_per_year)


# Bob works part time 
# 25hrs , spending -100


#Meeting Alice
# 30/hr , 45hr/wk , 46 weeks , spends 500 