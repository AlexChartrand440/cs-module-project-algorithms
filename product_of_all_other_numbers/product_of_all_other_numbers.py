'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    
    results = [];

    index = 0;

    for x in arr:

        current = 0;
        product = 1;

        for y in arr:

            if index != current and current + 1 <= len(arr):
                print('Multiplying: ' + str(product) + ' x ' + str(y));
                product *= y;

            current += 1;

        index += 1;
        results.append(product);

    return results;


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [ 1, 7, 3, 4 ];
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
