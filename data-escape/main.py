
import os
import re
def extractURLs(fileContent):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', fileContent.lower())
    for i in urls:  ##olmadığı zaman -1 döndürür
        print(i)
        c = str(i.find("http"))
        if c == "0":
            if i != "http://www.w3.org/2000/svg":
                if i != "https://www.tiktok.com/":
                    os.system(f"echo {i} >> link.txt")
    return urls



myFile = open("data.txt",encoding='utf8')
fileContent = myFile.read()

        
URLs = f"URLs  {extractURLs(fileContent)}"




