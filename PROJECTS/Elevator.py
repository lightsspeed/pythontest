E1 = 0  # Initial floor of elevator 1
E2 = 0  # Initial floor of elevator 2

while True:
    user = int(input("User's floor is (or type 'q' to quit): "))
    
    if user == 'q':
        break  # Exit the loop if the user enters 'q'
    
    distance_to_E1 = abs(user - E1)
    distance_to_E2 = abs(user - E2)
    
    if distance_to_E1 <= distance_to_E2:
        print("E1 is arriving at floor: ", user)
        E1 = user
        print("E1 is at floor no: ", user)
    else:
        print("E2 is arriving at floor ", user)
        E2 = user
        print("E2 is at floor no: ", user)
