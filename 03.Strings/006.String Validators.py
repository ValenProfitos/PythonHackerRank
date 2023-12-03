if __name__ == "__main__":
    s = input()

    mySisAlnum = any(c.isalnum()for c in s)
    mySisAlph = any(c.isalpha()for c in s)
    mySisDig = any(c.isdigit()for c in s)
    mySisLow = any(c.islower()for c in s)
    mySisUp = any(c.isupper()for c in s)

    print(mySisAlnum)
    print(mySisAlph)
    print(mySisDig)
    print(mySisLow)
    print(mySisUp)