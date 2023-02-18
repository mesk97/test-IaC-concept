def main():
    f = open("/tmp/aaa", "r")
    for s in f.readlines():
        ff = s.strip().split(",")
        print (ff)

if __name__ == "__main__":
    main()