'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=None):

    if arr is None:
        arr = [0 for i in range(0, n + 1)];
    
    if n < 0:
        return 0;
    elif n == 0 or n == 1:
        return 1;
    else:

        if arr[n] != 0:
            return arr[n];
        
        arr[n] = eating_cookies(n - 1, arr) + eating_cookies(n - 2, arr) + eating_cookies(n - 3, arr);

        return arr[n];
        # return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3);

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
