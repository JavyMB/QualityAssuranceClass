""" Hotel Class"""
from typing import List, Dict
from .base_model import BaseModel


class Hotel(BaseModel):
    """Class representing a hotel and its operations."""

    FILE_PATH = "hotels.json"

    def __init__(self, hotel_id: int, name: str, location: str, rooms: int):
        """Initialize a hotel instance.

        Args:
            hotel_id (int): Unique identifier for the hotel
            name (str): Name of the hotel
            location (str): Location of the hotel
            rooms (int): Number of rooms in the hotel
        """
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def to_dict(self) -> Dict:
        """Convert hotel instance to dictionary.

        Returns:
            Dict: Dictionary representation of the hotel
        """
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms,
            "reservations": self.reservations,
        }

    @classmethod
    def save_to_file(cls, hotels: List[Dict]) -> None:
        """Save hotels list to JSON file.

        Args:
            hotels (List[Dict]): List of hotel dictionaries to save
        """
        cls.save_file(hotels)

    @classmethod
    def load_from_file(cls) -> List[Dict]:
        """Load hotels from JSON file.

        Returns:
            List[Dict]: List of hotel dictionaries
        """
        return cls.load_file()

    @classmethod
    def create_hotel(cls, hotel_id: int, name: str, location: str,
                     rooms: int) -> None:
        """Create a new hotel and save it to file.

        Args:
            hotel_id (int): Unique identifier for the hotel
            name (str): Name of the hotel
            location (str): Location of the hotel
            rooms (int): Number of rooms in the hotel
        """
        hotels = cls.load_file()
        hotels.append({
            "hotel_id": hotel_id,
            "name": name,
            "location": location,
            "rooms": rooms,
            "reservations": []
        })
        cls.save_file(hotels)

    @classmethod
    def delete_hotel(cls, hotel_id: int) -> None:
        """Delete a hotel by its ID.

        Args:
            hotel_id (int): ID of the hotel to delete
        """
        hotels = cls.load_file()
        hotels = [h for h in hotels if h["hotel_id"] != hotel_id]
        cls.save_file(hotels)
