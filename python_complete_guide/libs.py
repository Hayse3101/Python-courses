

def get_count(str_value: str, symbol: str) -> int:
    cnt = 0
    for i in str_value:
        if i == symbol:
            cnt += 1
    return cnt


def get_len(str_value: str) -> int:
    cnt = 0
    for _ in str_value:
        cnt += 1
    return cnt


if __name__ == '__main__':
    print(__name__)
    print('Hello, I am libs.py')
