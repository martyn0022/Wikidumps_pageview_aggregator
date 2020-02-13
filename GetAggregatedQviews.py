import sys
import fileinput

def AggregateQviews():
    count = 0
    prev_qnr = None

    for line in fileinput.input():
        if line.startswith('Q') == False:
            pass
        else:
            qnr, views = line.split(' ')
            #print(type(views))
            views = int(views)
            if qnr == prev_qnr:
                count += views
            else: #if qnr != prev_qnr
                #total = str(count)
                print(prev_qnr,count)
                prev_qnr = qnr
                count = views

if __name__ == '__main__':
    AggregateQviews()