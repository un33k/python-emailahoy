import popen2
import re

mx_re = re.compile('mail\sexchanger\s=\s(\d+)\s(.*)\.')

def query_mx(host):
    mx = []
    addr = {}
    fout, fin = popen2.popen2('which nslookup')
    cmd = fout.readline().strip()
    if cmd <> '':
        fout, fin = popen2.popen2('%s -query=mx %s' % (cmd, host))
        line = fout.readline()
        while line <> '':
            m = mx_re.search(line.lower())
            if m:
                mx.append((eval(m.group(1)), m.group(2)))
            line = fout.readline()

        if mx:
            mx.sort()
    return mx

# 
# if __name__ == "__main__":
#     print query_mx('google.com')