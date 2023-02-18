def main(s, numRows):
    if numRows == 1:
        return s
    out = ["" for i in range(0, numRows)]
    base = numRows*2 - 2
    base_middle = numRows - 1
    for i in range(0, len(s)):
        ostatok = i % base
        if ostatok > base_middle:
            ostatok = base - ostatok
        out[ostatok] = out[ostatok] + s[i]
    return str("").join(out)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 2
    #s = "A"
    numRows = 1
    print(main(s, numRows))