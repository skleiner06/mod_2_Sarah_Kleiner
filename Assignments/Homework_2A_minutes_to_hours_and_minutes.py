"""
Name: Sarah Kleiner
Purpose: Convert a number of minutes into hours and remaining minutes.
"""

def minutes_to_hours_and_minutes():
    """This function asks the user for minutes and converts them into hours and remaining minutes."""

    minutes = int(input('How many minutes would you like to to calculate?')) #Assigns integer input to minutes

    hours = minutes // 60 # Number of full hours: minutes divided by 60
    remaining_minutes = minutes % 60 # Calculates the remaining minutes

    # Display the hours and remaining minutes
    print(hours, 'hours and', remaining_minutes, 'minutes')

    # Calls the function
minutes_to_hours_and_minutes() # Calls the function

