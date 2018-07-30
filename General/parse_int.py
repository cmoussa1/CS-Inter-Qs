# Implement parseInt
def parse_int(x):
    temp = []
    for c in str(x).strip():
        if c.isdigit():
            temp.append(c)
        else:
            break
    return int("".join(temp)) if "".join(temp) else None

print parse_int(1)
print parse_int(10.2)
print parse_int("14.6")
