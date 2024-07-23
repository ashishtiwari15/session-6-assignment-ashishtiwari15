from functools import wraps
import types

def closure_docstring_length(fn):
    """
    Closure to check if a function has a docstring of length greater than 50 characters.
    Input
    ------
        fn: Function to be checked
    Output
    ------
        A function that checks the docstring legth and returns a boolean response
    """
    test_free_var = 50
    if fn is None:
        raise ValueError("positional argument cannot be null: 'fn' ")
    def inner_function(*args, **kwargs):
        doc = fn.__doc__
        return doc is not None and len(doc.strip()) > test_free_var
    return inner_function

def get_next_fibonacci_number():
    """
    Closure to get next fibonacci number
    Input
    ------
        args: Optional Arguments for initializing base numbers
    Output
    ------
        A function that returns the next fibonacci number
    """
    num0, num1 = 0, 1
    def inner_function(*args):
        nonlocal num0, num1
        if len(args) > 0:
            if len(args) > 2:
                raise ValueError("Only two optional positional arguments allowed")
            elif len(args) < 2:
                raise ValueError("Atleast two optional positional arguments allowed")
            else:
                num0, num1 = args
        result = num0 + num1
        num0, num1 = num1, result
        return result
    return inner_function

def closure_count_function_calls(fn):
    """
    Closure to count the function calls 
    Input
    ------
        fn: input function to execute and count
    Output
    ------
        A function that returns the count of the currently called function
    """
    total_counts: dict = dict()
    if fn is None:
        raise ValueError("positional argument cannot be null: 'fn' ")
    @wraps(fn)
    def inner_function(*args, **kwargs):
        nonlocal total_counts
        function_name = fn.__name__
        total_counts[function_name] = total_counts[function_name] + 1 if function_name in total_counts.keys() else 1
        response = fn(*args, **kwargs)
        if function_name == '<lambda>':
            return f"Passed function is a lambda function. Such functions have been called {total_counts[function_name]} times and the last response was {response}"
        else:
            return f"Function {function_name} has been called {total_counts[function_name]} times and the last response was {response}"
    return inner_function

def closure_count_function_calls_updated(total_counts):
    """
    Closure to count the function calls based on dictionary passed as argument
    Input
    ------
        total_counts: dict => counter dictionary
        fn: input function to execute and count
    Output
    ------
        A function that returns the count of the currently called function
    """
    if not isinstance(total_counts, dict):
        raise TypeError("positional argument cannot be null: 'total_counts'")

    def wrapper(fn):
        if not callable(fn):
            raise TypeError("positional argument cannot be null: 'fn'")
        @wraps(fn)
        def inner_function(*args, **kwargs):
            function_name = fn.__name__
            total_counts[function_name] = total_counts[function_name] + 1 if function_name in total_counts.keys() else 1
            response = fn(*args, **kwargs)
            return response
        return inner_function
    return wrapper

total_counts: dict = dict()

@closure_count_function_calls_updated(total_counts=total_counts)
def lambda_test(x):
    return lambda y: x+y

func = lambda_test(3)
func(4)

print(total_counts)