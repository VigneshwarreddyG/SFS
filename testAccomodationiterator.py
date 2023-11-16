
import pytest
from unittest.mock import patch
from Accomodationdesignpattern import AccommodationDatabaseIterator, ShuffleIterator, apply_discount, display_customer_details
@pytest.fixture
def mock_cursor():
    class MockCursor:
        def execute(self, query):
            pass
        def fetchall(self):
            return [
                ('John', '2BHK', 3, 'City A', '2023-11-01'),
                ('Alice', '1BHK', 2, 'City B', '2023-11-05'),
                ('Bob', '3BHK', 4, 'City C', '2023-11-10')
            ]
    return MockCursor()

def test_accommodation_database_iterator(mock_cursor):
    iterator = AccommodationDatabaseIterator(mock_cursor)
    assert iterator.has_next() is True
    assert iterator.next_accommodation_detail() == ('John', '2BHK', 3, 'City A', '2023-11-01')
    assert iterator.has_next() is True
    assert iterator.next_accommodation_detail() == ('Alice', '1BHK', 2, 'City B', '2023-11-05')

    assert iterator.has_next() is True
    assert iterator.next_accommodation_detail() == ('Bob', '3BHK', 4, 'City C', '2023-11-10')

    assert iterator.has_next() is False
    assert iterator.next_accommodation_detail() is None

def test_shuffle_iterator(mock_cursor):
    accommodation_iterator = AccommodationDatabaseIterator(mock_cursor)
    iterator = ShuffleIterator(accommodation_iterator)

    shuffled_accommodations = [
        ('Alice', '1BHK', 2, 'City B', '2023-11-05'),
        ('Bob', '3BHK', 4, 'City C', '2023-11-10'),
        ('John', '2BHK', 3, 'City A', '2023-11-01')
    ]
    assert iterator.has_next() is True
    assert iterator.next_accommodation_detail() in shuffled_accommodations
    assert iterator.has_next() is True
    assert iterator.next_accommodation_detail() in shuffled_accommodations
    assert iterator.has_next() is True
    assert iterator.next_accommodation_detail() in shuffled_accommodations
    assert iterator.has_next() is False
    assert iterator.next_accommodation_detail() is None

def test_display_customer_details(capfd):
    # Set up mock data
    customer_details = [
        ('John', '2BHK', 3, 'City A', '2023-11-01'),
        ('Alice', '1BHK', 2, 'City B', '2023-11-05'),
        ('Bob', '3BHK', 4, 'City C', '2023-11-10')
    ]
    # Call the function
    display_customer_details(customer_details)
    # Capture printed output
    captured = capfd.readouterr()
    # Check if the printed output matches the expected result
    expected_output = "List of Customer Details:\n" \
                      "Name: John, Apartment Details: 2BHK, Members: 3, Location: City A, Move-In: 2023-11-01\n" \
                      "Name: Alice, Apartment Details: 1BHK, Members: 2, Location: City B, Move-In: 2023-11-05\n" \
                      "Name: Bob, Apartment Details: 3BHK, Members: 4, Location: City C, Move-In: 2023-11-10\n"

    assert captured.out == expected_output
if __name__ == '__main__':
    pytest.main()
