import os
import math

# 파일들이 저장된 경로


# 딕셔너리 안에 모든 데이터 프레임 저장
def getfiles(dir):
    files = []
    os_file_list = os.listdir(dir)
    for file in os_file_list:
        files.append(dir+f"\\{file}")
    return files
#
# print(getfiles(r"C:\Users\User\Desktop\workspace\autolelse\videos"))