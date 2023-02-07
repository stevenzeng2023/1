# 类
class Phone:
    __is_5g_enable = input("是否开启5G功能,开启请输入'1'，关闭请输入'0',请输入：")

    def __check_5g(self):
        if self.__is_5g_enable == str(1):
            print("5G已开启")

        elif self.__is_5g_enable == str(0):
            print("5G已关闭，使用4G网络")
        else:
            __is_5g_enable = input("输入有误，开启请输入'1'，关闭请输入'0'")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
