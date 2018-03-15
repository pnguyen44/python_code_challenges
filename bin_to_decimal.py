# 8 kyu- Bin to Decimal
# Complete the function which converts a binary number (given as a string) to a decimal number.

def bin_to_decimal(inp):
    return int(inp,2)

# Alternative Solution:
# def bin_to_decimal(inp):
#     result = 0
#     inp =  inp[:: -1]
#     for i in range(len(inp)):
#         result += int(inp[i]) * 2 ** i
#     return result
