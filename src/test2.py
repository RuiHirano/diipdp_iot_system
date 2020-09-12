import binascii

def convert16to10(x="0000", dicimal=2):
    minus = False
    binx = format(int(x, 16), '016b')  # 二進数表示 16桁に0埋め: '016' 二進数： 'b'
    if binx[0] == "1":
        # 補数変換
        binx = convert2Complement(binx)
        minus = True

    leftbin = binx[:dicimal*4]   # 整数部分
    rightbin = binx[dicimal*4:]  # 小数点部分

    # 10進数へ変換(整数部分)
    left10 = int(leftbin, 0)
    # 10進数へ変換(少数部分)
    right10 = 0
    for index, k in enumerate(rightbin):
        right10 += int(k)*2**(-index-1)
    
    if minus: # 補数だった場合、負にする
        return -(left10 + right10)
    else: 
        return left10 + right10

def convert2Complement(binx):
    # 2の補数変換
    return format((-int(binx[0]) << len(binx) | int(binx, 2))*-1, '016b')
    
        


if __name__ == "__main__":
    data = "e1ff a1 03 64 0005 0000 00f8 2035263f23ac"
    print(b"\xb8\xa8\xa3\x96Ia5".decode('utf-8'))
    #cal = binascii.b2a_hex(data)
    #print("cal: ", cal)
    i = 255
    hex_str = format(i, 'x')
    print("hex: ", hex_str)
    hex_num = int('f8', 16)
    print("hex num: ", bin(hex_num))
    print("z: ", convert16to10("00f8"))
    print("y: ", convert16to10("0005"))
    print("x: ", convert16to10("0000"))
    print("battery: ", 0x64)
    print("flag data type: ", bytes.fromhex("f7"))
    print("flag data: ", int("000000", 16))

    test = convert16to10()
    print("debug: ", test)


