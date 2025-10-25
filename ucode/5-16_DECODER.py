with open("5-16_DECODER.txt", "w") as f:
    for i in range(256):
        if i < 16:
            val = 1 << i
            f.write(f"{val}\n")
        else:
            f.write("0\n")
