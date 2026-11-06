def get_number(msg, low, high):
    while True:
        try:
            n = int(input(msg))
            if low <= n <= high:
                return n
            print(low, '~', high, '사이로 입력하세요.')
        except ValueError:
            print('숫자만 입력하세요.')


def load_best(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0


def save_best(fname, tries):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(str(tries))