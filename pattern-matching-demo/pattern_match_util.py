import re
def get_phone_no(input_data):
    pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
    phone_no = re.findall(pattern,input_data)
    return phone_no