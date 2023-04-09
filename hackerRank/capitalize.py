# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    word = ''
    for i in range(len(s)):
        word += s[i].capitalize() + " "

    return word


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
