import nesting_depth

test_cases = {
    '0000': '0000',
    '101': '(1)0(1)',
    '111000': '(111)000',
    '1': '(1)',
    '021': '0((2)1)',
    '312': '(((3))1(2))',
    '4': '((((4))))',
    '221': '((22)1)',
    '99122': '(((((((((99))))))))1(22))',
    '4444': '((((4444))))',
    '004444': '00((((4444))))',
    '440044': '((((44))))00((((44))))',
    '99999': '(((((((((99999)))))))))'
}


def test_output_challenge_2():
    for _input, output in test_cases.items():
        assert nesting_depth.get_nesting(_input) == output


def test_text_output_challenge_2():
    for index, (_input, output) in enumerate(test_cases.items()):
        assert nesting_depth.make_answer_string(index, _input) == f'Case #{index + 1}: {output}'
