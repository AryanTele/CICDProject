from src.mathop import add,sub

def test_add():
    assert add(0,0) == 0
    assert add(1,14) == 15
    assert add(3,0) == 3
    assert add(-4,14) == 10
    assert add(0,0) == 0
    assert add(1,-14) == -13
    assert add(3,0) == 3
    assert add(4,14) == 18 
    
def test_sub():
    assert sub(0,0) == 0
    assert sub(1,14) == -13
    assert sub(3,0) == 3
    assert sub(-4,14) == -18
    assert sub(0,0) == 0
    assert sub(1,-14) == 15 