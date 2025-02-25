def overlaps(a, b):
    a_start, a_end = a
    b_start, b_end = b
    
    return a_end > b_start and b_end > a_start


def get_match(acts):
    periods = {'C': [], 'J': []}
    impossible = 'IMPOSSIBLE'
    result = ''

    for period in acts:
        overlaps_c = False
        overlaps_j = False

        # Add activity to first available if it doesn't overlap with one of the
        # ones they are already doing
        for added_period in periods['C']:
            if overlaps(added_period, period):
                overlaps_c = True
        for added_period in periods['J']:
            if overlaps(added_period, period):
                overlaps_j = True

        if overlaps_c and overlaps_j:
            # At least one activity can't be done by either
            return impossible
        elif not overlaps_c:
            # Assign to C
            periods['C'].append(period)
            result += 'C'
        elif not overlaps_j:
            # Assign to J
            periods['J'].append(period)
            result += 'J'

    return result


def parenting_partnering():
    test_cases = int(input())

    for i in range(test_cases):
        activities = int(input())
        acts = []

        for _ in range(activities):
            a1, a2 = input().split(' ')
            a1, a2 = int(a1), int(a2)
            acts.append((a1, a2))

        answer = get_match(acts)

        print('Case #{}: {}'.format(i + 1, answer))


if __name__ == '__main__':
    parenting_partnering()
