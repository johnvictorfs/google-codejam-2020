def get_nesting(numbers, _open=0, text=''):
    if not numbers:
        # Final da string, fechar parenteses que restam ser fechados
        text += ')' * _open
        return text

    # Separar primeiro número passado dos restantes
    current, *rest = numbers
    current = int(current)

    # Abrir parenteses ainda necessários para o primeiro número, caso já não existam suficientes
    amount = max(_open, current) - min(_open, current)

    if not _open:
        text += '(' * amount
        _open += amount

    # Adicionar o primeiro número passado
    text += str(current)

    while(_open > 0):
        _next = None
        if rest:
            _next = int(rest[0])

        if _next is not None and current == _next:
            # Não abrir parenteses extras para números iguais consecutivos
            text += str(_next)
            current, *rest = rest
            current = int(current)
            continue
        elif _next is not None and current > _next:
            # Fechar parenteses suficientes já abertos quando o número atual é maior que o próximo
            amount = (_open - _next)
            text += ')' * amount
            _open -= amount
        elif _next is not None and _next > current:
            # Abrir parenteses extras necessários para o próximo número quando ele for maior que o atual
            amount = max(_next, _open) - min(_next, _open)
            text += '(' * amount
            _open += amount
        break

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
