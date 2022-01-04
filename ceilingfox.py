import psycopg2, psycopg2.extras
import os
import configparser
from random import *

def CeilingfoxPost():
    data=[]
    emojilist = open((os.path.join(os.path.dirname(__file__), 'blobfox')),'r',encoding='utf-8')
    data=emojilist.read().splitlines()
    emojilist.close()
    seed()
    zahl = randint(0,len(data)-1)
    return "$[rotate.deg=180 :"+data[zahl]+":]"
    
def CeilingfoxStory():
    text=""
    data=[]
    emojilist = open((os.path.join(os.path.dirname(__file__), 'blobfox')),'r',encoding='utf-8')
    data=emojilist.read().splitlines()
    emojilist.close()
    seed()
    zahl = randint(5,10)
    for i in range(zahl):
        emoji = randint(0,len(data)-1)
        text+="$[rotate.deg=180 :"+data[emoji]+":]"
    return text
    
def CeilingfoxYesNo():
    text=""
    seed()
    coin = randint(0,100)
    if (coin<=45):
        text="$[rotate.deg=180 :vlpnsayyes:]"
    elif (coin>45 and coin<55):
        text="$[rotate.deg=180 :blobfoxconfused:]"
    elif (coin>=55):
        text="$[rotate.deg=180 :vlpnsayno:]"
    else:
        text="$[rotate.deg=180 :vlpnsayyip:]"
    return text
    
def CeilingfoxNumber():
    fox=""
    text=""
    seed()
    emoji=randint(0,1)
    if emoji==1:
        fox=":blobfoxsignnoublush:"
    else:
        fox=":blobfoxsignnou:"
    number=randint(0,9)
    text="$[rotate.deg=180 "+fox+"\n\(\\\\[-18mu]\)$[rotate.deg=5 \(\scriptsize\colorbox{white}{\hspace{6mu}\\textcolor{black}{"+str(number)+".}\hspace{6mu}}\)]]"
    return text

def LoadEmojis():
    text=[]
    dirname=""
    
    #Load Postgres configuration
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'bot.cfg'))
    
    misskeydb = psycopg2.connect(
        host=config.get("postgres","host"),
        database=config.get("postgres","database"),
        user=config.get("postgres","user"),
        password=config.get("postgres","password"))
    
    mkcur = misskeydb.cursor(cursor_factory=psycopg2.extras.DictCursor)
    mkcur.execute('SELECT name FROM emoji WHERE host IS NULL;')
    rows=mkcur.fetchall()
    
    dir=os.path.split(__file__) #Array with two Elements
    dirname=dir[0]

    for row in rows:
        if (row['name'].startswith("blobfox") or (row['name'].startswith("vlpnsay") and not row['name']=="vlpnsay" and not row['name']=="vlpnsaynervous" and not row['name']=="vlpnsayhappy") or row['name']=="flanfox" or row['name']=="foxjump" or row['name'].startswith("mcfoxspin")): 
            text.append(f"{row['name']}")

    file = open(dirname+'/blobfox', 'w')
    for line in text:
        file.write(line + "\n")
    file.close()
    
    mkcur.close()
    misskeydb.close()