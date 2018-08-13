def is_palindrome(s):
    start, end = 0, len(s) - 1

    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True

