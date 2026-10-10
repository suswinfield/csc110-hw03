"""
Name: Susannah Winfeld - I've asked for an extension so this is just a rough draft
Peers: (add any collaborators)
References: https://www.w3schools.com/python/ref_string_isdigit.asp, https://pythonguides.com/check-if-input-is-a-number-in-python/
"""

# imported modules
import statistics # lets us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros
# Task 1:
#  Complete the function "read_five_ints" below:

def read_five_ints():
    """
updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    for i in range(len(grades)):
        user_input = input("Give me the next grade in [0 to 10]: ")
        #tests that user_input is a valid digit otherwise will print Error message and exit
        if user_input.isdigit() == True:
            #casting input to be an integer
            user_input = int(user_input)
            #checks that user_input is between 1 and 10, if not prints Error message and exits
            if user_input not in range(11):
                print("Error in read_five_ints: input integer outside of range")
                exit()
        #this will print an error message and exit if the value of user_input is not a valid digit
        else :
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        #updates grades with user inpuut at each index
        grades[i] = user_input
    return grades
        
     



        # for each idx in 0, 1,... 4 do:
        # check if the input is not a digit print error
        # convert to int
        # check if the int is not in the interval [0 to 10] print error
        # add the int to grades at index idx


    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
        
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    #asking user for either a b or c, saves response as user_input
    user_input = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    #checking that the input is a b or c
    if user_input == "a" or user_input == "b" or user_input == "c":
        #if a is chosen, runs the mean function
        if user_input == "a":
            print("picked: Mean")
            avg = statistics.mean(grades)
        #if b is chosen it runs the median function
        if user_input == "b":
            print("picked: Median")
            avg = statistics.median(grades)
        #if c is chosen it runs the mode function
        if user_input == "c":
            print("picked: Mode")
            avg = statistics.mode(grades)
    #this will print an error message and exit if the value of user_input is not a b or c
    else :
        print("Error in pick_averaging_method: incorrect option picked")
        exit()
    return avg

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    #asking for user input and saving that value as user_input
    user_input = input("Pick '1' for print average, or '2' for plot average: ")
    #this checks if user_input is 1 or 2
    if user_input == "1" or user_input == "2":
        #runs print_list_and)average() if user_input is 1
        if user_input == "1" :
            print_list_and_average(average)
        #runs plot_grades() if user_input is 2
        else :
            plot_grades(average)
    # this will print an error message and exit if user_input is not 1 or 2
    else :
        print("Error in pick_visualization: incorrect option picked")
        exit()



# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

