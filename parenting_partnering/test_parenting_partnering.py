import parenting_partnering

def test_overlaps():
    assert parenting_partnering.overlaps(
        (360, 480),
        (420, 540)
    ) == True

    assert parenting_partnering.overlaps(
        (420, 540),
        (600, 660)
    ) == False

    assert parenting_partnering.overlaps(
        (360, 480),
        (600, 660)
    ) == False

    assert parenting_partnering.overlaps(
        (0, 720),
        (720, 1440)
    ) == False

    assert parenting_partnering.overlaps(
        (0, 720),
        (710, 1440)
    ) == True


def reverse_all(text):
    # Each person in result can be reversed
    result = ''

    if text == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'

    for char in text:
        if char == 'J':
            result += 'C'
        else:
            result += 'J'

    return result


test_cases = [
    {
        'input': [(360, 480), (420, 540), (600, 660)],
        'output': 'CJC'
    },
    {
        'input': [(0, 1440), (1, 3), (2, 4)],
        'output': 'IMPOSSIBLE'
    },
    {
        'input': [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)],
        'output': 'JCCJJ'
    },
    {
        'input': [(0, 720), (720, 1440)],
        'output': 'CC'
    },
    {
        'input': [(1, 2), (3, 4), (4, 5), (5, 6)],
        'output': 'CCCC'
    },
    {
        'input': [(1, 2), (4, 5), (3, 4), (5, 6)],
        'output': 'JJJJ'
    },
    {
        'input': [(1,2), (1,2), (1,2)],
        'output': 'IMPOSSIBLE'
    },
    {
        'input': [(1,2), (1,2), (3, 4)],
        'output': 'JCJ'
    },
    {
        'input': [(0,1), (0,1), (0,1)],
        'output': 'IMPOSSIBLE'
    },
    {
        'input': [(0,1), (0,1)],
        'output': 'CJ'
    },
    {
        'input': [(2, 3), (3, 4), (4, 5), (5, 6)],
        'output': 'CCCC'
    }
]


def test_parenting_partnering():
    for case in test_cases:
        assert (
            parenting_partnering.get_match(case['input']) == case['output']
            or
            parenting_partnering.get_match(case['input']) == reverse_all(case['output'])
        )
