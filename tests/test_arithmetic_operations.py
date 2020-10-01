# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:27:50 2020

@author: Rajesh Sharma
"""
from functions import (check_datatype,
                       addition,
                       subtraction,
                       multiplication,
                       division)
import pytest

def test_check_datatype():
    num1, num2 = 2, 1
    e, first_num, second_num = check_datatype(num1, num2)
    return first_num, second_num

def test_addition():
    num1, num2 = test_check_datatype()
    test_add_result = addition(num1, num2)
    assert test_add_result == 3

def test_subtraction():
    num1, num2 = test_check_datatype()
    test_sub_result = subtraction(num1, num2)
    assert test_sub_result == 1

def test_multiplication():
    num1, num2 = test_check_datatype()
    test_mul_result = multiplication(num1, num2)
    assert test_mul_result == 2

def test_division():
    num1, num2 = test_check_datatype()
    test_div_result = division(num1, num2)
    assert test_div_result == 2