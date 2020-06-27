import os.path
import re
import sys

path = os.path.abspath(os.getcwd())
path1 = path + '/output.txt'
sys.stdout = open(path1, 'w')
mylist = ['/']
pattern = re.compile("(^static\s(.*)).*(?<!;|=)$")
for item in mylist:
    path3 = path + item
    myfiles = [os.path.join(root, name)
               for root, dirs, files in os.walk(path3)
               for name in files]
    for f in myfiles:
        file_name, file_extension = os.path.splitext(f)
        input_file = os.path.join(path, f)
        for i, line in enumerate(open(input_file)):
            for match in re.finditer(pattern, line):
                print('%s:%s:%s' % (input_file,i+1, match.group()))
sys.stdout.close()