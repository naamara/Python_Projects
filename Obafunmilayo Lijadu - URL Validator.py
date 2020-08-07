import re
web_address = input('Enter the website url: ')
def validator(web_address):
    '''Function to validate an website address given certain conditions it must meet before it is called valid'''
    try:
        pattern = re.compile(r'^(http://|https://)?[www\.]?[a-zA-Z0-9_.-]+\.[a-z]+$')
        if re.search(pattern,web_address):
            return 'The website url is valid'
        else:
            return 'The website url is invalid'
    except:
        return 'Only strings are allowed'
print(validator(web_address))
