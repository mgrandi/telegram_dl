# single dispatch notes

be careful when calling them that you don't pass in the arguments using keyword arguments
or else it can't figure out the position of the argument to dispatch on

also, if you are using `@staticmethod` with your dispatcher, you need to only do `@staticmethod` on the method that you
annotate with `@singledispatchmethod` , but not the methods you annotate with `@func.register`

relevant bug reports

* "functools.singledispatchfunction has confusing error message if no position arguments are passed in"
** https://bugs.python.org/issue41122
* "functools: singledispatchmethod doesn't work with classmethod"
** https://bugs.python.org/issue39679
