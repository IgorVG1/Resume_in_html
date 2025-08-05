def abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    abs1()
    abs2()
    print("Everything passed")