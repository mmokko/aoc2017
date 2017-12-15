import copy


class Garbage(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.start = 0
        self.end = 0
        self.count = 0


def _count(current, last, finding):
    # ignore ! except when last is also !
    if current == '!' and last != '!':
        return 0
    # ignore all if last is !
    if last == '!':
        return 0
    # ignore start if we are not already finding
    if current == '<' and not finding:
        return 0
    # ignore end char
    if current == '>':
        return 0
    return 1

def _get_last(current, last):
    if current == '!' and last == '!':
        return ''
    return current

def _find_garbage(stream):
    garbage_found = False
    garbage = Garbage()
    garbages = list()
    last = ''
    count = 0
    for idx in range(len(stream)):
        current = stream[idx]
        if current == '<' and not garbage_found and last != '!':
            garbage_found = True
            garbage.start = idx
            count = 0
        elif current == '>' and last != '!':
            garbage_found = False
            garbage.end = idx
            garbage.count = count
            garbages.append(copy.copy(garbage))
            garbage.reset()
        else:
            count += _count(current, last, garbage_found)
        last = _get_last(current, last)
    return garbages

def _clean_garbage(stream):
    garbages = _find_garbage(stream)
    for garbage in reversed(garbages):
        stream = stream[:garbage.start] + stream[garbage.end + 1:]
    return stream

def _count_groups(stream):
    score = 0
    group_index = 0
    last = ''
    for char in stream:
        if char == '{' and last != '!':
            group_index += 1
        if char == '}' and last != '!':
            score += group_index
            group_index -= 1
        last = char
    return score

def calc(stream):
    cleaned_stream = _clean_garbage(stream)
    return _count_groups(cleaned_stream.replace(',', ''))

def calc_carbage(stream):
    total = 0
    garbages = _find_garbage(stream)
    for garbage in garbages:
        total += garbage.count
    return total


def main():
    with open("day9_input.txt", 'r') as f:
        input_txt = f.read()
    print(calc(input_txt))
    print(calc_carbage(input_txt))


if __name__=='__main__':
    main()