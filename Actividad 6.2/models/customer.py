""" Customer Class"""
from typing import List, Dict
from .base_model import BaseModel


class Customer(BaseModel):
    """Class representing a customer and their operations."""

    FILE_PATH = "customers.json"

    def __init__(self, customer_id: int, name: str, email: str):
        """Initialize a customer instance.

        Args:
            customer_id (int): Unique identifier for the customer
            name (str): Customer's full name
            email (str): Customer's email address
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict:
        """Convert customer instance to dictionary.

        Returns:
            Dict: Dictionary representation of the customer
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def save_to_file(cls, customers: List[Dict]) -> None:
        """Save customers list to JSON file.

        Args:
            customers (List[Dict]): List of customer dictionaries to save
        """
        cls.save_file(customers)

    @classmethod
    def load_from_file(cls) -> List[Dict]:
        """Load hotels from JSON file.

        Returns:
            List[Dict]: List of hotel dictionaries
        """
        return cls.load_file()

    @classmethod
    def create_customer(cls, customer_id: int, name: str, email: str) -> None:
        """Create a new customer and save it to file.

        Args:
            customer_id (int): Unique identifier for the customer
            name (str): Customer's full name
            email (str): Customer's email address
        """
        customers = cls.load_from_file()
        customers.append({
            "customer_id": customer_id,
            "name": name,
            "email": email,
        })
        cls.save_file(customers)

    @classmethod
    def delete_customer(cls, customer_id: int) -> None:
        """Delete a customer by their ID.

        Args:
            customer_id (int): ID of the customer to delete
        """
        customers = cls.load_from_file()
        customers = [c for c in customers if c["customer_id"] != customer_id]
        cls.save_file(customers)
