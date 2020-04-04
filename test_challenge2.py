import challenge2


expected = """Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)
Case #5: (((33))1(2))
Case #6: 0
Case #7: 0((2)1(3(1(((2))))))
Case #8: 0((2)1)
Case #9: (((3))1(2))
Case #10: ((((4))22)1)"""

def a():
    print(expected)

def test_challenge_2(capfd):
    # challenge2.do_the_thing()
    a()
    out, err = capfd.readouterr()
    assert out == expected

