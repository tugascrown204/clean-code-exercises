# Writing Tests Exercise
# Basic function to add two numbers

def add(a, b):
    return a + b

# Unit tests for the add function

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5

# Run the tests
if __name__ == '__main__':
    test_add()
    print('All tests passed!')