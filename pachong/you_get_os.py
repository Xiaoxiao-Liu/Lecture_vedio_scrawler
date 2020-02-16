import os
# p_links是从网页爬虫那边获取到的最后的视频链接，
# 因为我担心放在一个文件里运行会有损内存，毕竟视频数量还是有点多的
# 所以在使用you-get批量下载视频时，我单独写了一个文件来执行
p_links = [["从网页爬虫那边获取到的最后的视频链接"]]
i = 1
lectures_dict = {}
for lectures in p_links:

    lectures_dict[i] = lectures
    i+=1
for j in lectures_dict.keys():
    print(j)
    # 提前编辑好目录
    path = " -o F:\Python_projects\\vedios\Python编程基础\\"+str(j)
    for link in lectures_dict[j]:
        cmd = "you-get "+link+path
        #这里就是you-get批量下载视频并且存到制定目录的核心代码了
        os.system(cmd)

