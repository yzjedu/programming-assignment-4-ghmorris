# Programmer: Grace-Ann Morris 
# Course: CS701/GB-731, Dr. Yalew
# Date: August 13, 2024 
# Programming Assignment: 4
# Program Inputs: A positive integer < 1000
# Program Outputs: The English name of the integer

#Integer to English Name 
#Conversion Logic 
def digit_name(n: int) -> str:
    """
    Convert a single digit to its English name.
    Args:
        n (int): A single-digit integer (0-9).
    Returns:
        str: The English name of the digit.
    """
    #List of names for digits from 0 to 9
    names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return names[n]

def teen_name(n: int) -> str:
    """
    Convert a number between 10 and 19 to its English name.
    Args:
        n (int): An integer between 10 and 19.
    Returns:
        str: The English name of the number.
    """
    #List of names for numbers from 10 to 19
    names = ["ten", "eleven", "twelve", "thirteen", "fourteen", 
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    return names[n - 10]

def tens_name(n: int) -> str:
    """
    Convert a number between 20 and 99 to its English name.
    Args:
        n (int): An integer between 20 and 99.
    Returns:
        str: The English name of the number.
    """
    #List of names for tens place (20, 30, etc)
    names = ["", "", "twenty", "thirty", "forty", "fifty", 
             "sixty", "seventy", "eighty", "ninety"]
    #Evaluate if the number is a multiple of 10
    if n % 10 == 0:
        return names[n // 10]
    else:
    #Add tens place name with digit name
        return names[n // 10] + " " + digit_name(n % 10)

def int_name(n: int) -> str:
    """
    Convert a number less than 1000 to its English name.
    Args:
        n (int): An integer less than 1000.
    Returns:
        str: The English name of the number.
    """
    #Edge Cases
    if n == 0: #Edge Case for 0 
        return "zero"
    parts = []
    if n >= 100:
        #Compute hundreds place and the remainder
        hundreds = n // 100
        remainder = n % 100
        parts.append(digit_name(hundreds) + " hundred")
        #Check if there is a remainder to include
        if remainder != 0:
            parts.append(int_name(remainder))
    elif n >= 20:
        #Show tens and units for numbers 20 to 99
        parts.append(tens_name(n))
    elif n >= 10:
        #Includenumbers 10 to 19
        parts.append(teen_name(n))
    else:
        # Include single-digit numbers
        parts.append(digit_name(n))
    return " ".join(parts)

def main():
    """
    Main function to handle user input and print the result.
    """
    try: #Input Validation 
        #Ask the user for input
        number = int(input("Enter a positive integer less than 1000: "))
        #Evaluate Input
        if 0 <= number < 1000:
            print(int_name(number))
        else: #If user inputs a integer above 1000 show error 
            print("Invalid input.Please enter a positive integer less than 1000.")
    except ValueError: #If user inputs anything other than a positive integer
        print("Invalid input.Please enter a valid integer.")

if __name__ == "__main__":
    main()
