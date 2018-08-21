def is_overlapping(list1, list2):
    def length_of_list(a_list):
        length = 0
        while a_list:
            length += 1
            a_list = a_list.next
        return length

    l1, l2 = length_of_list(list1), length_of_list(list2)
    if l1 > l2:
        l2, l1 = l1, l2

    for _ in range(l2 - l1):
        list2 = list2.next

    while list2 and list1 and list2 is not list1:
        if list1 is list2:
            return list1
        list1, list2 = list1.next, list2.next
    return list1
