# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:27:50 2020

@author: Rajesh Sharma

File Editing Versions::
    V.No.                              V.Desc                                 Modified Date
    v.0.1                   Added Check DataType Function                       04/10/2020
"""
from functions import (check_datatype,
                       addition,
                       subtraction,
                       multiplication,
                       division)
import sys, pytest

# Added check datatype function :: v.o.1  :: STARTS
@pytest.mark.datatype
def test_check_datatype():
    num1, num2 = 2, 1
    e, first_num, second_num = check_datatype(num1, num2)
    return first_num, second_num
# Added check datatype function :: v.o.1  :: ENDS

@pytest.mark.skip("Don't want to perform the addition test as it is already tested")
def test_addition():
    num1, num2 = test_check_datatype()
    test_add_result = addition(num1, num2)
    assert test_add_result == 3

@pytest.mark.skip("Don't want to perform the subtraction test as it is already tested")
@pytest.mark.arith
def test_subtraction():
    num1, num2 = test_check_datatype()
    test_sub_result = subtraction(num1, num2)
    assert test_sub_result == 1
    assert test_sub_result > 2

@pytest.mark.skipif(sys.version_info > (3, 3), reason="Don't want to run Multiplication test for Python version"
                                                      " greater than 3.3")
@pytest.mark.arith
def test_multiplication():
    num1, num2 = test_check_datatype()
    test_mul_result = multiplication(num1, num2)
    assert test_mul_result == 2

@pytest.mark.parametrize('num1, num2, result',
                         [
                             (5, 5, 1),
                             (14, 7, 2),
                             (8, 8, 1)
                         ])
@pytest.mark.arith
def test_division(num1, num2, result):
    # num1, num2 = test_check_datatype()
    test_div_result = division(num1, num2)
    assert test_div_result == result
    print('----o/p---',test_div_result, '------')