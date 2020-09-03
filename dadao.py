from bs4 import BeautifulSoup, Comment
import os
import asyncio

SOURCE="/Users/john/Documents/大道朝天/"
DEST="./dadao/"

def j(x):
    s = list(map(str,x))
    return ''.join(s)

async def process_html(filename):
    soup=BeautifulSoup(open(SOURCE+filename,encoding="utf8"))
    content=soup.select("#content")
    title=soup.select("title")
    h1=soup.select("h1")
    #print(title)
    #print(content)
    f=open(DEST+filename,'w+')
    html = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
%s
</head>
<body>
%s
%s
</body>
</html>
    '''
    #print(h1[0].contents)
    #print(h1[0])
    f.write(html%(j(title),j(h1),j(content)))
    f.close()
    
#for root, dirs, files in os.walk(SOURCE):
#    for filename in files:
#        print(filename)
async def loop_all():
    import os,sys
    for f in os.listdir(SOURCE):
        try:
            await process_html(f)
        except Exception as e:
            print(f"Exception {e} when process {f}")
        
        sys.stdout.write('.')
        sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(loop_all())
    #asyncio.run(process_html('1000411.html'))

