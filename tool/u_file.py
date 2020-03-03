import os


# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)


# 获取文件大小
def getFileSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)


# 获取文件夹大小
def getDocSize(path):
    sumsize = 0
    try:
        filename = os.walk(path)
        for root, dirs, files in filename:
            for fle in files:
                size = os.path.getsize(path + fle)
                sumsize += size
        return formatSize(sumsize)
    except Exception as err:
        print(err)


# 读取目录下的所有文件，包括嵌套的文件夹
def get_file_list(dir, filelist):
    newDir = dir
    if os.path.isfile(dir):
        filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            if s == ".DS_Store":
                continue
            newDir = os.path.join(dir, s)
            get_file_list(newDir, filelist)
    # 默认顺序排列
    return sorted(filelist, reverse=False)


# 读取目录下的所有文件，包括嵌套的文件夹
def get_dir_files(dir, filelist=[], status=0, str1=""):
    """
    dir: 目录地址
    filelist: 变量地址
    status: 表示是包含 1，取消 0，还是不包含 -1
    str1: 过滤词
    """
    newDir = dir
    if os.path.isfile(dir):
        filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            if status == 1:
                # 如果不包含改字符串就跳过
                if str1 not in s:
                    continue
            elif status == -1:
                # 如果包含改字符串就跳过
                if str1 in s:
                    continue
            newDir = os.path.join(dir, s)
            get_dir_files(newDir, filelist, status, str1)
    # 默认顺序排列
    return sorted(filelist, reverse=False)


def create_path2dir(filename):
    """
    :desc: 创建文件路径的方法
    :param: 
        filename 文件的路径
    :return:
    """
    file_dir = os.path.dirname(filename)
    print(file_dir)
    if os.path.exists(file_dir):
        pass
    else:
        os.makedirs(file_dir)


# if __name__ == "__main__":
#     print(getFileSize("../detailhtml/20161103112313.html"))
#     # 1006.142578kb
#     print(getDocSize("../data/"))
#     # 111.856756M
