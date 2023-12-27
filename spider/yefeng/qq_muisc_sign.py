import time

import requests

# qq：qq账号， qq_url:qq签到听歌地址， cookie, size：次数
def sing_music(qq, qq_url, cookie, size):
    url = "https://shanhe.kim/api/qy/qy_v3.php"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    data = {
        "qq": qq,
        "url": qq_url,
        "key": cookie,
        "size": size
    }
    response = requests.get(url, headers=header, params=data)
    print(response.text)


if __name__ == '__main__':
    sing_music("1797719651",
               "https://y.qq.com/n/ryqq/songDetail/000sZjQO3AcECz",
               "Q_H_L_5llXnhDTIiEPBTAwLwvbWeHzLZLYyoVqdTS5Ech3HxSu8vpR2WQrIvg", 50)

    # sing_music("1797719651",
    #            "https://y.qq.com/n/ryqq/songDetail/003YC3p31HyR96",
    #            "Q_H_L_5llXnhDTIiEPBTAwLwvbWeHzLZLYyoVqdTS5Ech3HxSu8vpR2WQrIvg", 50)
    #
    # sing_music("2951575706",
    #            "https://y.qq.com/n/ryqq/songDetail/000sZjQO3AcECz",
    #            "Q_H_L_5LU_tAY9yqyfv6kZnH4iLdIMH9zUZkDC0MjmwiqCSytO9RbBtu1fXyw&PC=U316&FORM=CHROMN", 50)
    #
    # sing_music("2951575706",
    #            "https://y.qq.com/n/ryqq/songDetail/003YC3p31HyR96",
    #            "Q_H_L_5LU_tAY9yqyfv6kZnH4iLdIMH9zUZkDC0MjmwiqCSytO9RbBtu1fXyw&PC=U316&FORM=CHROMN", 50)
