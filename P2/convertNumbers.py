# pylint: disable=invalid-name
""" This program converts integers to binary and hexadecimal."""
import time
import sys
import os

def integer_to_binary(n):
    """Convert an integer to binary"""
    try:
        n = int(str(n), 0)  # Convert to integer
    except ValueError:
        return "#VALUE!"
    if n == 0:
        return "0"
    binary = ""
    if n < 0:
        n = (1 << 8) + n
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def integer_to_hexadecimal(n):
    """Convert an integer to hexadecimal"""
    try:
        n = int(str(n), 0)  # Convert to integer
    except ValueError:
        return "#VALUE!"
    hex_digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hex_value = ""
    if n < 0:
        n = (1 << 32) + n  # Handle negative numbers using two's complement (32-bit)
    while n > 0:
        remainder = n % 16
        hex_value = hex_digits[remainder] + hex_value
        n //= 16
    return hex_value

def process_file(file_path):
    """ Process a file and return valid data and errors """
    results = []
    errors=[]
    try:
        with open(file_path, 'r',encoding="utf-8") as file:
            for line_num, num in enumerate(file, start=1):
                try:
                    num = str(num).strip()
                    binary = integer_to_binary(num)
                    hexadecimal = integer_to_hexadecimal(num)
                    results.append((line_num,num, binary, hexadecimal))
                except ValueError:
                    errors.append(f"Error handled on line {line_num}: {num.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return results,errors

def main():
    """ Main function """
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Elapsed Time
    start_time = time.time()
    data, errors = process_file(file_path)

    if not data:
        print("Error: No valid data to process.")
        sys.exit(1)

    # Calculate Elapsed Time
    end_time = time.time()
    elapsed_time = end_time - start_time
    # Write results to file
    with open("ConvertionResults.txt", 'a',encoding="utf-8") as result_file:
        print(f"NUMBER  {file_name} BINARY  HEXADECIMAL")
        result_file.write(f"NUMBER  {file_name} BINARY  HEXADECIMAL\n")
        for line,num, binary, hexadecimal in data:
            print(f"{line} {num}   {binary}    {hexadecimal}")
            result_file.write(f"{line} {num}   {binary}    {hexadecimal}\n")
        print(f"Time Elapsed: {elapsed_time:.2f} seconds\n")
        result_file.write(f"\nTime Elapsed: {elapsed_time:.2f} seconds\n")

    # Print errors, if any
    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(error)

if __name__ == "__main__":
    main()
