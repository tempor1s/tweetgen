import time


def time_it(func):
    """
    A wrapper function that is used to get the time that a function takes
    Made with <3 by Ben Lafferty

    Use:
        @time_it
        def func():
            return 'hi'
    """
    # Made wth love by Ben <3 - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 1000) + ' ms')
        return result

    return wrapper
