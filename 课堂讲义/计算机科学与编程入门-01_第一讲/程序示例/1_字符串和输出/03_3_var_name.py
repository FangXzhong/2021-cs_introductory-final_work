"""
Date: 2021.2.9
Author: Justin

要点说明：
变量的命名规则
"""

# ----------
# 1. 变量名可以是字母或下划线开头，包含任意数量的字母、下划线和数字
text_1 = 'hello'

# ----------
# 2. 变量名不能用数字开头，自然也不能全是数字。下面的变量声明会报错
# 1_text = 'hello'

# ----------
# 3. 下划线开头的变量名往往对Python解释器有特殊意义，不推荐初学者使用
# 连续两个下划线开头和结尾的变量名，用于Python内置的专有变量，编程时不要这样命名
print(__file__)  # 例如，__file__是Python内置的字符串变量，保存了当前文件的名称

# ----------
# 4. 不要使用Python的关键字（保留字）作为变量名。下面的变量声明会报错
# if = 'hello'

# Python的关键字如下，区分大小写：
# and	as	assert	break	class	continue
# def	del	elif	else	except	finally
# for	from	False	global	if	import
# in	is	lambda	nonlocal	not	None
# or	pass	raise	return	try	True
# while	with	yield 
 