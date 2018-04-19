if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(list(integer_list)[:n])
    print(hash(t))