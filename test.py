import math

def test_mod():
    assert(400%360==40)
    assert(-40%360==320)
    print(400%360)
    print(-40%360)
# test_mod()

def test_plot():
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4])
    plt.axis([-10, 10,- 10, 10])
    plt.ylabel('some numbers')
    plt.show()
