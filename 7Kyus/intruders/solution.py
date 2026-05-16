def eliminate_unset_bits(number):
    ret = 1
    nun = number.count("1")
    if nun == 0:
        return 0
    for i in range(nun):
        ret = ret<<1
    return ret - 1

if __name__ == "__main__":
    print(eliminate_unset_bits("11010101010101"))
    print(eliminate_unset_bits("111"))
    print(eliminate_unset_bits("1000000"))
    print(eliminate_unset_bits("000"))
