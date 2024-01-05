N = int(input())
people = [input().rstrip().split() for _ in range(N)]

people.sort(key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
print(people[0][0])
print(people[N-1][0])

# x_yy = 0
# # max_y = []
# # for name, dd, mm, yy in people:
# #     yy = int(yy)
# #     if max_yy < yy:
# #         max_yy = yy
# #     if max_yy == yy:
# #         max_y.append((name, dd, mm))
# #
# # if len(max_y) == 1:
# #     print(max_y[0][0])
# #
# # else:
# #     max_y.sort(key=lambda x: x[2])
# #
# #     max_mm = 0
# #     max_m = []
# #     for name, dd, mm in max_y:
# #         mm = int(mm)
# #         if max_mm < mm:
# #             max_mm = mm
# #         if max_mm == mm:
# #             max_m.append((name, dd))
# #
# #     max_m.sort(key=lambda x: x[1])
# #     print(max_m[0][0])
# #
# #
# # people.sort(key=lambda x: x[3])
# #
# # min_yy = 2010
# # min_y = []
# # for name, dd, mm, yy in people:
# #     yy = int(yy)
# #     if min_yy > yy:
# #         min_yy = yy
# #     if min_yy == yy:
# #         min_y.append((name, dd, mm))
# #
# # if len(min_y) == 1:
# #     print(min_y[0][0])
# #
# # else:
# #     min_y.sort(key=lambda x: x[2])
# #
# #     min_mm = 12
# #     min_m = []
# #     for name, dd, mm in min_y:
# #         mm = int(mm)
# #         if min_mm > mm:
# #             min_mm = mm
# #         if min_mm == mm:
# #             min_m.append((name, dd))
# #
# #     min_m.sort(key=lambda x: x[1])
# #     print(min_m[0][0])
# ma
