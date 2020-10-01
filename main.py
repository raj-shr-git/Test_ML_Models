# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:19:33 2020

@author: Rajesh Sharma
"""
import logging
logging.basicConfig(filename='main_file.log', filemode='w', level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")
try:
    logging.info(" Module Import Started ")
    from functions import (check_datatype,
                           addition,
                           subtraction,
                           multiplication,
                           division)
    import hello
except ImportError as ie:
    # Output expected ImportErrors
    logging.error(msg=ie.__class__.__name__  + " :: Missing Package --> " + ie.name)
except Exception as exception:
    # Output unexpected Exceptions
    logging.info("#### Exceptions other than ModuleImportError ####")
    logging.log(msg=(exception, False))
    logging.log(msg=exception.__class__.__name__ + " :: " + exception.name)

def main(num1, num2):
    add_result = addition(num1, num2)
    sub_result = subtraction(num1, num2)
    mul_result = multiplication(num1, num2)
    div_result = division(num1, num2)
    return add_result, sub_result, mul_result, div_result

if __name__ == "__main__":
    import sys
    # num1 = float(input("Enter the first number\n>"))
    # num2 = float(input("Enter the second number\n>"))
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    logging.info("#### User entered input numbers ####")
    dtype_result, first_num, second_num = check_datatype(num1, num2)
    logging.info("#### Datatype check performed on entered numbers ####")
    if dtype_result == 0:
        add_result, sub_result, mul_result, div_result = main(first_num, second_num)
        logging.info("#### Arithmetic Operations performed on input numbers ####")
        print(add_result, sub_result, mul_result, div_result)
    else:
        print(dtype_result.__class__.__name__ + " :: Wrong Input!! --> " + str(dtype_result))
        logging.error(msg=(dtype_result.__class__.__name__ + " :: Wrong Input!! --> " + str(dtype_result)))
        print("\nTry again with a different value!!")