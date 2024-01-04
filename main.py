# Print a welcome message to the user
print ("Hi, 👋  Welcome to profile description generator! Lets begin! ")

# Create the main loop
while True:
    
    # Create the sub loop for asking the user for their name
    while True:
        print ("Lets fill in your details for the first option! ")
    
        # Ask the user to input a name
        name = input ("Hi, 👋 My name is ENTER NAME HERE-")
        
        # Ask the user if the name is correct
        choice = input ("Are you sure you would like your name to be " + name + "? (y, n) ")
        
        # If the user is sure they would like their name to be the one input run this
        if choice == "y":
            # Print a message to the user confirming the first line of your profile
            print ("Great! The first line of your profile is this! Hi, My name is " + name + "! ")
            # Write this data to the file
            with open ("descript.txt", "w" ) as descript:
                descript.write ("Hi, My name is " + name + "! \n")
            # Break out of the subloop
            break
        
        # If the user has decided to reset their name
        elif choice == "n":
            print ("Lets try that one more time shall we. ")
            
        # If the user has put in a invalid input
        else:
            print ("Invalid Input: Please retry")
    
    # Create a sub loop for creating where the user is based        
    while True:
        print ("Lets fill in your details for the second option! ")
     
        # Ask the user where they  are based   
        location = input ("Please enter the location you are based in. ")
    
        choice = input ("Are you sure you would like to set your location to be in " + location + "? (y, n)" )
        
        if choice == "y":
            # Print a message to the user confirming that they have chosen the selected option to be there location
            print ("Great! This is the second line of your profile: I am based in " + location + "! ")
            # Write this data to the file
            with open ("descript.txt", "a" ) as descript:
                descript.write ("I am based in " + location + "! \n")
            # Break out of the subloop
            break
        
        # If the user has decided to reset their location
        elif choice == "n":
            print ("Lets try that one more time shall we. ")
            
        # If the user has put in a invalid input
        else:
            print ("Invalid Input: Please retry")
            
    # Ask the user for a bio
    bio = input ("Why dont you write a short bio about yourself? ")
    print ("This is your Bio: " + bio)
    with open ("descript.txt", "a") as descript:
        descript.write ("About Me: " + bio + "\n")
        
    # Ask for a fun fact about the user
    fact = input ("How about a fun fact about yourself? ")
    with open ("descript.txt", "a") as descript:
        descript.write ("Fun Fact about me: " + fact + "\n")
        
    # Give the user the finished profile
    print ("Looks like we are all done now! Just copy this text then add it into your profile description! ")
    with open ("descript.txt", "r") as descript:
        content = descript.read()
        print (content)
    break