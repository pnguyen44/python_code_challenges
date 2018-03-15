# 7 kyu- Mumbling
# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
#
# accum("abcd")    # "A-Bb-Ccc-Dddd"
# accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt")    # "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    result = []
    s = list(s)
    s = [' '] + s
    for x  in range(len(s)):
        result.append((s[x] * x).title())
    result.pop(0)

    return '-'.join(result)
