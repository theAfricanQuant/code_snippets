# Decorators


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Executed Before', original_function.__name__)
        result = original_function(*args, **kwargs)
        print('Executed After', original_function.__name__, '\n')
        return result
    return wrapper_function


@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')


display_info('John', 25)
display_info('Travis', 30)
