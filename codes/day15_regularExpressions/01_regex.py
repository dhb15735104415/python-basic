"""
    正则表达式(regular expression)描述了一种字符串匹配的模式（pattern），
    可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。
    比如判断email是否合法
    创建一个匹配Email的正则表达式：
        1、创建一个匹配Email的正则表达式；
        2、用该正则表达式去匹配用户的输入来判断是否合法。

    因为正则表达式也是用字符串表示的所以，我们要首先了解如何用字符来描述字符。
"""

'''
    1、在正则表达式中，如果直接给出字符，就是精确匹配。
    .可以匹配任意字符
    \d可以匹配一个数字，\D表示非数字
    \w可以匹配一个字母或数字或下划线
'''
# 练习1:普通字符 abc、元字符 \d

regex1 = 'abc'  # 匹配字符串中是否包含 'abc'
regex2 = '\d'  # 匹配字符串中是否包含单个数字

'''
    2、匹配变长字符
    用.匹配除换行符以外的任意字符
    用*表示任意个字符（包括0个），
    用+表示至少一个字符，
    用?表示0个或1个字符，
    用{n}表示n个字符，
    用{n,m}表示n到m个字符
'''

# 练习2：\d{3}\s+\d{3,8}
'''
    从左到右解读一下：
    
    \d{3}表示匹配3个数字，例如'010'；
    
    \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，'    '等；
    
    \d{3,8}表示3-8个数字，例如'1234567'。
'''

'''
    3、字符集
    用[]表示范围，就可以匹配多个字符了
'''

'''
    [0-9]其实表示的就是\d ，那么[^0-9]表示\D
    [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
    
    [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
    
    [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
    
    [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
    
    A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
    
    ^表示行的开头，^\d表示必须以数字开头。
    
    $表示行的结束，\d$表示必须以数字结束。
    
    你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
    
    
    .	匹配除 "\n" 之外的任何单个字符，要匹配包括 '\n' 在内的任何字符，请使用象 '[\s\S]' 的模式
    [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
    [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符
    \d	匹配一个数字字符。等价于 [0-9]
    \D	匹配一个非数字字符。等价于 [^0-9]
    \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]
    \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]
    \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'
    \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'
    示例
    [Pp]ython	匹配 "Python" 或 "python"
    rub[ye]	匹配 "ruby" 或 "rube"
    [aeiou] 匹配中括号内的任意一个字母
    [0-9]	匹配任何数字。类似于 [0123456789]
    [a-z]	匹配任何小写字母
    [A-Z]	匹配任何大写字母
    [a-zA-Z0-9]	匹配任何字母及数字
    [^aeiou]	除了aeiou字母以外的所有字符
    [^0-9]	匹配除了数字外的字符
'''
