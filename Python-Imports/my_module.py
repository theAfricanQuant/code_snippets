
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    return next((i for i, value in enumerate(to_search) if value == target), -1)
