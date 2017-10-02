# -*- coding: UTF-8 -*-

import os
import json
import shutil

source = os.path.realpath(__file__)
path = os.path.split(source)[0]

dirList = os.listdir(path)
fileList = []
for dirName in dirList:
    if not os.path.isfile(dirName):
        dirName = path + os.sep + dirName
        fileList = fileList + [dirName + os.sep + f for f in os.listdir(dirName) if f.endswith(".json")]
        target = os.path.join(dirName, "void_file")
        if not os.path.exists(target):
            os.mkdir(target)
        else:
            pass

for i in fileList:
    with open(i, 'r') as f:
        data = json.loads(f.read())
        print "this json is intact >>> " + i

    if ((data[u'Point'] == [] or data[u'Point'] is None) or
            (data[u'Answers'] == [] or data[u'Answers'] is None) or
            data[u'ID'] is None or
            (data[u'Degree'] == [] or data[u'Degree'] is None) or
            (data[u'Label'] == [] or data[u'Label'] is None) or
            (data[u'Analyse'] == [] or data[u'Analyse'] is None) or
            (data[u'Content'] == [] or data[u'Content'] is None) or
            (data[u'Method'] == [] or data[u'Method'] is None) or
            (data[u'Discuss'] == [] or data[u'Discuss'] is None)):
        recover_file = os.path.split(i)[0] + os.sep + "void_file"
        shutil.move(i, recover_file)
        print "this json is NOT intact"
    elif data[u'Options'] == [] or data[u'Options'] is None or None in data[u'Options']:
        recover_file = os.path.split(i)[0] + os.sep + "void_file"
        shutil.move(i, recover_file)
        print "this json is NOT intact"
    else:
        pass