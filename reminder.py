from SpeechRecognition import speech,textTospeech
import sqlite3,time,datetime
from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time


class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(classAtom, "Taskbar", style, \
                                 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                                 0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(hinst, iconPathName, \
                              win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, \
                          hicon, "Balloon  tooltip", title, 200, msg))
        # self.show_balloon(title, msg)
        time.sleep(10)
        DestroyWindow(self.hwnd)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.


def balloon_tip(title, msg):
    w = WindowsBalloonTip(msg, title)


def getMax(db,table_name):
    try:
        sql="select max({}_id) from {}".format(table_name,table_name)
        res=db.execute(sql)
        count=int(res.fetchone()[0])
        return count+1
    except:
        return 1

def createTable(db,table_name):
    query='create table if not exists {} ({}_id  integer not NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT, {}_name text ,{}_time TEXT )'.format(table_name,table_name,table_name,table_name)
    db.execute(query)

def connectDb():
    dbname='disk'
    conn = sqlite3.connect('{}.db'.format(dbname))
    db = conn.cursor()
    return db,conn

def insertTable(db,table_name,reminder_id,reminder_name,reminder_time):
    sql="insert into  {} values ( {} , '{}',  '{}')".format(table_name,reminder_id,reminder_name,reminder_time)
    #print sql
    db.execute(sql)


def getReminderTime(db,table_name):
    sql= "select {}_time,{}_name from {}".format(table_name,table_name,table_name)
    print sql
    res=db.execute(sql)
    temp=res.fetchall()
    return temp


def convertTime(t):
    t=t.split(" ")
    temp=[]
    if t[1] == 'p.m.' :
        temp.append(str(int(t[0].split(':')[0])+12))
    else:
        temp.append(str(int(t[0].split(':')[0])))

    temp.append(str(int(t[0].split(':')[1])))
    temp=':'.join(temp)
    print temp
    return temp

"""
def convertDate(date):
    date=date.lower()
    date=date.split(" ")
    temp=[]
    temp.append(date[0])
    date=date[1]
"""
def reminder():
    db,conn = connectDb()
    table_name='reminder'
    createTable(db,table_name)


    textTospeech("what is reminder subject ?")
    reminder_subject=speech()

    """
    textTospeech("what is the reminder date ?")
    reminder_date=speech()
    """

    textTospeech("what is reminder time ?")
    reminder_time=speech()
    print reminder_time
    reminder_time=convertTime(reminder_time)

    print reminder_subject, reminder_time

    reminder_id=getMax(db,table_name)

    insertTable(db,table_name,reminder_id,reminder_subject,reminder_time)
    #print datetime.datetime.now()
    conn.commit()
    db.close()
    conn.close()


def checkReminder():
    t=str(datetime.datetime.now())
    #t=t.split(" ")
    t=t.split(" ")[1]
    t=t.split(":")
    #print t
    t=":".join(t[:2])
    #print t
    db,conn=connectDb()
    reminderlist=getReminderTime(db,table_name='reminder')
    #print reminderlist
    for x in reminderlist:
        if  x[0] == t :
            balloon_tip(x[1],x[1])

if __name__ == '__main__':
    checkReminder()
    #reminder()
    #reminder()
    #convertTime('8:15 p.m.')
