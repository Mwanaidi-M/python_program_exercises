""" These are custom exception classes for practice.

Returns:
    The SalaryOutOfRange & SalaryOutOfRange1 Exception classes take args
"""

class CustomException(Exception):
    pass


# This class has a default arg so when an obj of this class is created, the 'msg' arg does not have to be specified.
class SalaryOutOfRange(Exception):

    def __init__(self, msg='sddddds'):
        self.msg = msg


    def __str__(self):
        return f'{self.msg}'

# This class has a positional arg so when an obj of this class is created, the 'msg' arg needs to be specified.
class SalaryOutOfRange1(Exception):

    def __init__(self, msg):
        self.msg = msg


    def __str__(self):
        return f'{self.msg}'
