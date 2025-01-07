import random
import datetime
import requests
from urllib.parse import quote


# 随机生成步数的函数
def generate_step():
    """根据当前日期生成不同的步数，周一到周五生成1w5~3w步，周六和周天生成2w2~4w步"""
    today = datetime.datetime.now()
    weekday = today.weekday()  # 0 = 周一, 6 = 周日

    if weekday < 5:  # 周一到周五
        return random.randint(15000, 40000)
    else:  # 周六和周日
        return random.randint(22000, 90000)


# 构建 URL 的函数
def build_url(user, password, step):
    """根据提供的用户、密码和步数构建请求 URL"""
    # 对用户和密码进行 URL 编码，避免特殊字符问题
    user_encoded = quote(user)
    password_encoded = quote(password)
    step_encoded = quote(str(step))

    # 拼接 URL
    url = f"https://api.leafone.cn/api/misport?user={user_encoded}&password={password_encoded}&step={step_encoded}"
    return url


# 发送 GET 请求并获取响应的函数
def send_request(url):
    """发送 GET 请求并返回响应"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.81 Safari/537.36",
    }

    try:
        # 发送 GET 请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        return f"Request failed: {e}"


# 主逻辑函数
def main(user, password):
    """主函数，调用其他函数完成爬取任务"""
    step = generate_step()  # 生成步数
    url = build_url(user, password, step)  # 构建 URL
    response_text = send_request(url)  # 发送请求并获取响应
    return response_text


# 测试函数
if __name__ == "__main__":
    # 示例用户和密码
    user = "226390686@qq.com"
    password = "226390686a+"

    # 获取 API 响应
    response = main(user, password)
    print("API Response:", response)
