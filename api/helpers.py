UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_snake(string):
    result = [string[0].lower()]
    for char in string[1:]:
        if char in UPPER_CASE:
            result.append("_")
        result.append(char.lower())
    return "".join(result)
