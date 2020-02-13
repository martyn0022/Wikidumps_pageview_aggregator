import sys
import fileinput


def generateQviews():
    prev_qnr = None
    qnr = None
    for i, line in enumerate(fileinput.input()):
        #print("prev_qnr is: {}".format(prev_qnr))
        qnr, *views = line.rstrip('\n').split(' ')
        #print(qnr)
        if qnr != prev_qnr:
            #print('previous qnr and current qnr not the same, updating prev_qnr...\n\n')
            prev_qnr = qnr
        else:
            #print("qnr match, writing to file....")
            #print(type(views))
            views[0] = str(views[0])
            print(prev_qnr , views[0])
            #print("written \n updating prev_qnr...")
            prev_qnr = qnr


if __name__ == '__main__':
    generateQviews()