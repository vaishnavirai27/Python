# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end=" ")
#     print()
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
# for i in range(5, 0, -1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()
# for i in range(1, 6):
#     for j in range(1, 5 - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, 5 - i + 1):
#         print(" ", end=" ")
#     for k in range(i, 0, -1):
#         print(k, end=" ")
#     print()


# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for k in range(i, 6):
#         print(k, end=" ")
#     print()


# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print("", end=" ")
#     for k in range(i, 6):
#         print(k, end=" ")
#     print()

# n = 9
# for i in range(1, n // 2 + 2):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(n // 2, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# n = 7
# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print(i, end=" ")
#     print()

n = 7
for i in range(1, n // 2 + 2):
    for j in range(1, n // 2 - i + 2):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()
for i in range(n // 2, 0, -1):
    for j in range(1, n // 2 - i + 2):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()
