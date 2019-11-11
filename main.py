# -*- coding:utf-8 -*-
import codecs
import os
import sys
from configparser import ConfigParser

# 只扫描特定文件
suffix_name = '.xsh'

# 这是密钥路径
keyLocation = "D:\guuglersa"

def joinString(infolist, keyLocation, iconId):
    fullString = infolist[0] + "=#" + str(iconId) + "#0%" + infolist[1] + "%" + infolist[2] + "%" + infolist[3] + "%%0%-1%%%22%%0%0%0%" + keyLocation + "%%-1%-1%0%0%%1080%%0%0%1#MobaFont%10%0%0%0%15%238,232,213%0,43,54%133,153,0%0%-1%0%%xterm%-1%-1%0,0,0%54,54,54%255,96,96%255,128,128%96,255,96%128,255,128%255,255,54%255,255,128%96,96,255%128,128,255%255,54,255%255,128,255%54,255,255%128,255,255%236,236,236%255,255,255%80%24%0%1%-1%<none>%%0#0# #-1"
    print(fullString)
    return


def convertFile(filePath, fileName):
    config = ConfigParser()
    config.read_file(codecs.open(filePath, "r", "utf-8-sig"))
    name = fileName.replace(".xsh", "")
    ipAddr = config.get("CONNECTION", "Host")
    port = config.get("CONNECTION", "Port")
    username = config.get("CONNECTION:AUTHENTICATION", "UserName")
    infoList = [name, ipAddr, port, username]
    return infoList


def scanDirs(basePath):
    global iconId
    print('basePath', basePath)
    iconId = 41 # 图标ID
    for dirRoot, dirs, dirFiles in os.walk(basePath):
        if iconId == 41:
            SubRep = ''
        else:
            print("")
            patharr = dirRoot.split('\\')
            SubRep = patharr[-1]
        print("[Bookmarks]")
        print("SubRep=%s" % SubRep)
        print("ImgNum=%d" % iconId)
        iconId += 1
        for fileName in dirFiles:
            if fileName.endswith(suffix_name):
                fileFullName = dirRoot + os.sep + fileName
                #print(fileFullName)
                infoList = convertFile(fileFullName, fileName)
                joinString(infoList, keyLocation, iconId)

if __name__ == '__main__':
    xshellpath = sys.argv[1]
    scanDirs(xshellpath)
