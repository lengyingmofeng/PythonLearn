# @作者 : 叶枫
# @文件 : 实用用户注册时的验证.py 
# @时间 : 2020/10/14 15:07 
# @版本 ：1.0


def validate_login_name(login_name):
    str_len = len(login_name)
    # 1.用户最多25个字符长度、不能包含空格、单双引号、问号等特殊符号
    if str_len == 0 or str_len > 25:
        return False
    # 自定义的非法字符串，打架可以根据自己的系统进行自由的添加
    invalid_chars = "'\"?!$#@^%()*&+-"
    for char in login_name:
        if char in invalid_chars:
            return False
    return True


def validate_password(password):
    valid_symbols = [chr(value) for value in range(ord("A"), ord("Z") + 1)]
    valid_symbols += [chr(value) for value in range(ord("a"), ord("z") + 1)]
    valid_symbols += [chr(value) for value in range(ord("0"), ord("9") + 1)]
    valid_symbols += list("_@$#")
    str_len = len(password)
    # 判断密码是否有效
    if str_len < 6 or str_len > 18:
        return False
    # 遍历没一个字符
    for char in password:
        if char not in valid_symbols:
            return False
    # 如果代码能够执行到这里，密码一定合法
    if password.isdecimal() or password.isalpha():
        return "★" * 2
    if password.isalnum() or validete_password_letter_symobl(password) or validate_password_decimal_symbol(password):
        return "★" * 4
    return "★" * 6


def validate_password_decimal_symbol(password):
    """验证传入的字符串是否是数字+合法特殊符号的组合"""
    valid_symbols = [chr(value) for value in range(ord("0"), ord("9") + 1)]
    valid_symbols += list("_@$#")
    valid_symbols = str(valid_symbols)
    for char in password:
        if valid_symbols.find(char) == -1 :
            return False
    return True


def validete_password_letter_symobl(password):
    """验证传入的字符串是否是字母+合法符号的组合"""
    valid_symbols = [chr(value) for value in range(ord("A"), ord("Z") + 1)]
    valid_symbols += [chr(value) for value in range(ord("a"), ord("z") + 1)]
    valid_symbols += list("_@$#")
    valid_symbols = str(valid_symbols)
    for char in password:
        if valid_symbols.find(char) == -1:
            return False
    return True


if __name__ == '__main__':


    login_name = "admin"
    print("登录名是否合法：", validate_login_name(login_name))

    password = "123456"
    print("密码等级", validate_password(password))
