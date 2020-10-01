import add_2_nos

def test_add_2_nos():
    "Test that addition of two numbers works"
    num1 = 3
    num2 = 2
    add_result = add_2_nos.add_two_nos(num1,num2)

    assert add_result == 5
