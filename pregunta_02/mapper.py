#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":
    for line in sys.stdin:
       credit=line [0:-1].split(',')     
       sys.stdout.write("{}\t{}\n".format(credit[3],credit[4]))