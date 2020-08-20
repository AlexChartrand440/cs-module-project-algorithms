'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    discovered = [];
    count = [];

    for i in arr:
        if i not in discovered:
            discovered.append(i);
            count.append(1);
        elif i in discovered:
            count[discovered.index(i)] += 1;

    print(discovered[count.index(1)]);

    return discovered[count.index(1)];


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")