import csv
from service.elastic import client_elastic



def main(): 
    with open("lib/poi-nonindo.csv", 'r', encoding='utf-8-sig') as file_csv:
        readers = csv.DictReader(file_csv, delimiter=';')
        datas = [read for read in readers]
    client_elastic.run(datas=datas)


if __name__ == "__main__": 
    main()