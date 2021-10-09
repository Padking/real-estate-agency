import phonenumbers


def get_normalized_phone_number(raw_phone_number: str, region='RU',
                                in_format=phonenumbers.PhoneNumberFormat.E164) -> str:
    try:
        phone_number = phonenumbers.parse(raw_phone_number, region=region)
    except phonenumbers.NumberParseException:
        phone_number = phonenumbers.phonenumber.PhoneNumber()

    possible_number = phonenumbers.is_possible_number(phone_number)
    valid_number = phonenumbers.is_valid_number(phone_number)
    if possible_number and valid_number:
        normalized_phone_number = phonenumbers.format_number(phone_number,
                                                             in_format)
        return normalized_phone_number
