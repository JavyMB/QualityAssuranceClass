""" Test Reservation """
import unittest
from models.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Unit Test for Reservation"""

    def test_create_reservation(self):
        """Test Create a Reservation"""
        Reservation.create_reservation(1, 1, 1)
        reservations = Reservation.load_from_file()
        self.assertTrue(any(r["reservation_id"] == 1 for r in reservations))

    def test_cancel_reservation(self):
        """Test Cancel reservation"""
        Reservation.create_reservation(2, 1, 1)
        Reservation.cancel_reservation(2)
        reservations = Reservation.load_from_file()
        self.assertFalse(any(r["reservation_id"] == 2 for r in reservations))


if __name__ == "__main__":
    unittest.main()
