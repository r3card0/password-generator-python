def set_len_character(number: int) -> int:
    try:
        max_num:int=number
        max_num = int(max_num)
        if max_num > 8:
            return max_num
        else:
            return False
    except ValueError:
        return 'Please, enter an integer value'


def run():
    print(set_len_character(16))


if __name__ == "__main__":
    run()