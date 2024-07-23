import pytest # type: ignore
import session6
import os
import inspect
import re
import random

def test_session5_readme_exists():
    """
    Test Case to check if README file exists in the repository scope.
    """
    assert os.path.isfile("README.md"), "Found README.md file"
    
def test_session5_readme_500_words():
    """
    Test Case to check if README file contains more than 500 words.
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words."
    
def test_session5_readme_file_for_more_than_10_hashes():
    """
    Test Case to check if README file contains more than 10 titles.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
    
def test_session5_indentations():
    """
    Test Case to check if the code file contains properly indented code blocks
    """
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for index, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations. {index}-{len(space)}"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_session5_function_name_had_cap_letter():
    """ 
    Test Case to check if all functions of the code file have small letters only.
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_session6_closure_docstring_length_no_args():
    """ 
        Test closure_docstring_length with no arguments
    """
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        session6.closure_docstring_length()

def test_session6_closure_docstring_length_invalid_args():
    """ 
        Test closure_docstring_length with invalid arguments
    """
    with pytest.raises(ValueError, match=r".*cannot be null: 'fn'*"):
        session6.closure_docstring_length(None)

def test_closure_docstring_length():
    """
    Test Case to check normal execution of a closure that checks if the function passed to it has a docstring of greater than 50 characters
    """
    def my_func_positive():
        """
        This is a test function that shall be passed to the closure_docstring_length function.
        This is a positive flow function.
        """
        pass
    
    def my_func_negative():
        """
        Negative test function
        """
        pass
    positive_func_var = session6.closure_docstring_length(my_func_positive)
    negative_func_var = session6.closure_docstring_length(my_func_negative)
    assert True == positive_func_var(), "closure_docstring_length function failing for normal execution in positive flow"
    assert False == negative_func_var(), "closure_docstring_length function failing for normal execution in negative flow"
    
def test_closure_docstring_length_no_docstring():
    simple_lambda_function = lambda x: x ** 2
    lambda_function_var = session6.closure_docstring_length(simple_lambda_function)
    assert False == lambda_function_var(), "closure_docstring_length failed for a function with no docstring."
    
def test_get_next_fibonacci_number_validation():
    fibonacci_var = session6.get_next_fibonacci_number()
    
    with pytest.raises(ValueError, match=r".*Only two optional positional arguments allowed*"):
        fibonacci_var(5, 8, 13)
        
    with pytest.raises(ValueError, match=r".*Atleast two optional positional arguments allowed*"):
        fibonacci_var(5)
    
def test_get_next_fibonacci_number():
    """
    Test case to check next fibonacci number
    """
    fibonacci_var = session6.get_next_fibonacci_number()
    assert 1 == fibonacci_var(), "get_next_fibonacci_number failing for first number"
    assert 2 == fibonacci_var(), "get_next_fibonacci_number failing for second number"
    assert 3 == fibonacci_var(), "get_next_fibonacci_number failing for third number"
    assert 5 == fibonacci_var(), "get_next_fibonacci_number failing for fourth number"
    assert 8 == fibonacci_var(), "get_next_fibonacci_number failing for fifth number"
    
def test_get_next_fibonacci_number_custom_args():
    """
    Test case to check next fibonacci number with custom args
    """
    fibonacci_var = session6.get_next_fibonacci_number()
    assert 13 == fibonacci_var(5, 8), "get_next_fibonacci_number failing for custom initialized arguments"
    assert 21 == fibonacci_var(), "get_next_fibonacci_number failing for next value of custom initialized arguments"
    
def test_closure_count_function_calls():
    """
    Test case to check count of each passed function
    """
    def add(*args):
        return sum(args)
    
    def sub(a, b):
        return a-b
    
    def mult(a, b):
        return a*b
    
    sample_lambda = lambda x: x**2
    
    add_function_var = session6.closure_count_function_calls(add)
    sub_function_var = session6.closure_count_function_calls(sub)
    mult_function_var = session6.closure_count_function_calls(mult)
    lambda_function_var = session6.closure_count_function_calls(sample_lambda)
    
    response1 = add_function_var(1, 2, 3)
    response2 = sub_function_var(3, 2)
    response3 = mult_function_var(2, 5)
    response4 = lambda_function_var(4)
    
    assert response1 == "Function add has been called 1 times and the last response was 6", "function closure_count_function_calls not working for normal condition"
    assert response2 == "Function sub has been called 1 times and the last response was 1", "function closure_count_function_calls not working for normal condition"
    assert response3 == "Function mult has been called 1 times and the last response was 10", "function closure_count_function_calls not working for normal condition"
    assert response4 == "Passed function is a lambda function. Such functions have been called 1 times and the last response was 16", "function closure_count_function_calls not working for normal condition"
    
def test_closure_count_function_calls_addition():
    """
    Test case to check count of each passed function
    """
    def add(*args):
        return sum(args)
    
    add_function_var = session6.closure_count_function_calls(add)
    last_arguments, response = [], ""
    for x in range(1, 11):
        random_args = [random.randint(1, 100 - 1) for _ in range(x+1)]
        response = add_function_var(*random_args)
        last_arguments = random_args if x == 10 else []
    expected_response = f"Function {add.__name__} has been called 10 times and the last response was {sum(last_arguments)}"
    assert response == expected_response, "function closure_count_function_calls not working for multiple iterative loops"
    
def test_closure_count_function_calls_subtraction():
    """
    Test case to check count of each passed function
    """
    def sub(a, b):
        return a - b
    
    sub_function_var = session6.closure_count_function_calls(sub)
    last_a, last_b, response = 0, 0, ""
    for x in range(1, 11):
        a, b = random.randint(1, 100), random.randint(1, 100)
        response = sub_function_var(a, b)
        if x == 10:
            last_a, last_b = a, b
    expected_response = f"Function {sub.__name__} has been called 10 times and the last response was {last_a - last_b}"
    assert response == expected_response, "function closure_count_function_calls not working for multiple iterative loops"
    
def test_closure_count_function_calls_multiplication():
    """
    Test case to check count of each passed function
    """
    def mult(a, b):
        return a * b
    
    mult_function_var = session6.closure_count_function_calls(mult)
    last_a, last_b, response = 0, 0, ""
    for x in range(1, 11):
        a, b = random.randint(1, 100), random.randint(1, 100)
        response = mult_function_var(a, b)
        if x == 10:
            last_a, last_b = a, b
    expected_response = f"Function {mult.__name__} has been called 10 times and the last response was {last_a * last_b}"
    assert response == expected_response, "function closure_count_function_calls not working for multiple iterative loops"
    
def test_closure_count_function_calls_lambda():
    """
    Test Case to to check count of each lambda function called
    """
    sample_lambda_square = lambda x: x ** 2
    sample_lambda_cube = lambda x: x ** 3
    sample_lambda_sqrt = lambda x: x ** 0.5
    
    control_dict = {
        sample_lambda_square: session6.closure_count_function_calls(sample_lambda_square),
        sample_lambda_cube: session6.closure_count_function_calls(sample_lambda_cube),
        sample_lambda_sqrt: session6.closure_count_function_calls(sample_lambda_sqrt),
    }
    
    count_dict = {}
    
    func_list = [sample_lambda_square, sample_lambda_cube, sample_lambda_sqrt]
    last_func, last_arg, response = None, 0, 0
    for x in range(1, 11):
        random_arg = random.randint(1, 100)
        random_func = random.choice(func_list)
        lambda_func_var = control_dict[random_func]
        response = lambda_func_var(random_arg)
        count_dict[random_func] = count_dict[random_func] + 1 if random_func in count_dict.keys() else 1
        if x == 10:
            last_func, last_arg = random_func, random_arg
    expected_response = f"Passed function is a lambda function. Such functions have been called {count_dict[last_func]} times and the last response was {last_func(last_arg)}"
    assert response == expected_response, "function closure_count_function_calls not working for multiple iterative loops"

def test_closure_count_function_calls_validations():
    """ 
        Test closure_count_function_calls with no arguments
    """
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        session6.closure_count_function_calls()

def test_closure_count_function_calls_invalid_args():
    """ 
        Test closure_count_function_calls with none arguments
    """
    with pytest.raises(ValueError, match=r".*positional argument cannot be null: 'fn'*"):
        session6.closure_count_function_calls(None)

def test_closure_count_function_calls_updated_validations():
    """ 
        Test losure_count_function_calls_updated with no arguments
    """
    with pytest.raises(TypeError, match=r".*required positional argument: 'total_counts'*"):
        session6.closure_count_function_calls_updated()
        
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        function_var = session6.closure_count_function_calls_updated({"add": 0})
        function_var()

def test_closure_count_function_calls_updated_invalid_args():
    """ 
        Test closure_count_function_calls_updated with none arguments
    """
    with pytest.raises(TypeError, match=r".*positional argument cannot be null: 'total_counts'*"):
        session6.closure_count_function_calls_updated(None)

    with pytest.raises(TypeError, match=r".*positional argument cannot be null: 'fn'*"):
        function_var = session6.closure_count_function_calls_updated({"add": 0})
        function_var(None)

def test_closure_count_function_calls_updated():
    """
    Test Case for generic checks for closure_count_function_calls_updated
    """
    total_counts: dict = dict()
    
    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def add(*args):
        return sum(args)

    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def sub(a:int, b:int):
        return a-b

    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def div(a, b):
        if b==0:
            raise ZeroDivisionError("Cannot divide by 0")
        else:
            return a/b

    response_add = add(2, 3, 4)
    response_sub = sub(3, 1)
    response_div = div(4, 2)
    
    expected_dict: dict = {
        'add': 1,
        'sub': 1,
        'div': 1
    }

    assert expected_dict == total_counts, "closure_count_function_calls_updated function failing for generic tests"

def test_closure_count_function_calls_updated_multiple_runs():
    """
    Testing closure_count_function_calls_updated for multiple runs
    """
    total_counts: dict = dict()
    
    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def add(*args):
        return sum(args)

    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def sub(a:int, b:int):
        return a-b

    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def div(a, b):
        if b==0:
            raise ZeroDivisionError("Cannot divide by 0")
        else:
            return a/b
    
    random_count_1 = random.randint(1, 10)
    random_count_2 = random.randint(15, 20)
    random_count_3 = random.randint(50, 70)
    
    for _ in range(random_count_1):
        add(50, 50, 90)
    
    for _ in range(random_count_2):
        sub(70, 30)
    
    for _ in range(random_count_3):
        div(30, 60)

    expected_counts: dict = {
        'add': random_count_1,
        'sub': random_count_2,
        'div': random_count_3
    }
    
    assert total_counts == expected_counts, "closure_count_function_calls_updated function failing for multiple iteration tests"
    
def test_closure_count_function_calls_updated_lambda_func():
    """
    Testing closure_count_function_calls_updated function for lambda function
    """
    total_counts: dict = dict()
    
    @session6.closure_count_function_calls_updated(total_counts=total_counts)
    def lambda_complex_number(x: int):
        return lambda y: complex(x, y)
    
    response = lambda_complex_number(3)
    response(2)
    
    expected_counts: dict = {
        lambda_complex_number.__name__: 1
    }
    
    assert total_counts == expected_counts, "closure_count_function_calls_updated function failing for lambda functions"