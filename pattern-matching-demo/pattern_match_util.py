import re

''' function to match the phone no from 
    the input string and return it '''
def get_phone_no(input_data):
    pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
    phone_no = re.findall(pattern,input_data)
    return phone_no


''' function to match the email id from 
    the input string and return it '''
def get_email_id(input_data):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_id = re.findall(pattern,input_data)
    return email_id

''' function to match the order no from 
    the input string and return it '''
def get_order_no(input_data):
    pattern = r'order[^\d]*(\d*)'
    order_no = re.findall(pattern,input_data)
    return order_no