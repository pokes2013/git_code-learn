import re
import os
import requests


def extract_string_between_symbols(text, start_symbol, end_symbol):
    pattern = f"{start_symbol}(.*?){end_symbol}"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None





def get_duoye_url_list(url):
    aburl_list = []
    com = "https://avmoo.online/"
    url = url.replace("https", "http")
    # print(url)

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        html_content = response.text

        # 页码和章节提取，这里需要注意的是re.findall提取标签之间的内容，没有标签是不行的，返回的结果是一个list
        yema_list = re.findall('<a name="numbar"  href=".*?">.*?</a>', html_content)

        for yema in yema_list:
            # print(yema)
            yema_url = extract_string_between_symbols(yema, '/', '">')
            zhangjie = extract_string_between_symbols(yema, ">", "<")

            aburl = com + yema_url
            aburl_list.append(aburl)
            # print(yema_url)
            # print(zhangjie)
            # print(aburl)
    else:
        print("无法访问")
    return aburl_list


def delete_file(filename):
    """
    判断文件是否存在，如果存在则删除。
    """
    if os.path.exists(filename):
        os.remove(filename)
        print(f"文件 {filename} 删除成功！")
    else:
        print(f"文件 {filename} 不存在。")





def html_danye(url,xrfs):
    """
    获取网页源代码，写入到yuadaima.txt
    xrfs为写入方式
    """
    # url = input("请输入你的网址:")
    # url = "https://avmoo.online/cn/series/5019cd7b9d64f152"
    # print(url)
    htmlurl = url.replace("https", "http")

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    response = requests.get(htmlurl, headers=header)

    if response.status_code == 200:
        html_content = response.text
        # print(html_content)
        with open("yuadaima.txt", xrfs, encoding='UTF-8') as fff:
            fff.write(html_content)


def tiqu_yuandaima():
    list_title = []
    list_vido_info = []
    list_id_any = []
    with open("yuadaima.txt", 'r', encoding='UTF-8') as file:
        print(file.readline())
        for line in file:
            line = line.rstrip('\n')
            if "<title>" in line:
                title = extract_string_between_symbols(line, "<title>", "</title>")
                list_title.append(title)

            if "<span>" in line:
                # name = extract_string_between_symbols(line, "<span>", "</span>")
                name = extract_string_between_symbols(line, "<span>", "<")
                # name = name.split("<", 1)[0]
                print(name)
                id_fanhao = extract_string_between_symbols(line, "<date>", "</date>")
                date = extract_string_between_symbols(line, "/ <date>", "</date></span>")
                id_name = id_fanhao + "~" + name + "~" + date
                list_vido_info.append(id_name)

                id_pokes = id_name.split("~")[0:1]
                id_pokes = ''.join(id_pokes)
                list_id_any.append(id_pokes)

    # 写入title的信息
    title = ''.join(list_title)
    with open("yuadaima-已处理.txt", 'a', encoding='UTF-8') as file:
        # print(title)
        file.write(title)
        file.write("\n" * 2)

    # 写入搜索的信息
    sousuo = '|'.join(list_id_any)
    with open("yuadaima-已处理.txt", 'a', encoding='UTF-8') as file:
        print(sousuo)
        file.write(sousuo)
        file.write("\n" * 3)
        file.write("*" * 60)
        file.write("\n" * 3)

    # 写入每一行的详细信息
    for avinfo in list_vido_info:
        if "【VR】" not in avinfo:
            with open("yuadaima-已处理.txt", 'a', encoding='UTF-8') as file:
                print(avinfo)
                file.write(avinfo + "\n")


url = input("请输入网址：")

delete_file("yuadaima-已处理.txt")
delete_file("yuadaima.txt")

yemalist = get_duoye_url_list(url)
if len(yemalist) > 0:
    print(yemalist)
    print("多页处理中，请稍后")

    ## 多页追加写入到yuandaima.txt
    for url in yemalist:
        html_danye(url,"a")


    tiqu_yuandaima()
else:
    print("只有1页，正在处理")
    html_danye(url,"w")
    tiqu_yuandaima()

# yemalist = get_duoye_url_list(url)
# print(yemalist)
# https://avmoo.online/cn/series/6b127c02eff776a4
