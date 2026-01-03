
import os,requests,time

video_url="https://cdn15.yzzy-tv-cdn.com/20230627/16833_55f64ab2/2000k/hls/26acccb1ba0000106.ts"

def ceshigc(video_url):
    # 提取文件名
    filename = os.path.basename(video_url)

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    # 发送HTTP GET请求
    response = requests.get(video_url,headers=header)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打开文件以二进制写入模式
        with open(filename, 'wb') as f:
            # 写入视频数据
            f.write(response.content)
            time.sleep(1)
        print('视频下载成功！')
    else:
        print('视频下载失败！')

s1 = "https://cdn15.yzzy-tv-cdn.com/20230627/16833_55f64ab2/2000k/hls/26acccb1ba"
s2 = ".ts"

for i in range(1, 160):
    formatted_number = f"{i:07}"
    pj_url=s1+str(formatted_number)+s2
    ceshigc(pj_url)