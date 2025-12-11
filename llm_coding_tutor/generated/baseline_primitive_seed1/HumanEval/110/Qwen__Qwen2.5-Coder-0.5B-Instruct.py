def exchange(lst1, lst2):
    # count the number of odd numbers in lst1 and even numbers in lst2
    odd_count_lst1 = sum(1 for num in lst1 if num % 2!= 0)
    even_count_lst2 = sum(1 for num in lst2 if num % 2 == 0)
    
    # if there are enough even numbers in lst2 to replace all odd numbers in lst1, return "YES"
    if even_count_lst2 >= odd_count_lst1:
        return "YES"
    else:
        return "NO"```