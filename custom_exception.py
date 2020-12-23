# To be able to use a user defined exception in another file [errors.py], you need to import it as a whole or
# import the Custom Exception classes in that file.

from errors import CustomException, SalaryOutOfRange, SalaryOutOfRange1

"""There are 3 examples showcasing how the 3 custom exception classes are being used.

Raises:
    CustomException: User is asked for a number and if the number is less than 2 then this exception is raised and an error msg is displayed.
    SalaryOutOfRange: User enters a salary, if the salary is not greater than 5000 and not less than 15000, this exception with a default arg is raised and the error msg is diplayed.
    SalaryOutOfRange1: User enters a salary, if the salary is not greater than 5000 and not less than 15000, this exception with a positional arg is raised and an error msg is displayed.
"""
sm = int(input('Gime me a number:\t'))

try:
    if sm < 2:
        raise CustomException
    else:
        print(sm)
except CustomException:
    print('someting wong')


salary = int(input('Enter your salary:\t'))

try:
    if not 5000 < salary < 15000:
        raise SalaryOutOfRange
except:
    sx = SalaryOutOfRange()
    print(sx)


salary1 = int(input('Enter your salary:\t'))

try:
    if not 5000 < salary1 < 15000:
        raise SalaryOutOfRange1
except:
    sx = SalaryOutOfRange1('SOMETIN WOOOOOONG')
    print(sx)