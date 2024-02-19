from App.calculations import add
import pytest

@pytest.mark.parametrize("num1,num2,res",[
    (3,2,5),
    (7,1,8),
    (3,0,3),
])

def test_add(num1,num2,res):
    print("testing add function")
    assert add(num1,num2) == res
