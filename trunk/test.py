import os, sys, time

prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
f = open(prgpath + "\\testcron.txt", "ab")
f.write("-"*80 + "\n")
f.write("time: %s\n" % time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time())))
f.write("parameters: %s\n" % sys.argv)
f.write("-"*80 + "\n")
