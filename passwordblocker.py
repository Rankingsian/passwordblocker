password = "pass123"
your_answer=""
number_of_attempts = 0
number_of_attempts_allowed = 3
max_try = "Not reached"

while  your_answer != password and max_try!= "Reached":
    if number_of_attempts < number_of_attempts_allowed:
        your_answer= input("Please enter your password: ")
        number_of_attempts += 1
    else:
        max_try = "Reached"
        print("You have reached the maximum number of attempts")
        break
if your_answer == password:
    print("Access granted")
else:
    print("Access denied")
# This code is a simple password blocker that restricts access to a system or application by requiring the user to enter a password.
        
    
