# Alternative method using built-in bin() function
def alternative_denary_to_binary(decimal_num):
    """
    Convert decimal to binary using Python's built-in bin() function
    """
    return bin(decimal_num)[2:]  # Remove '0b' prefix

if __name__ == "__main__":
    print("Decimal to Binary Converter")
    main()