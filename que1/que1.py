# Question 1 (Python):
# Write a python function to give the frequency of digits appearing after the decimal place.
# give_remainder_dict(Dividend, Divisor, Number_of_Digits) -> dictionary with frequency of each
# digit after decimal point



# ---------------------------------Solution --------------------------------


# Create a function which returns a dictionary containing frequency of digits after decimal 
def give_remainder_dict(divident, divisor, n):
    
    dict  = {}                        # Initialize the empty dictionary
    
    # nserting 0-9 as keys with value 0 in dictionary
    for i in range(10): 
        dict[i]=0
    
    # Calculating n digits after decimal
    dig_after_dec = (f"{{:.{n+1}f}}".format(divident/divisor-int(divident/divisor)))[2:-1]
  
    
    # Iterating through every digit in 'dig_after_dec'
    for i in dig_after_dec:
        dict[int(i)] += 1;           # For each digit in 'dig_after_dec', increment the frequency in dictionary
    
    return dict                      # Return the dictionary
    
  
  
# Taking divident, divisor and n as input  
divident = int(input("Enter the value of Divident: "))
divisor = int(input("Enter the value of divisor: "))
n = int(input("Enter number of digits after decimal: "))

result = give_remainder_dict(divident, divisor, n)     # Calling give_remainder_dict function and passing values of divident, divisorand n and 
                                                       # storing output dictionary in result

print(result)                                          # Printing the result
