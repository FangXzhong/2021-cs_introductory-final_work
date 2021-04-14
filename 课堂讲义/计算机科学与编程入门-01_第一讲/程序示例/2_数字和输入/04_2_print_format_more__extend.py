"""
Date: 2021.2.9
Author: Justin

要点说明：
进一步展示格式化输出
"""

# format()括号中的参数，可以是变量，也可以直接写字符串、数字（不用做类型转换）等
name = '张飞'
score = 95
print('{}同学，你的成绩是{}分。'.format(name, score))

print('{}同学，你的成绩是{}分。'.format('刘备', 77))


# format中的参数可以按位置索引（从0开始）
# 位置编号写在{}中，输出时可以按任意顺序调用
print(('{0}, {1}').format('apple', 'cherry'))
print(('{0}, {1}, {0}').format('apple', 'cherry'))      
print(('{1}, {0}, {0}').format('apple', 'cherry'))       

print('-'*20)

# format中的参数也可以用名称标记，在{}中用参数名称引用
print('我喜欢{c1}和{c2}，最喜欢的还是{c1}。'.format(c1='红色', c2='黄色' ))      