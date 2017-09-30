# coding:utf-8

import os
import json
import shutil

source = os.path.realpath(__file__)
path = os.path.split(source)[0]
target = os.path.join(path, "void_file")

os.mkdir(target)

a = [path + os.sep + i for i in os.listdir(path) if i.endswith('.json')]

for i in a:
    with open(i, 'r') as f:
        data = json.loads(f.read())
        print "this file has been dealed >>> " + i
        if (data[u'Point'] is None and
                    data[u'Options'] is None and
                    data[u'Answers'] is None and
                (data[u'blank_answer'] == [] or data[u'blank_answer'] is None)):
            shutil.move(i, target)
            print "this file has been moved. "
        else:
            pass
