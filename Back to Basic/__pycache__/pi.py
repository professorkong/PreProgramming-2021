import math
PI_STRING = "3.141592653589793238"
RED = "\x1B[31m"
GREEN = "\x1B[32m"
RESET = "\x1B[0m"
def main():
    """
    Here we simply call the functions which estimate pi using various methods
    """
    print("-----------------")
    print("| codedrome.com |")
    print("| Estimating Pi |")
    print("-----------------\n")
def print_as_text(pi):
    """
    Takes a value for pi and prints it below a definitive value,
    with matching digits in green and non-matching digits in red
    """
    pi_string = str("%1.18f" % pi)
    print("Definitive: " + PI_STRING)
    print("Estimated:  ", end="")
    for i in range(0, len(pi_string)):
        if pi_string[i] == PI_STRING[i]:

            print(GREEN +  pi_string[i] + RESET, end="")
        else:
            print(RED +  pi_string[i] + RESET, end="")
    print("\n") 
print_as_text()
