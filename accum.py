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
    result = ''
    for i, v in enumerate(s):
        result += (s[i] * (i +1)).title() + '-'
    return result[: -1]

# Alternative Solution:
# def accum(s):
#     return '-'.join( (v * c).title() for c, v in enumerate(s, 1))
