"""
Date: 2021.3.7
Author: Justin

要点说明：
回顾变量复制，以便后续和列表复制进行对比
"""
name1 = '刘备'
name1_bak = name1
print(name1, name1_bak)

name1 = '刘皇叔'  # 修改name1，不会影响name1_bak
print(name1, name1_bak)

