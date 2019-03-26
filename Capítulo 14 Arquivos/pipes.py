import os
cmd = 'dir /s'
fp = os.popen(cmd) #permite usar python como cmd
print(fp)
res = fp.read()
print(res)
stat = fp.close()
print(stat)

filename = 'book.tex'
cmd = 'md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)