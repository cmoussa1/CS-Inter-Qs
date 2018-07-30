# Find the first non-repeated character in a String

NO_OF_CHARS = 256

# Returns an array of size 256 containg count
# of characters in the passed char array
def get_char_count(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+=1
    return count

# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def first_non_repeating(string):
    count = get_char_count(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index

print first_non_repeating("geeksforgeeks")
