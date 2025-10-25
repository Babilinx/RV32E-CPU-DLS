"""
IN:
{write}{}{reset}{mem}{in}{}{in}

"""

inp = [
    0b00000000,
    0b00000001,
    0b00000100,
    0b00000101,
]
inp_msk = 0b00000111

wr = [
    0b00000000,
    0b10000000,
]
wr_msk = 0b10000000

rst = [
    0b00000000,
    0b00100000,
]
rst_msk = 0b00100000

out = [
    "0000000000000000",
    "0000000000001001",
    "0000000000010100",
    "0000000000011101",
]

def data(val):
    return (val & 0b00011000) >> 3


with open("2BIT_REG.txt", "w") as f:
    for i in range(256):
        print(f"{i:b}")
        
        # Write
        if i & wr_msk:
            print("write")
            if i & rst_msk:
                f.write(out[0])
            elif (i & inp_msk) == 0b000:
                f.write(out[0])
            elif (i & inp_msk) == 0b001:
                f.write(out[1])
            elif (i & inp_msk) == 0b100:
                f.write(out[2])
            elif (i & inp_msk) == 0b101:
                f.write(out[3])
            else:
                f.write(out[0])

        # Reset
        elif i & rst_msk:
            print("reset")
            f.write(out[0])
        
        # Keep the data
        else:
            print(f"data {data(i)}")
            f.write(out[data(i)])
        
        f.write("\n")
