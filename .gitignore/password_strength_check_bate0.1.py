"""
    作者：Johnson
    功能：判断密码强度（长度、数字、小写及大写字母）
    版本：0.1
    日期：01/01/2018
    功能：限制密码设置次数；循环的终止
          保存设置的密码及其对应的强度到文件中
          读取保存的密码
          将相关方法封装成一个整体：面向对象编程；定义一个password工具类
          将文件操作封装到一个类中
"""


class PasswordTool:
    """
        密码复杂性检测工具类
    """
    # 定义类的属性；(self,password)之中password表示从外部传递的参数
    def __init__(self, password):
        # self.password表示类的属性，接收外部传参
        self.password = password
        # 类的属性——密码强度
        self.strength_level = 0
        # 类的属性——密码强度文字描述
        self.strength_level_description = ''

    # 定义类的方法
    def check_number_exist(self):
        """
            判断字符串中是否含有数字
        """
        has_number = False
        # self.password-类的属性，在类里面的函数都可以调用
        for c in self.password:
            if c.isnumeric():
                has_number = True
        return has_number

    def check_lower_exist(self):
        """
            判断字符串中是否含有小写字母
        """
        has_lower = False
        for c in self.password:
            if c.islower():
                has_lower = True
        return has_lower

    def check_upper_exist(self):
        """
            判断字符串中是否含有大写字母
        """
        has_upper = False
        for c in self.password:
            if c.isupper():
                has_upper = True
        return has_upper

    # 定义类的方法，处理密码规则
    def process_password(self):
        # 规则1：密码长度要求大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则3：包含小写字母
        if self.check_lower_exist():
            self.strength_level += 1
        else:
            print('密码要求包含小写字母！')

        # 规则4：包含大写字母
        if self.check_upper_exist():
            self.strength_level += 1
        else:
            print('密码要求包含大写字母！')

        if self.strength_level == 1:
            self.strength_level_description = '密码强度非常弱'
        elif self.strength_level == 2:
            self.strength_level_description = '密码强度很弱'
        elif self.strength_level == 3:
            self.strength_level_description = '密码强度较弱'
        else:
            self.strength_level_description = '密码强度合格'


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self,line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines # 显示读取内容


def main():
    """
        主函数
    """
    # 限制密码设置次数
    try_times = 5
    file_path = 'password6.1.txt'
    # 实例化文件工具对象
    file_tool = FileTool(file_path)

    while try_times > 0:
        password = input('请输入密码：')

        # 实例化密码工具对象，并按类的初始化方法传入一个参数
        password_tool = PasswordTool(password)
        # 调用类的密码规则方法，判断密码强度
        password_tool.process_password()

        # 如果存储密码强度不合格的密码，只是提示密码强度不合格，写文件代码放在这里；
        file_tool.write_to_file(line='密码：{}，强度：{}\n'.format(password, password_tool.strength_level_description))
        print('密码保存成功')

        if password_tool.strength_level == 4:
            print('恭喜！密码强度合格！')
            # # 如果不存储密码强度不合格的密码，写文件代码放在这里；
            # file_tool.write_to_file(line='密码：{}，强度：{}\n'.format(password, password_tool.strength_level_description))
            # print('密码保存成功')
            break
        else:
            print('抱歉！密码强度不合格')
            try_times -= 1
        print()
    else:
        print('尝试次数过多，密码设置失败！')

    # 读文件
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()

