from os import link
from PySide2.QtWidgets import QMainWindow, QApplication,QFileDialog,QInputDialog
from PySide2.QtGui import QImage,QPixmap
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont
import requests
# from PySide2.QtCore import QTimer,QAbstractTableModel,Qt,QCoreApplication
from ui_main import Ui_MainWindow
import sys
import requests 
from bs4 import BeautifulSoup
import re
import os


class MainWindow(QMainWindow):
    
    def __init__(self):
        self.url = []
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # select a directory to save all images
        self.path = self.ui.create_dir.clicked.connect(self.create)
        # add new links to your list
        self.ui.add.clicked.connect(self.link)
        # download all your images
        self.ui.download.clicked.connect(self.scrape)
        # delete all links
        self.ui.remove.clicked.connect(self.clear)
        # LEAVE SESSION
        self.ui.quit.clicked.connect(self.close)

        ## SHOW ==> MAIN WINDOW ##
        self.show()
        ## ==> END ##
        
    def create(self):
        """this function is to get the path of a directory"""
        self.path = str(QFileDialog.getExistingDirectory())
        self.ui.path_dir.setText(str(self.path))
        return self.path

    def link(self):
        """this function is to add links to a list or url"""
        link, done = QInputDialog.getText(self, 'Input Dialog', 'Enter your link:')
        self.url.append(link)
        display = '\n'.join([str(elem) for elem in self.url])
        self.ui.data_links.setText(display)

    def scrape(self):
        """this function will initiate web scraping throught all the web pages """
        try:
            self.get_images()
        except:
            font = QFont()
            font.setPointSize(12)
            self.ui.downloaded.setFont(font)
            self.ui.downloaded.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                             u"color: rgb(255, 0, 0);")
            self.ui.downloaded.setText('an error has occured \nplease verify if the directory and link names are viable')

    def clear(self):
        """this will clear all our list"""
        self.url.clear()
        self.ui.data_links.clear()
        self.ui.path_dir.clear()
        self.ui.downloaded.clear()

    def get_images(self):
        counter = 0
        done = []
        for i in range(len(self.url)):
            htmldata = getdata(self.url[i]) 
            soup = BeautifulSoup(htmldata, 'html.parser') 
            for item in soup.find_all('img', {'src':re.compile('.jpg')}, {'src':re.compile('.png')}):
                try:
                    img_data = requests.get(item['src']).content
                    with open(self.path+'/img'+str(counter)+'.jpg', 'wb') as handler: # this will save your image in path as name
                        handler.write(img_data)                   # this will save the image
                    done.append('#'*10+str(item)+'##### downloaded #####')
                    self.ui.downloaded.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                             u"color: rgb(0, 153, 0);")
                    font = QFont()
                    font.setPointSize(12)
                    self.ui.downloaded.setFont(font)
                    self.ui.downloaded.setText('all : {} images found have been succesfully downloaded'.format(len(done)))
                except Exception as e:
                    print(e)
                    print(item['src'])
                counter= counter + 1

def getdata(url): 
    r = requests.get(url) 
    return r.text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
