# excute shell or dos command

import sys
import getopt
import commands

def contains(opts, patterns):
  return len(filter(lambda x: x[0] in patterns, opts)) == 1

def usage(error=None):
  if (error != None):
    print "ERROR: %s" % (error)
  print "Usage: python wei-excutor.py <msg>"
  sys.exit(-1)

def excute(cmds):
  status, output = commands.getstatusoutput(cmds)
  print "Output: ", output
  print "Status: ", status

def main():
  try:
    (opts, args) = getopt.getopt(sys.argv[1:], "h",
      ["help"])
  except getopt.GetoptError:
    usage()
  if (contains(opts, ("-h", "--help"))):
    usage()
  else:
    excute(args[0])

if __name__ == "__main__":
  main()