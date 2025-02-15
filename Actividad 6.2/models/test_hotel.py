""" Tes Hotel """
import unittest
from models.hotel import Hotel  # Assuming your classes are in hotel.py


class TestHotel(unittest.TestCase):
    """Unit Test Hotel."""

    def setUp(self):
        """Set up test environment."""
        # Clear the hotels file before each test
        Hotel.save_to_file([])

    def test_create_hotel(self):
        """Test creating a hotel."""
        Hotel.create_hotel(1, "Hotel A", "Location A", 10)
        hotels = Hotel.load_from_file()
        self.assertTrue(any(h["hotel_id"] == 1 for h in hotels))

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        Hotel.create_hotel(2, "Hotel B", "Location B", 20)
        Hotel.delete_hotel(2)
        hotels = Hotel.load_from_file()
        self.assertFalse(any(h["hotel_id"] == 2 for h in hotels))

    def test_create_multiple_hotels(self):
        """Test creating multiple hotels."""
        Hotel.create_hotel(3, "Hotel C", "Location C", 30)
        Hotel.create_hotel(4, "Hotel D", "Location D", 40)
        hotels = Hotel.load_from_file()
        self.assertTrue(any(h["hotel_id"] == 3 for h in hotels))
        self.assertTrue(any(h["hotel_id"] == 4 for h in hotels))

    def test_delete_nonexistent_hotel(self):
        """Test deleting a hotel that does not exist."""
        Hotel.create_hotel(5, "Hotel E", "Location E", 50)
        Hotel.delete_hotel(6)  # Hotel with ID 6 does not exist
        hotels = Hotel.load_from_file()
        self.assertTrue(any(h["hotel_id"] == 5 for h in hotels))

    def test_load_empty_file(self):
        """Test loading from an empty file."""
        hotels = Hotel.load_from_file()
        self.assertEqual(hotels, [])

    def test_save_and_load_hotels(self):
        """Test saving and loading hotels."""
        Hotel.create_hotel(7, "Hotel F", "Location F", 60)
        Hotel.create_hotel(8, "Hotel G", "Location G", 70)
        hotels = Hotel.load_from_file()
        self.assertEqual(len(hotels), 2)
        self.assertTrue(any(h["hotel_id"] == 7 for h in hotels))
        self.assertTrue(any(h["hotel_id"] == 8 for h in hotels))


if __name__ == "__main__":
    unittest.main()
