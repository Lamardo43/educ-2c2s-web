import datetime


def function_logger(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            function_name = func.__name__
            with open(file_path, 'a') as file:
                file.write(function_name + '\n')
                file.write(start_time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
                file.write(str(args) + '\n')
                file.write(str(kwargs) + '\n')

                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                file.write(str(result) + '\n')
                file.write(end_time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
                execution_time = end_time - start_time
                file.write(str(execution_time) + '\n\n')

            return result

        return wrapper

    return decorator


# Пример использования:

@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'


greeting_format('John')
