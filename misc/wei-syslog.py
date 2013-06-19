import sys
import getopt
import syslog

# In ubuntu default settings, the msg will log into /var/log/syslog
def contains(opts, patterns):
  return len(filter(lambda x: x[0] in patterns, opts)) == 1

def usage(error=None):
  if (error != None):
    print "ERROR: %s" % (error)
  print "Usage: python wei-syslog.py <msg>"
  sys.exit(-1)

def logit(msg):
    syslog.openlog("touch-syslog.py", syslog.LOG_PID)
    syslog.syslog(syslog.LOG_INFO, str(msg))

def main():
  try:
    (opts, args) = getopt.getopt(sys.argv[1:], "h",
      ["help"])
  except getopt.GetoptError:
    usage()
  if (contains(opts, ("-h", "--help"))):
    usage()
  else:
    logit(args[0])

if __name__ == "__main__":
  main()