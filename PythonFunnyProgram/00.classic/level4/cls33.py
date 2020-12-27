################################
# ord ordinal     char -> int
# chr character   int  -> char
# bin             10 -> 2
# int             2(str) -> 10

# encode
# decode

################################
# '''
# 原字符串左侧对齐， 右侧补零:
# '''
# str.ljust(width,'0')
# input: '789'.ljust(32,'0')
# output: '78900000000000000000000000000000'
#
#
# '''
# 原字符串右侧对齐， 左侧补零:
# 方法一：
# '''
# str.rjust(width,'0')
# input: '798'.rjust(32,'0')
# output: '00000000000000000000000000000798'
# '''
# 方法二：
# '''
# str.zfill(width)
# input: '123'.zfill(32)
# output:'00000000000000000000000000000123'
# '''
# 方法三：
# '''
# '%07d' % n
# input: '%032d' % 89
# output:'00000000000000000000000000000089'

info = 'When you want to give up, think about what made you insist on coming here.'


def encode(s):
    encode_str = ''
    for c in info:
        encode_str += bin(ord(c))[2:].rjust(8, '0')
    return encode_str


def decode(s):
    decode_str = ''
    for i in range(0, len(s), 8):
        decode_str += chr(int(s[i:i + 8], 2))
    return decode_str


def dec_to_bin(a):
    ret = ''
    while a != 0:
        ret += str(a % 2)
        a //= 2
    return ret[::-1]


def bin_to_dec(bin_str):
    ret = 0
    base = 1
    for b in bin_str[::-1]:
        ret += int(b) * base
        base *= 2
    return ret

# encode_s = encode(info)
# decode_s = decode(encode_s)
# print(encode_s)
# print(decode_s)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def print_prime(beg, end):
    for n in range(beg, end+1):
        if is_prime(n):
            print(n)

print_prime(1, 1000)