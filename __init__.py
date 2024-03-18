def triangle(n):
    k = n - 1

    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i + 1):
            print("□ ", end="")

        print("\r")
    n = 4

if __name__ == '__main__':
    triangle(4)

"teste 2"