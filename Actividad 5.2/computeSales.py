# pylint: disable=invalid-name
""" This program computes Total of Sales"""
import json
import sys
import time
import os


def load_json_file(filename):
    """Loads a JSON file and returns its content as a dictionary."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
        print(f"Error loading file {filename}: {e}")
        return None


def convert_price_catalogue(price_catalogue):
    """Converts the price catalogue from a list to a dictionary."""
    return {item["title"]: item["price"] for item in price_catalogue}


def compute_total_sales(price_catalogue, sales_record):
    """Computes the total cost of sales based on price catalogue."""
    total_cost = 0.0
    errors = []
    for sale in sales_record:
        product = sale.get("Product")
        quantity = sale.get("Quantity")
        if product not in price_catalogue:
            errors.append(f"Product '{product}' not found in price catalogue.")
            continue
        try:
            unit_price = float(price_catalogue[product])
            quantity = int(quantity)
            total_cost += unit_price * quantity
        except (ValueError, TypeError) as e:
            errors.append(f"Invalid data for product '{product}': {e}")
    return total_cost, errors


def main():
    """Main function to handle the command-line execution."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json sales.json")
        sys.exit(1)
    price_file = sys.argv[1]
    sales_file = sys.argv[2]
    file_name = os.path.splitext(os.path.basename(sales_file))[0]
    price_catalogue = load_json_file(price_file)
    sales_record = load_json_file(sales_file)
    if price_catalogue is None or sales_record is None:
        print("Error: One or both input files could not be processed.")
        sys.exit(1)
    price_catalogue = convert_price_catalogue(price_catalogue)
    start_time = time.time()
    total_cost, errors = compute_total_sales(price_catalogue, sales_record)
    elapsed_time = time.time() - start_time
    print("\nSales Report")
    print("=" * 40)
    print(f"TC: ${total_cost:.2f}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    if errors:
        print("\nErrors:")
        print("-" * 40)
        for error in errors:
            print(error)
    with open("SalesResults.txt", 'a', encoding='utf-8') as file:
        file.write(f"{file_name}: ${total_cost:.2f}\n")
        file.write(f"Execution Time: {elapsed_time:.4f} s\n")
        if errors:
            file.write("\nErrors:\n")
            file.write("-" * 40 + "\n")
            for error in errors:
                file.write(f"{error}\n")


if __name__ == "__main__":
    main()
