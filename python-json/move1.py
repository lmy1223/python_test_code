# coding:utf-8

import json
import os
import shutil


def getFileName(oldPath):
    fileList = []
    if not os.path.isfile(oldPath):
        dirList = os.listdir(oldPath)
        for dirName in dirList:
            if os.path.isfile(dirName):
                if dirName.endswith(".json"):
                    fileList = fileList + [oldPath + os.sep + dirName]
                else:
                    pass
            else:
                dirName = oldPath + os.sep + dirName
                fileList = fileList + [dirName + os.sep + f for f in os.listdir(dirName) if f.endswith(".json")]
    else:
        pass
    return fileList


def moveFile(fileList, newPath):
    for file in fileList:
        with open(file, 'r') as f:
            data = json.load(f, "UTF-8")
        if data[u'Point'] is None and data[u'Options'] is None and data[u'Answers'] is None and (data[
                u'blank_answer'] == [] or data[u'blank_answer'] is None):
            oldPath = file
            newPath = newPath
            shutil.move(oldPath, newPath)
        else:
            pass


def main():
    source = os.path.realpath(__file__)
    oldPath = os.path.split(source)[0]
    newPath = "D:\\56\\file_list"
    fileList = getFileName(oldPath)
    # print fileList
    moveFile(fileList, newPath)


if __name__ == '__main__':
    main()
