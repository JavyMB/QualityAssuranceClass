""" Test Customer """
import unittest
from models.customer import Customer


class TestCustomer(unittest.TestCase):
    """Unit tests for the Customer class."""

    def setUp(self):
        """Set up test environment."""
        # Clear the customer file before each test
        Customer.save_to_file([])

    def test_create_customer(self):
        """Test customer creation and storage in file."""
        Customer.create_customer(1, "John Doe", "john@example.com")
        customers = Customer.load_from_file()
        self.assertTrue(any(c["customer_id"] == 1 for c in customers))

    def test_delete_customer(self):
        """Test customer deletion from file."""
        Customer.create_customer(2, "Jane Doe", "jane@example.com")
        Customer.delete_customer(2)
        customers = Customer.load_from_file()
        self.assertFalse(any(c["customer_id"] == 2 for c in customers))

    def test_create_multiple_customers(self):
        """Test creation of multiple customers."""
        Customer.create_customer(3, "Alice Smith", "alice@example.com")
        Customer.create_customer(4, "Bob Brown", "bob@example.com")
        customers = Customer.load_from_file()
        self.assertTrue(any(c["customer_id"] == 3 for c in customers))
        self.assertTrue(any(c["customer_id"] == 4 for c in customers))

    def test_delete_nonexistent_customer(self):
        """Test deletion of a customer that does not exist."""
        Customer.create_customer(5, "Charlie Black", "charlie@example.com")
        Customer.delete_customer(6)  # ID 6 does not exist
        customers = Customer.load_from_file()
        self.assertTrue(any(c["customer_id"] == 5 for c in customers))

    def test_load_empty_file(self):
        """Test loading from an empty file."""
        customers = Customer.load_from_file()
        self.assertEqual(customers, [])

    def test_save_and_load_customers(self):
        """Test saving and loading customers."""
        customers = [
            {"customer_id": 7, "name": "David White",
             "email": "david@example.com"},
            {"customer_id": 8, "name": "Eva Green",
             "email": "eva@example.com"},
        ]
        Customer.save_to_file(customers)
        loaded_customers = Customer.load_from_file()
        self.assertEqual(customers, loaded_customers)

    def test_update_customer(self):
        """Test updating an existing customer."""
        Customer.create_customer(9, "Frank Blue", "frank@example.com")
        customers = Customer.load_from_file()
        for customer in customers:
            if customer["customer_id"] == 9:
                customer["name"] = "Frank Red"
                customer["email"] = "frank.red@example.com"
        Customer.save_to_file(customers)
        updated_customers = Customer.load_from_file()
        self.assertTrue(any(c["name"] == "Frank Red"
                            for c in updated_customers))
        self.assertTrue(any(c["email"] == "frank.red@example.com"
                            for c in updated_customers))

    def test_create_customer_with_existing_id(self):
        """Test creating a customer with an existing ID."""
        # Create initial customer
        Customer.create_customer(10, "Grace Yellow", "grace@example.com")
        # Get initial count
        customers_before = Customer.load_from_file()
        initial_count = len(customers_before)
        # Try to create customer with same ID
        Customer.create_customer(10, "Grace Blue", "grace.blue@example.com")
        # Get count after attempted duplicate creation
        customers_after = Customer.load_from_file()
        final_count = len(customers_after)
        # Verify count increased by 1
        self.assertEqual(final_count, initial_count + 1)
        # Verify we have exactly 2 customers with ID 10
        customers_with_id_10 = [
            c for c in customers_after if c["customer_id"] == 10]
        self.assertEqual(len(customers_with_id_10), 2)
        # Verify both customers exist
        self.assertTrue(any(
            c["email"] == "grace@example.com"
            for c in customers_with_id_10))
        self.assertTrue(any(
            c["email"] == "grace.blue@example.com"
            for c in customers_with_id_10))


if __name__ == "__main__":
    unittest.main()
