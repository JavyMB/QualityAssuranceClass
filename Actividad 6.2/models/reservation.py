""" Reservation Class"""
from typing import List, Dict
from .base_model import BaseModel


class Reservation(BaseModel):
    """Class for managing hotel reservations."""

    FILE_PATH = "reservations.json"

    def __init__(self, reservation_id: int, hotel_id: int, customer_id: int):
        """Initialize a reservation instance.

        Args:
            reservation_id (int): Unique identifier for the reservation
            hotel_id (int): ID of the hotel
            customer_id (int): ID of the customer
        """
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def to_dict(self) -> Dict:
        """Convert reservation instance to dictionary.

        Returns:
            Dict: Dictionary representation of the reservation
        """
        return {
            "reservation_id": self.reservation_id,
            "hotel_id": self.hotel_id,
            "customer_id": self.customer_id,
        }

    @classmethod
    def save_to_file(cls, reservations: List[Dict]) -> None:
        """Save reservations list to JSON file.

        Args:
            reservations (List[Dict]): List of reservation dictionaries to save
        """
        cls.save_file(reservations)

    @classmethod
    def load_from_file(cls) -> List[Dict]:
        """Load reservations from JSON file.

        Returns:
            List[Dict]: List of reservation dictionaries
        """
        return cls.load_file()

    @classmethod
    def create_reservation(cls, reservation_id: int, hotel_id: int,
                           customer_id: int) -> None:
        """Create a new reservation and save it to file.

        Args:
            reservation_id (int): Unique identifier for the reservation
            hotel_id (int): ID of the hotel
            customer_id (int): ID of the customers
        """
        reservations = cls.load_from_file()
        reservations.append({
            "reservation_id": reservation_id,
            "hotel_id": hotel_id,
            "customer_id": customer_id,
        })
        cls.save_file(reservations)

    @classmethod
    def cancel_reservation(cls, reservation_id: int) -> None:
        """Cancel a reservation by its ID.

        Args:
            reservation_id (int): ID of the reservation to cancel
        """
        reservations = cls.load_from_file()
        reservations = [r for r in reservations
                        if r["reservation_id"] != reservation_id]
        cls.save_file(reservations)
