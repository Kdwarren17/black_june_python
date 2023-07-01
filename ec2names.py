import random

ec2_amount = int(input("How many EC2 instances do you want names for? "))
department_name = input("What is your department name? ")
    
characters = ['&', '*', '$', '?', '@', '^', '%', '_', '#', '!!']
    
# Generate EC2 names
for i in range(int(ec2_amount)):
    # Generate a random number between 0 and 99
    numbers = random.randrange(100)
      
    # Concatenate the department name, a randon character, and the random number
    ec2_name = department_name + random.choice(characters) + str(numbers)
      
    # Print the generated EC2 name
    print(ec2_name)
