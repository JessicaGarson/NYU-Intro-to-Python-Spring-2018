def number_formatted(phone_number):
    """Formats a phone number"""
    area_code = phone_number[0:3]
    second_part = phone_number[3:6]
    third_part = phone_number[6:]
    return '({})-{}-{}'.format(area_code, second_part, third_part)


# print(second_part)
print(number_formatted(phone_number="3017041328"))
