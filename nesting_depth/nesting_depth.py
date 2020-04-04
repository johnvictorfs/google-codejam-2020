def get_nesting(numbers, _open=0, text=''):
    if not numbers:
        # Final da string, fechar parenteses que restam ser fechados
        text += ')' * _open
        return text

    # Separar primeiro número passado dos restantes
    first, *rest = numbers
    first = int(first)

    # Abrir parenteses ainda necessários para o primeiro número, caso já não existam suficientes
    amount = max(_open, first) - min(_open, first)
    text += '(' * amount
    _open += amount

    # Adicionar o primeiro número passado
    text += str(first)

    for i in range(_open):
        if rest and str(first) == rest[0]:
            # Não abrir parenteses extras para números iguais consecutivos
            continue
        elif rest and int(first) > int(rest[0]):
            # Fechar parenteses suficientes já abertos quando o número atual é maior que o próximo
            amount = (_open - int(rest[0]))
            text += ')' * amount
            _open -= amount

            text += rest[0]
            first, *rest = rest
        elif rest and int(rest[0]) > int(first):
            # Abrir parenteses extras necessários para o próximo número quando ele for maior que o atual
            amount = int(rest[0]) - _open
            text += '(' * amount
            _open += amount
            text += rest[0]
            first, *rest = rest

    # Continuar com restante da String, mantendo valores já alterados
    return get_nesting(rest, _open, text)


def make_answer_string(index, numbers):
    answer = get_nesting(numbers)
    return 'Case #{}: {}'.format(index + 1, answer)


def nesting_depth():
    test_cases = int(input())

    for i in range(test_cases):
        numbers = input()
        print(make_answer_string(i, numbers))


if __name__ == '__main__':
    nesting_depth()
