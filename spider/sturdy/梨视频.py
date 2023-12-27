# @作者 : 叶枫
# @文件 : 梨视频.py 
# @时间 : 2021/10/25 12:02
# @版本 ：1.0
# @功能描述:
import requests, time
first_time = time.time()
url = "https://www.pearvideo.com/video_1744406"
contID = url.split("_")[-1]
videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.5296292389146533"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    # 防盗链： 溯源，当前本次请求的上一级是谁
    "Referer": url
}
resp = requests.get(videoStatus, headers=headers)
# 把内容转换成JSON
dic = resp.json()
# 拿到视频地址
srcUrl = dic['videoInfo']['videos']['srcUrl']
# 拿到systemTime
systemTime = dic['systemTime']
# 把srcUrl中的systemTime替换成cont-{contID}拿到视频地址
srcUrl = srcUrl.replace(systemTime, f'cont-{contID}')
# 下载视频
with open("明明就.mp4", "wb") as f:
    f.write(requests.get(srcUrl, headers=headers).content)

last_time = time.time()
final = last_time - first_time
print("用时间" % final)