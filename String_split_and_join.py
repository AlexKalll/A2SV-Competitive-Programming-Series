def split_and_join(line):
    # write your code here
    b = "-".join(line.split(" "))
    return b
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
