import subprocess
import Qviews
import queryOSM

#This step queries on Overpass to produce a list of Qnumbers


choice = input("Press 1 for to use AreaID and 2 for bbox choice: ")
if choice =='1':
    Key = input("Input Key: ")
    Value = input("Input Value: ")
    Location = input("Input Location: ")
    result = queryOSM.query( Key , Value , Location )
else:
    Key = input("Input Key: ")
    Value = input("Input Value: ")
    bbox = []
    while len(bbox) < 4:
        coordinate = float(input("input bbox coordinates: "))
        bbox.append(coordinate)
    result = queryOSM.boundbox( Key , Value , bbox )
 
print(result)


#Accessing the Q numbers from the large chucnk of JSON files produced from the API 
listofQnumbers = [( data['tags']['wikidata'] ) for data in result['elements'] if data['tags'].get('wikidata',) ]
print(listofQnumbers)
with open("Qnumbers.txt" , 'w' , encoding = 'utf-8') as f:
    for qnr in listofQnumbers:
        f.write(qnr + '\n')
print('file saved as Qnumbers.txt')


subprocess.run(['getQueriedQviews.sh'], shell = True)
