import os
import sqlite3
import string
from assistant import textTospeech

def check(location):
    if " " in location:
        temp=location.split('\\')
        test=[]
        for x in temp:
            if " " in x:
                test.append('"'+x+'"')
            else:
                test.append(x)
        location="\\".join(test)
        return location
    return location

def displayresult(result):
    for i in range(len(result)):
        text= str(i+1)+" : "+ str(result[i][1]) + "\t location is :"+result[i][2].split('\\')[-1]
        print(text)
        textTospeech("location is ")
        textTospeech(text.split(":")[-1])

"""
def getResult(file,db):
    tables=['document','images','programs','misc','music','videos']
    data=[]
    for table in tables:
        sql="select * from {} where {}_nickname like "%{}%"".format(table,table,file)
        res = db.execute(sql)
        result=res.fetchall()
        print(result)
    return data
"""


def program(file,db):
    sql = """select * from programs where programs_nickname like "%{}%" """.format(file)
    # print(sql)
    res = db.execute(sql)
    result = res.fetchall()
    # print(len(result))
    if len(result) == 0:
        print("Nothing like that exists")
        return
    if len(result) > 1:
        displayresult(result)
        index = int(input("Which {}".format(file)))
        file_name = result[index - 1][1]
        location = result[index - 1][2]
        location = check(location)
        print(location)
        path = str(location) + "\\" + str(file_name)
        # path=check(path)
        print(path)
        os.system(path)
    else:
        file_name = result[0][0]
        location = result[0][1]
        path = str(location) + "/" + str(file_name)
        os.system(path)

def getDocumentapp(file,db):
    if file.endswith('pdf'):
        sql = """select * from misc where misc_nickname="{}" """.format("Acrobat Reader DC")
        # print(sql)
        res = db.execute(sql)
        result = res.fetchall()[0]
        print(result)
        location=check(result[1])
        path = str(location) + "\\" + check(str(result[0]))
        return path
    elif file.endswith('.txt'):
        """
        sql = ""select * from programs where programs_nickname="{}"".format("notepad")
        # print(sql)
        res = db.execute(sql)
        result = res.fetchall()[0]
        print(result)
        location = check(result[1])
        path = str(location) + "\\" + check(str(result[0]))
        """
        return "notepad"




def document(file,db):
    sql = """select * from document where document_nickname like "%{}%" """.format(file)
    # print(sql)
    res = db.execute(sql)
    result = res.fetchall()
    if len(result) == 0:
        print("Nothing like that exists")
        return
    if len(result) > 1:
        displayresult(result)
        index = int(input("Which {}".format(file)))
        file_name = result[index - 1][1]
        location = result[index - 1][2]
        location = check(location)
        print(location)
        #app=getDocumentapp(file_name,db)

        #path =app+" "+ str(location.replace('\\','/')) + "\\" + str(file_name.replace('\\','/'))
        # path=check(path)
        file_name=check(file_name)
        path= str(location.replace('\\','/')) + "\\" + str(file_name.replace('\\','/'))
        print(path)
        os.system(path)
    else:
        file_name = result[0][0]
        location = result[0][1]
        #app = getDocumentapp(file_name, db)
        #path = app + " " + str(location.replace('\\', '/')) + "/" + str(file_name.replace('\\', '/'))
        file_name = check(file_name)
        path= str(location.replace('\\','/')) + "\\" + str(file_name.replace('\\','/'))
        print(path)
        os.system(path)




def files(file,table_name,db):
    sql = """select * from {} where {}_nickname like "%{}%" """.format(table_name,table_name,file)
    # print(sql)
    res = db.execute(sql)
    result = res.fetchall()
    if len(result) == 0:
        print("Nothing like that exists")
        return
    if len(result) > 1:
        displayresult(result)
        index = int(input("Which {}".format(file)))
        file_name = result[index - 1][1]
        location = result[index - 1][2]
        location = check(location)
        print(location)
        # app=getDocumentapp(file_name,db)

        # path =app+" "+ str(location.replace('\\','/')) + "\\" + str(file_name.replace('\\','/'))
        # path=check(path)
        file_name = check(file_name)
        path = str(location.replace('\\', '/')) + "\\" + str(file_name.replace('\\', '/'))
        print(path)
        os.system(path)
    else:
        file_name = result[0][0]
        location = result[0][1]
        # app = getDocumentapp(file_name, db)
        # path = app + " " + str(location.replace('\\', '/')) + "/" + str(file_name.replace('\\', '/'))
        file_name = check(file_name)
        path = str(location.replace('\\', '/')) + "\\" + str(file_name.replace('\\', '/'))
        print(path)
        os.system(path)


def fileopen(file):
    conn = sqlite3.connect('disk.db')
    db = conn.cursor()
    #print("app" in file)
    tables = ['programs', 'document', 'videos', 'music', 'images', 'misc']
    if "app" in file:
        file=file.split("app ")[1]
        print(file)
        #program(file,db)
        files(file,tables[0],db)
    elif "document" in file:
        file = file.split("document ")[1]
        print(file)
        #document(file,db)
        files(file,tables[1],db)
    else:
        print("Sorry unable to understand the file type please try again using "+'\napp'+'\ndocument'+'\nat start')

if __name__ == '__main__':
    temp = input("Enter file name :")
    fileopen(temp)

