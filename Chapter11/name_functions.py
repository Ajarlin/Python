import unittest

def get_formatted_name(first, last):
    """ Generate a formatted name"""
    full_name = f"{first} {last}"
    return full_name.title()

if __name__ == '__main__':
    unittest.main()
