
def next_palindrome(n):
        n = n+1
        while not is_palindrome(n):
            n = n + 1
        return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int (input("Enter the size of list :- "))
    num_list =[]
    for i in range(size):
        num_list.append(int(input("Enter the number of the list : ")))
    print(f"you her entered {num_list}")

    # list comprihensial give one list and one line code
    # print(f"Output list : {[num_list[i] if num_list[i] <10 else next_palindrome(num_list[i]) for i in range(size)]}")

    new_list = []
    for element in num_list:
        if element > 10:
            n = next_palindrome(element)
            new_list.append(n)
        else:
            new_list.append(element)
    print(f"Output List : {new_list}")
