#if , elif , else


# Syntax
# 
#if condition:
#    statement
# elif condition:
#     statement
#else: condition
#   statement


number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')


#with if and else 
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')

#with if elif and else statement
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')


# outer if statement NESTED IF ELSE
#if condition1:
    # statement(s)

    # inner if statement
#    if condition2: 
        # statement(s)