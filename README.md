[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JI_9fwwW)
# Programming Assignment: Integer to English Name

## Objective

This assignment will test your ability to use functions together with conditionals and loops to implement a program that converts an integer into its English name.

## Problem Statement

When printing a check, it is customary to write the check amount both as a number (“$274.15”) and as a text string (“two hundred seventy four dollars and 15 cents”). Doing so reduces the recipient’s temptation to add a few digits in front of the amount. For a human, this isn’t particularly difficult, but how can a computer do this? There is no built-in function that turns 274 into "two hundred seventy four". We need to program this function. You are tasked with writing a program that converts a positive integer less than 1000 into its English name. The program should be able to handle numbers in the hundreds, tens, and units.

### Tasks

1. **Input Validation**:

   - Prompt the user to enter a positive integer less than 1000.

2. **Conversion Logic**:

   - Use conditionals to break down the number into hundreds, tens, and units, and convert each part to its English equivalent.
   - Construct the full English name by combining these parts.

3. **Edge Cases**:
   - Ensure that the program handles edge cases, such as numbers in the teens and the edge of each hundred.

## Hint

 - You will need few fucntions complete this assignment

#### 1. A `main()` function
- **Purpose**: Serves as the entry point of the program.
- **Functionality**:
  - Prompts the user to input a positive integer less than 1000.
  - Calls the `intName()` function to convert the input number into its English name and prints the result.

#### 2. `intName(number)`
- **Purpose**: Converts a number into its English name.
- **Parameters**: `number` (a positive integer < 1000).
- **Returns**: A string representing the English name of the number.
- **Logic**:
  - If the number is 100 or greater, it determines the hundreds part by calling `digitName()` and appending "hundred".
  - It handles numbers from 20 to 99 using the `tensName()` function and numbers from 10 to 19 using the `teenName()` function.
  - For numbers less than 10, it directly calls `digitName()`.


## Instructions

1. Update the `assignment.py` file with the conversion logic.
2. Use comments to document your code and describe your approach.
3. Test your completed code using the test cases provided in the `test_assignment.py` file.

## Intro Comments Template

```python
# Programmer: [your name]
# Course: CS701/GB-731, Dr. Yalew
# Date: [Submission date]
# Programming Assignment: 4
# Program Inputs: A positive integer < 1000
# Program Outputs: The English name of the integer
```

## Submission

- Clone the project
- Follow the instructions on the README.md file and the comment on code
  - Complete the code
  - You can look into the `test_assignment.py` for inspiratin too
- **Test the program**: by running `pytest`
  - If the test passes
    - Push the project to the repository
      - If this is hard
      - Submit the assignment.py on moodle
