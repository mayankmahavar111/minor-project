import time
from selenium import webdriver
import os


"""
def search(text):
    driver = webdriver.Chrome('G:\minor project\chromedriver.exe')
    driver.get('http://www.google.com')
    time.sleep(1)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(text)
    search_box.submit()
    time.sleep(5)
#search("mayank mahavar")
"""

def search(text):
    text=text.lower()
    if 'youtube' in text:
        search_youtube(text.split('youtube')[1])
    else:
        search_cmd(text)

def search_cmd(text):
    os.system(""" start firefox  "? {}" """.format(text))

def open_url(url):
    os.system(""" start firefox "{}" """.format(url))

def search_youtube(key):
    os.system(""" start firefox "https://www.youtube.com/results?search_query={}" """.format(key))



if __name__ == '__main__':
    #open_url('nitk.com')
    search("YouTube sick boy")