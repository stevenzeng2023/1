# # 文件的操作 write   会覆盖原内容
# f = open("H:/py/test1.txt", 'w', encoding="UTF-8")
# f.write('My home have a little dog\nThe little dog is Lucky\nIt is usually wangwangwang')
# f.flush()
# f.close()


# f = open("H:/py/test2.txt", 'a', encoding="UTF-8")
# f.write('dogdogdogdog')
# f.flush()
# f.close()
# f = open("H:/py/test2.txt", 'a', encoding="UTF-8")  # 文件的操作 a   在最后处追加内容
# f.write('\nIt is a little dog')
# f.flush()
# f.close()





# # 练习
# with open("H:/py/bill.txt", 'r') as fr:
#
#     with open("H:/py/bill.txt.bak", 'w') as fw:
#         for line in fr:
#             line = line.strip()
#             if line.count("测试") == 1:
#                 continue
#             fw.writelines(line)
#             fw.write("\n")



