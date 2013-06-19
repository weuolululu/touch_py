import sys
import getopt
import os.path
import os
from elementtree import ElementTree

POM_NS = "{http://maven.apache.org/POM/4.0.0}"
global ROOT

def contains(opts, patterns):
  return len(filter(lambda x: x[0] in patterns, opts)) == 1

def usage(error=None):
  if (error != None):
    print "ERROR: %s" % (error)
  print "Usage: python pom-dps.py <pom-full-path>"
  sys.exit(-1)

def print_iterator(name, index):
  global ROOT
  print
  print name + ": "
  if (index == 3):
    print map(lambda dependency: dependency[index].text if len(dependency) > 3 else '', ROOT.findall("//%sdependency" % (POM_NS)))
  else:
    print map(lambda dependency: dependency[index].text, ROOT.findall("//%sdependency" % (POM_NS)))

  # for dependency in ROOT.findall("//%sdependency" % (POM_NS)):
  #   if (index == 3):
  #     print dependency[index].text if len(dependency) > 3 else ''
  #   else:
  #     print dependency[index].text

def parse(pom):
  global ROOT
  ROOT = ElementTree.parse(pom)
  keys = [0,1,2,3]
  names = ["groupIds", "artifactIds", "versions", "scopes"]
  map(print_iterator, names, keys)

def main():
  try:
    (opts, args) = getopt.getopt(sys.argv[1:], "h",
      ["help"])
  except getopt.GetoptError:
    usage()
  if (contains(opts, ("-h", "--help"))):
    usage()
  if (not os.path.exists(args[0])):
    usage("POM file not found: %s" % (args[0]))
  else:
    parse(args[0])

if __name__ == "__main__":
  main()