# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:19:33 2020

@author: Rajesh Sharma
"""
import logging
logging.basicConfig(filename='main_file.log', filemode='a',level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

def check_datatype(numb1, numb2):
    try:
        num1, num2 = float(numb1), float(numb2)
        return 0, num1, num2
    except ValueError as ve:
        return ve, 0, 1

def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    try:
        num1/num2
    except ZeroDivisionError as zde:
        print("Your second number cannot be 0 for division")
        logging.error(msg="Denominator cannot be 0")
        return None
    return num1/num2