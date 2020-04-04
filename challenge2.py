if __name__ != '__main__':
    # Mock input for tests
    index = 0

    with open('input2.txt') as f:
        input_data = [a.replace('\n', '') for a in f.readlines()]

    def input():
        global index
        index += 1
        return input_data[index - 1]

def get_nesting(numbers, _open=0, text=''):
    if not numbers:
        if _open:
            for i in range(_open):
                text += ')'
        return text

    first, *rest = numbers

    first = int(first)

    for i in range(max(_open, first) - min(_open, first)):
        text += '('
        _open += 1

    text += str(first)

    if not rest:
        for i in range(_open):
            text += ')'
        return text

    for i in range(_open):
        if rest and str(first) == rest[0]:
            continue
        elif rest and int(first) > int(rest[0]):
            for i in range(_open - int(rest[0])):
                text += ')'
                _open -= 1
                if _open == 0:
                    # Não fechar mais parenteses do que existem abertos
                    break
            # Adicionar previamente o próximo número, se for menor
            text += rest[0]
            first, *rest = rest
        elif rest and int(rest[0]) > int(first):
            # (((3))1)((2)) minha output
            # (((3))1(2)) output correta

            for i in range(_open):
                text += '('
                _open += 1
            text += rest[0]
            first, *rest = rest
        else:
            for i in range(_open):
                text += ')'
                _open -= 1

    return get_nesting(rest, _open, text)


def do_the_thing():
    test_cases = int(input())

    for i in range(test_cases):
        answer = get_nesting(input())
        end = '\n'
        if (i + 1) == test_cases:
            end = ''
        print('Case #{}: {}'.format(i + 1, answer), end=end)


if __name__ == '__main__':
    do_the_thing()
