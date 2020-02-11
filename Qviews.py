def AggregateQviews():
    count = 0
    prev_qnr = None

    with open('sorted_qviews.txt' , 'r' , encoding ='utf-8') as infile:
        with open('AggregatedQviews.txt' , 'a' , encoding = 'utf-8') as outfile:
            for line in infile:
                if line.startswith('Q') == False:
                    pass
                else:
                    qnr, views = line.split(' ')
                    views = int(views)
                    if qnr == prev_qnr:
                        count += views
                    else: #if qnr != prev_qnr
                        total = str(count)
                        outfile.write(f'{prev_qnr} '  + total + '\n')
                        prev_qnr = qnr
                        count = views

def generateQviews():
    prev_qnr = None
    qnr = None
    with open('jointlist.txt', 'r' , encoding = 'utf-8') as infile:
        with open('queried_Qviews.txt' , 'a' , encoding = 'utf-8') as outfile:
            for i, line in enumerate(infile):
                #print("prev_qnr is: {}".format(prev_qnr))
                qnr, *views = line.rstrip('\n').split(' ')
                #print(qnr)
                if qnr != prev_qnr:
                    #print('previous qnr and current qnr not the same, updating prev_qnr...\n\n')
                    prev_qnr = qnr
                else:
                    print("qnr match, writing to file....")
                    print(type(views))
                    views[0] = str(views[0])
                    outfile.write(f'{prev_qnr} '  + views[0] + '\n')
                    print("written \n updating prev_qnr...")
                    prev_qnr = qnr
                    

