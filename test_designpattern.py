
import pytest
from Db_Operations import FormDatabaseIterator,ShuffleIterator,FilterByAppointmentDateIterator,apply_discount,display_customer_details
def test_form_database_iterator():
    form_details = [('Car1', 'Payment1', 'Model1', '2023-11-01'),
                    ('Car2', 'Payment2', 'Model2', '2023-11-02'),
                    ('Car3', 'Payment3', 'Model3', '2023-11-03')]

    form_iterator = FormDatabaseIterator(form_details)
    assert form_iterator.has_next() == True
    assert form_iterator.next_form_detail() == ('Car1', 'Payment1', 'Model1', '2023-11-01')
    assert form_iterator.has_next() == True
    assert form_iterator.next_form_detail() == ('Car2', 'Payment2', 'Model2', '2023-11-02')
    assert form_iterator.has_next() == True
    assert form_iterator.next_form_detail() == ('Car3', 'Payment3', 'Model3', '2023-11-03')
    assert form_iterator.has_next() == False
    assert form_iterator.next_form_detail() == None

test_form_database_iterator()

def test_shuffle_iterator():
    form_details = [('Car1', 'Payment1', 'Model1', '2023-11-01'),
                    ('Car2', 'Payment2', 'Model2', '2023-11-02'),
                    ('Car3', 'Payment3', 'Model3', '2023-11-03')]

    form_iterator = FormDatabaseIterator(form_details)
    shuffle_iterator = ShuffleIterator(form_iterator)
    assert shuffle_iterator.has_next() == True
    shuffled_form = shuffle_iterator.next_form_detail()
    assert shuffled_form in form_details
    assert shuffle_iterator.has_next() == True
    shuffled_form = shuffle_iterator.next_form_detail()
    assert shuffled_form in form_details
    assert shuffle_iterator.has_next() == True
    shuffled_form = shuffle_iterator.next_form_detail()
    assert shuffled_form in form_details
    assert shuffle_iterator.has_next() == False
    assert shuffle_iterator.next_form_detail() == None

test_shuffle_iterator()

def test_filter_by_appointment_date_iterator():
    form_details = [('Car1', 'Payment1', 'Model1', '2023-11-01'),
                    ('Car2', 'Payment2', 'Model2', '2023-11-02'),
                    ('Car3', 'Payment3', 'Model3', '2023-11-03'),
                    ('Car4', 'Payment4', 'Model4', '2023-11-01')]

    form_iterator = FormDatabaseIterator(form_details)

    filter_iterator = FilterByAppointmentDateIterator(form_iterator, '2023-11-01')
    assert filter_iterator.has_next() == True
    assert filter_iterator.next_form_detail() == ('Car1', 'Payment1', 'Model1', '2023-11-01')
    assert filter_iterator.has_next() == True
    assert filter_iterator.next_form_detail() == ('Car4', 'Payment4', 'Model4', '2023-11-01')
    assert filter_iterator.has_next() == False
    assert filter_iterator.next_form_detail() == None

test_filter_by_appointment_date_iterator()

def test_apply_discount_decorator():
    payment_info = "Sample Payment Info"
    discounted_payment = apply_discount(payment_info)
    
    assert isinstance(discounted_payment, str)
    assert "Discount Applied" in discounted_payment

def test_display_customer_details_decorator(capfd):
    details = [("John Doe", "Toyota", "Paid", "12345", "2023-11-10")]
    display_customer_details(details)
    captured = capfd.readouterr()
    
    assert "List of Customer Details:" in captured.out
    assert "John Doe" in captured.out
    assert "Toyota" in captured.out
    assert "Paid" in captured.out
    assert "12345" in captured.out
    assert "2023-11-10" in captured.out

