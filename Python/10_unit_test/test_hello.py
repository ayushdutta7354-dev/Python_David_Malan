
from hello import hello;



def test_hello():
    assert hello("Ayush") == "hello, Ayush";

def test_hello_2():
    assert hello("David") == "hello, David";

def test_hello_3():
    assert hello("Suresh") == "hello, David";

def test_default():
    assert hello() == "hello, World";

