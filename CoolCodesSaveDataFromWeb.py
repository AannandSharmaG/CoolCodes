import urllib.request
myFileUrl = "http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv"

def LetsDownloadACsv(csvUrl):
    response = urllib.request.urlopen(csvUrl)
    csvData = response.read()
    csvDataString = str(csvData)
    data = csvDataString.split('\\n')
    fw = open('data.csv','w')
    for line in data:
        fw.write(line+'\n')
    fw.close()
LetsDownloadACsv(myFileUrl)