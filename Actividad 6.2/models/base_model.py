""" Base Model"""
import json
import os
from typing import List, Dict


class BaseModel:
    """Base class for file operations"""
    FILE_PATH = ""  # Should be overridden by child classes

    @classmethod
    def load_file(cls) -> List[Dict]:
        """Helper method to load data from JSON file.

        Returns:
            List[Dict]: List of dictionaries
        """
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Error reading {cls.FILE_PATH}. Initializing empty list.")
            return []

    @classmethod
    def save_file(cls, data: List[Dict]) -> None:
        """Save data to JSON file.

        Args:
            data (List[Dict]): List of dictionaries to save
        """
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
