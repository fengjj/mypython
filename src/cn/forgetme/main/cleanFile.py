import sys
import glob
def cleanFile(uri):
    files = glob.glob(uri)
    for file in files:
        print file
        file = os.path.join(file)
        os.remove(file)
if __name__=='__main__':
    cleanFile(sys.argv[1])
        
