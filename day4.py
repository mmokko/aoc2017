ADDED_SECURITY = True


def get_letters(value):
    letters = dict()
    for letter in value:
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters


def is_anagram(value, other):
    if len(value) != len(other):
        return False
    letters = get_letters(value)
    for letter, count in letters.items():
        if count != other.count(letter):
            return False
    return True


def is_unique(value, pool, added_security):
    if not added_security:
        if value in pool:
            return False
    else:
        for item in pool:
            if is_anagram(value, item):
                return False
    return True


def is_valid(line, added_security):
    items = line.split()
    for idx in range(1, len(items)):
        search_items = items[idx:]
        if not is_unique(items[idx - 1], search_items, added_security):
            return False
    return True


def valid_passphrases(lines, added_security=False):
    total = 0
    for line in lines:
        total += 1 if is_valid(line, added_security) else 0
    return total


def main():
    with open("day4_input.txt", 'r') as f:
        lines = f.read().splitlines()
    print(valid_passphrases(lines))
    print(valid_passphrases(lines, ADDED_SECURITY))


if __name__=='__main__':
    main()