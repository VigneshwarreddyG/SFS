import random
import mysql.connector
class AccommodationDatabaseIterator:
    def __init__(self, cursor):
        self.cursor = cursor
        self.fetch_data()
        self.current_index = 0

    def fetch_data(self):
        self.cursor.execute("SELECT nameofcustomer, ApartmentDetails, members, location, movein FROM accomodationservice")
        self.accommodation_details = self.cursor.fetchall()

    def has_next(self):
        return self.current_index < len(self.accommodation_details)

    def next_accommodation_detail(self):
        if self.has_next():
            detail = self.accommodation_details[self.current_index]
            self.current_index += 1
            return detail
        else:
            return None
class ShuffleIterator:
    def __init__(self, accommodation_iterator):
        self.accommodation_iterator = accommodation_iterator
        self.shuffled_accommodations = random.sample(accommodation_iterator.accommodation_details, len(accommodation_iterator.accommodation_details))
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.shuffled_accommodations)

    def next_accommodation_detail(self):
        if self.has_next():
            detail = self.shuffled_accommodations[self.current_index]
            self.current_index += 1
            return detail
        else:
            return None

def apply_discount(payment_info):
    return f"{payment_info} - Discount Applied"
def display_customer_details(details):
    print("List of Customer Details:")
    for detail in details:
        print(f"Name: {detail[0]}, Apartment Details: {detail[1]}, Members: {detail[2]}, Location: {detail[3]}, Move-In: {detail[4]}")

# Example usage:
if __name__ == "__main__":
    # MySQL configuration
    mysql_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Saicharan@27",
        database="SFS"
    )
    cursor = mysql_conn.cursor()
    accommodation_iterator = AccommodationDatabaseIterator(cursor)
    print("Original Order:")
    while accommodation_iterator.has_next():
        print(accommodation_iterator.next_accommodation_detail())
    accommodation_iterator = AccommodationDatabaseIterator(cursor)
    shuffle_iterator = ShuffleIterator(accommodation_iterator)
    print("\nShuffled Order:")
    while shuffle_iterator.has_next():
        print(shuffle_iterator.next_accommodation_detail())    
    cursor.close()
    mysql_conn.close()
