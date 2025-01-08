#haha denary to binary converter
def denary_to_binary(denary_num):
    """
    turn a denary number to a binary number!!!! yaaaaaayyyyyy
    
    args:
        decimal_num (int): the chosen denary number
    
    returns:
        str: the binary version of the number
    """
    # if you put 0
    if denary_num == 0:
        return "0"
    
    # list for binary digits
    binary = []
    
    # absolute value for negative nellys
    num = abs(denary_num)
    
    # hawk tuah on it and turn it to denary
    while num > 0:
        # append remainder (0 or 1) to the list
        binary.insert(0, str(num % 2))
        # integer division by 2
        num //= 2
    
    # negative sign if original was negative
    if denary_num < 0:
        binary.insert(0, "-")
    
    # skibidi on list till it string
    return "".join(binary)

def main():
    while True:
        try:
            # user input
            denary_input = int(input("Enter a denary number to convert to binary (or enter 0 to exit): "))
            
            # exit condition
            if denary_input == 0:
                print("Exiting the program.")
                break
            
            # convert and display result
            binary_result = denary_to_binary(denary_input)
            print(f"Decimal {denary_input} in binary is: {binary_result}")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
# Alt method using built-in bin() function
def alternative_denary_to_binary(denary_num):
    """
    Convert decimal to binary using Python's built-in bin() function
    """
    return bin(denary_num)[2:]  # Remove '0b' prefix

if __name__ == "__main__":
    print("Denary to Binary Converter")
    main()