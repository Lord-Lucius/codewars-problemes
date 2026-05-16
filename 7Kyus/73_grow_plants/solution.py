def growing_plant(up_speed, down_speed, desired_height):
    count = 0
    grow = 0

    if up_speed >= desired_height:
        return 1

    while grow <= desired_height:
        grow += up_speed
        count += 1
        if grow >= desired_height:
            return count
        grow -= down_speed
    return count

if __name__ == "__main__":
    sample_test_cases = [
    #     up  dn    h    exp
        (100, 10, 910,   10),
        ( 10,  9,   4,    1),
        (  5,  2,   0,    1),
        (  5,  2,   5,    1),
        (  5,  2,   6,    2),
        ( 57, 51, 505,   76),
    ]

    for up_speed, down_speed, desired_height, expected in sample_test_cases:
        print(f"function result: {growing_plant(up_speed, down_speed, desired_height)} :: expected: {expected}")
