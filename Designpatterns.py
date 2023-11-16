import random

from random import sample
class CarServiceBookingIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def has_next(self):
        return self.index < len(self.data)

    def next(self):
        if self.has_next():
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            return None

class FilterCarServiceBookingIterator:
    def __init__(self, data, condition):
        self.data = [item for item in data if condition(item)]
        self.index = 0

    def has_next(self):
        return self.index < len(self.data)

    def next(self):
        if self.has_next():
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            return None
        






# Sample data for car service booking details
car_service_data = [
    {'customer_name': 'John Doe', 'car_model': 'Sedan', 'payment_info': 'Credit Card', 'appointment_date': '2023-11-15', 'pickup_date': '2023-11-15', 'drop_time': '12:00 PM'},
    {'customer_name': 'Jane Smith', 'car_model': 'SUV', 'payment_info': 'PayPal', 'appointment_date': '2023-11-20', 'pickup_date': '2023-11-20', 'drop_time': '2:30 PM'}
]

# Original Order
print("Original Order of Car Service Booking Details:")
for data in car_service_data:
    print(data)

# Iterator
iterator = CarServiceBookingIterator(car_service_data)
while iterator.has_next():
    print(iterator.next())

# Filtered Order
filtered_iterator = FilterCarServiceBookingIterator(car_service_data, lambda x: x['customer_name'] == 'John Doe')
print("Filtered Car Service Booking Details:")
while filtered_iterator.has_next():
    print(filtered_iterator.next())


# CSS decorator generator based on customer type
class CSSDecorator:
    def __init__(self, base_style):
        self.base_style = base_style
        self.customer_styles = {}

    def add_customer_style(self, customer_type, style):
        self.customer_styles[customer_type] = style

    def generate_css(self, customer_type):
        css_content = self.base_style + self.customer_styles.get(customer_type, '')
        return css_content

# Example usage
base_style = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 20px;
    }
    /* Add other base styles here */
"""

css_decorator = CSSDecorator(base_style)

# Add styles for different customer types
css_decorator.add_customer_style('customer', """
    #customer-section {
        background-color: #ffc;
        border: 1px solid #faa;
    }
""")

css_decorator.add_customer_style('agent', """
    #agent-section {
        background-color: #cfc;
        border: 1px solid #afa;
    }
""")

css_decorator.add_customer_style('admin', """
    #admin-section {
        background-color: #ccf;
        border: 1px solid #aaf;
    }
""")

# Replace 'customer' with the actual customer type
customer_type = 'customer'
dynamic_css = css_decorator.generate_css(customer_type)

# Write CSS to a file
with open('dynamic_styles.css', 'w') as css_file:
    css_file.write(dynamic_css)



