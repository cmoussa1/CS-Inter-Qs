# Reverse a string recursively and iteratively

# Iterative solution
def reverse_str_iter(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print reverse_str_iter("Hello, world!")

# Recursive Solution
def reverse_str_recur(text):
    if text == "":
        return text
    else:
        return reverse_str_recur(text[1:]) + text[0]

print reverse_str_recur("Hello, world!")
