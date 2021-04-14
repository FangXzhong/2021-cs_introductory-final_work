"""
Date: 2021.2.9
Author: Justin

要点说明：
展示字符串自带的功能函数（通常也称为“方法”），如改变大小写等
用字符串变量后加点“.”的方式引用，可以理解成从属关系
注意体会与print、len这些函数在形式上的区别
"""

msg = 'welcome to Beijing'  # 注意字符串中的大小写

# 调用字符串自带的函数，注意用句点“.”的方式调用，函数名称后带一对括号
msg_new = msg.upper()  #把字符串转为全部大写
print(msg_new)
print(msg)  # 注意，上面的操作不会改变该字符串本身

print('----------')
print(msg.lower())   #把字符串转为全部小写

print(msg.swapcase())  #把字符串所有字符的大小写反转
print(msg.title())     #把各单词的首字母转为大写
print(msg.capitalize())   #把字符串首字母转为大写，其它字母小写

print('----------')
print(msg)  # 再次检查确认，上面的操作不会改变该字符串本身
