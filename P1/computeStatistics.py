# pylint: disable=invalid-name
"""
This Program executes input data from a .txt file and calculates:
Mean , Median, Mode, Variance, Standard Deviation and Elapsed Time
"""

import sys
import time
import os
def calculate_mean(data):
    """ Calculate Mean of a list of numbers """
    return sum(data) / len(data)

def calculate_median(data):
    """ Calculate Median of a list of numbers """
    data_sorted = sorted(data)
    n = len(data_sorted)
    if n % 2 == 0:
        return (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    return data_sorted[n // 2]

def calculate_mode(data):
    """ Calculate Mode of a list of numbers """
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    max_count = max(frequency.values())
    mode_values = [key for key, count in frequency.items() if count == max_count]
    if len(mode_values) == 1:
        return mode_values[0]
    return mode_values[0]

def calculate_variance(data):
    """ Calculate Variance of a list of numbers """
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std_deviation(data):
    """ Calculate Standard Deviation of a list of numbers """
    return calculate_variance(data) ** 0.5

def process_file(file_path):
    """ Process a file and return valid data and errors """
    valid_data = []
    errors = []

    try:
        with open(file_path, 'r',encoding="utf-8") as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    valid_data.append(float(line.strip()))
                except ValueError:
                    errors.append(f"Error -> {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    count = len(valid_data)+len(errors)
    return valid_data, errors,count

def main():
    """ Main function """
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    # Elapsed Time
    start_time = time.time()
    data, errors, count = process_file(file_path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    if not data:
        print("Error: No valid data to process.")
        sys.exit(1)
    # Calculate statistics
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data)
    std_deviation = calculate_std_deviation(data)

    # Calculate Elapsed Time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print results
    print(f"Descriptive Statistics:{file_name}")
    print(f"MEAN: {mean:f}")
    print(f"MEDIAN: {median:f}")
    print(f"MODE: {mode:f}")
    print(f"VARIANCE: {variance:f}")
    print(f"SD: {std_deviation:f}")
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")

    # Write results to file
    with open("StatisticsResults.txt", 'a',encoding="utf-8") as result_file:
        result_file.write(f"\n{file_name}:\n")
        result_file.write(f"COUNT: {count}\n")
        result_file.write(f"MEAN: {mean:f}\n")
        result_file.write(f"MEDIAN: {median:f}\n")
        result_file.write(f"MODE: {mode:f}\n")
        result_file.write(f"AD: {std_deviation:f}\n")
        result_file.write(f"VARIANCE: {variance:f}\n")
        result_file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")

    # Print errors, if any
    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(error)

if __name__ == "__main__":
    main()
