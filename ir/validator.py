__author__ = 'sarangis'

from ir.exceptions import *
from ir.types import *

class Validator:
    def validate(self):
        raise NotImplementedError("Validation method has to be implemented")

def decorator(func=None, **options):
    if func != None:
        # We received the function on this call, so we can define
        # and return the inner function
        def inner(*args, **kwargs):
            if len(options) > 0:
                print "Decorated function with options:"
            else:
                print "Decorated function without options!"

            for k, v in options.items():
                print "\t{}: {}".format(k, v)

            func(*args, **kwargs)

        return inner

    else:
        # We didn't receive the function on this call, so the return value
        # of this call will receive it, and we're getting the options now.
        def partial_inner(func):
            return decorator(func, **options)
        return partial_inner

@decorator
def function_a(x, y):
    print x + y

@decorator(foo="bar", baz=42)
def function_b(x, y):
    print x + y

def verify(decorated_func, **options):
    if decorated_func != None
        def wrapper(self, *args, **kw):
            for k, v in options.items():
                if not isinstance(k, v):
                    raise InvalidTypeException("Expected " + k + " to be of type: " + v.__class__.name)

        return wrapper

@verify(ftype=FunctionType)
def test_verify(ftype):
    pass