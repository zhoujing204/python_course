# 导入被测试的函数
from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    
    # 使用设定的输入'janis', 'joplin'去调用被测试的函数
    formatted_name = get_formatted_name('janis', 'joplin')
    
    # 用断言语句去判断函数实际输出format_name是否符合预期'Janis Joplin'
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    
    assert formatted_name == 'Wolfgang Amadeus Mozart'