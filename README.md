Have you ever created a program that takes input from the command line? Have you ever wanted to convert the input to an integer or any other type? If so, you'll know how annoying it can be. Try/except blocks, while loops, multiple input calls and much more... but what if I told you that you can forget about those and just use this module! Introducing...

# InputValidation
A python module to validate input.

# Supported Operating Systems
The inputvalidation module should be supported on Windows, Linux and Mac (althought it has not been tested on Mac).

# Installation
The inputvalidation module can be install using pip.
```
pip install inputvalidation
```
# Usage
```python
import inputvalidation as iv
```

After you imported the inputvalidation module you're ready to go.

```python
# Simple int validator
intValidator = iv.Validator(type=int)
intNumber = intValidator.input("Enter an integer: ") # Enter an integer: 15
print("\nNumber:", intNumber, type(number)) # Number: 15 <class 'int'>
```

Here's a simple validator using regex to make sure the user enters a valid phone number.

```python
phoneValidator = iv.Validator(pattern=r"^\([2-9][\d]{2}\) [\d]{3}-[\d]{4}$") # Regex pattern to match phone numbers
phoneNumber = phoneValidator.input("Enter a phone number: ")
print("\nPhone number:", phoneNumber)
```

Here's what happens when you run the previous code block.

```
Enter a phone number: 23980983
Enter a phone number: 24-42653-35
Enter a phone number: (234) 567-8901

Phone number: (234) 567-8901
```

You don't have to call the input method to use the validator, you can validate strings using the validate method instead.

```python
print(
    intValidator.validate("162"), # True
    intValidator.validate("0x5"), # False
    intValidator.validate("Hello, world!"), # False
sep="\n")
```

The inputvalidation module also supports default values for when the user leaves the input field empty.

```python
# Validator using the default parameter
nameValidator = iv.Validator(default="John Doe")
name = nameValidator.input(f"Enter your name (default = {nameValidator.default}): ") # Enter your name (default = John Doe): 
print("\nName:", name) # Name: John Doe
```

If you want to ask the user a multiple choice question you can use the MultipleChoice validator.

```python
# Multiple choice input
modeValidator = iv.MultipleChoice(options=["yes", "no"], default="no", caseSensitive=False)
answer = modeValidator.input(f"Are you sure you want to exit? (default = {modeValidator.default}): ") # Are you sure you want to exit? (default = no): Yes
print("\nAnswer:", answer) # Answer: yes
```

You can make the validators as complex as you like. Converting the input to a custom type, using regex to make sure the input is valid, running custom functions/lambdas on the input to validate them, etc. (preCustom will be called before all other tests, postCustom will be called after all other tests).

```python
# Overcomplicated validator to validate hex numbers and convert them to integers
numberValidator = iv.Validator(
    type=lambda inp: int(inp.strip().lstrip("0x"), 16), # Converts strings to integers using base 16
    pattern=r"[0x]?[0-9]+", # Regex pattern for hex numbers
    preCustom=lambda inp: inp.strip().lstrip("0x").isnumeric() # Checks if the input is numeric
)
number = numberValidator.input("Enter a hex number: ") # Enter a hex number: 0x52
print("\nEntered:", number, type(number)) # Entered: 82 <class 'int'>
```

Heres a validator that turns user input into a boolean (the "type" lambda turns the input into a boolean, this lambda will be called after the input is validated, to convert the input string to a boolean, whatever the type function/lambda returns will be used as the output).

```python
boolValidator = iv.MultipleChoice(type=lambda inp: inp == "true", options=["true", "false"], caseSensitive=False)
userInput = boolValidator.input("(true/false): ")
```

The previous block of code is basically a better version of this (the "type" lambda will be called everytime the input method is called, while the next block of code runs the equality check manually, you'd have to do this everytime you call the input method, this is why using the "type" keyword argument is better).

```python
boolValidator = iv.MultipleChoice(options=["true", "false"], caseSensitive=False)
userInput = boolValidator.input("(true/false): ") == "true"
```
