'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    # []
    # [ 0 , 3, 1, 0, -2 ]

    # 0 == 0: Append

    # [ 0 ]
    # [ 0 , 3, 1, 0, -2 ]

    # 3 > 0: Insert <-

    # [ 3, 0 ]
    # [ 0, 3, 1, 0, -2 ]

    # 1 > 0: Insert <-

    # [ 1, 3, 0 ]
    # [ 0, 3, 1, 0, -2 ]

    # 0 == 0: Append

    # [ 1, 3, 0, 0 ]
    # [ 0, 3, 1, 0, -2 ]

    # -2 < 0: Insert <-

    # [ -2, 1, 3, 0, 0 ]
    # [ 0, 3, 1, 0, -2 ]

    shifted = [];

    for i in arr:
        if len(shifted) == 0:
            shifted.append(i);
        elif i != 0:
            shifted.insert(0, i);
        else:
            shifted.append(i);

    return shifted;


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")