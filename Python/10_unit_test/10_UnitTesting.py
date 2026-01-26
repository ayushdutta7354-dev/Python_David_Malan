# Unit Testing:

from misc_10 import square;
import pytest;

print(square(10));
square(5);


def main():
    test_square();
    test_positive();
    test_negative();

def test_square():
    try:
        assert square(2) == 4;
    except:
        print("Assertion Error for 2 sqaured not 4");
    try:
        assert square(5) == 9;
    except:
        print("Assertion Error for 3 sqaured not 9");


# aliter:

def test_positive():
    assert square(2) == 4;
    assert square(3) == 9;


def test_negative():
    assert square(-2) == 4;
    assert square(-3) == 9;


def test_zero():
    assert square(0) == 0;

def test_str():
    with pytest.raises(TypeError):
        square("cat");

if __name__ == "__main__":
    main();

# we can make diff files for testing different fn in a file.