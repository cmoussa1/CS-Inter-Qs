# Determine if two strings are anagrams

def det_if_anagram(str1, str2):
    # the sorted strings are checked
    if(sorted(str1) == sorted(str2)):
        return "The strings are anagrams."
    else:
        return "The strings aren't anagrams."

print det_if_anagram("listen", "silent")
print det_if_anagram("bad", "dad")
