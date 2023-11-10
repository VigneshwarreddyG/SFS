import mysql.connector
import random

class FormDatabaseIterator:
    def __init__(self, form_details):
        self._form_details = form_details
        self._index = 0

    def has_next(self):
        return self._index < len(self._form_details)

    def next_form_detail(self):
        if self.has_next():
            self._index += 1
            return self._form_details[self._index - 1]
        else:
            return None

class ShuffleIterator:
    def __init__(self, form_iterator):
        self._form_iterator = form_iterator
        self._shuffled_forms = random.sample(self._form_iterator._form_details, len(self._form_iterator._form_details))
        self._index = 0

    def has_next(self):
        return self._index < len(self._form_iterator._form_details)

    def next_form_detail(self):
        if self.has_next():
            self._index += 1
            return self._shuffled_forms[self._index - 1]
        else:
            return None

class FilterByAppointmentDateIterator:
    def __init__(self, form_iterator, target_appointment_date):
        self._form_iterator = form_iterator
        self._target_appointment_date = target_appointment_date
        self._index = 0

    def has_next(self):
        while self._index < len(self._form_iterator._form_details):
            form_detail = self._form_iterator._form_details[self._index]
            if form_detail[3] == self._target_appointment_date:
                return True
            self._index += 1
        return False

    def next_form_detail(self):
        if self.has_next():
            form_detail = self._form_iterator._form_details[self._index]
            self._index += 1
            return form_detail
        else:
            return None

def apply_discount(payment_info):
    # Decorator function to add a discount to the payment information
    return f"Discount Applied: {payment_info}"

def display_customer_details(details):
    # Decorator function to display customer details
    print("List of Customer Details:")
    for detail in details:
        print(detail)

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="alexchilaka@2000",
        database="SFS"
    )

def get_all_bookings():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT car_model, payment_info, model_number, appointment_date FROM car_bookings")
    booking_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return booking_data

if __name__ == "_main_":
    booking_data = get_all_bookings()

    iterator = FormDatabaseIterator(booking_data)
    
    print("List of Customer Details:")
    while iterator.has_next():
        print(iterator.next_form_detail())

    shuffle_iterator = ShuffleIterator(iterator)
    print("\nShuffled Customer Details:")
    while shuffle_iterator.has_next():
        print(shuffle_iterator.next_form_detail())

    filter_iterator = FilterByAppointmentDateIterator(iterator, "2023-11-10")
    print("\nFiltered Customer Details (Appointment Date: 2023-11-10):")
    while filter_iterator.has_next():
        print(filter_iterator.next_form_detail())

    decorated_booking_data = []
    for booking in iterator._form_details:
        decorated_booking = booking[:2] + (apply_discount(booking[1]),) + booking[2:]
        decorated_booking_data.append(decorated_booking)
    display_customer_details(decorated_booking_data)