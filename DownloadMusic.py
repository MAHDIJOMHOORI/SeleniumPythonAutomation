from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import wget,platform,time,os,sys

options=Options()
options.add_argument('-headless')
if platform.system =='windows':
    driver = Firefox(executable_path='geckodriver.exe')
else:
    driver = Firefox(executable_path='geckodriver',options=options)

def Download_Music(name):    
    try:        
        driver.get('https://www.mp3juices.cc/')    
        driver.find_element_by_css_selector('#query').send_keys(name,Keys.ENTER)
        time.sleep(3)
        source=driver.page_source
        soup=BeautifulSoup(source,'lxml')
        count_music=0
        name_music_k=[]
        for elem in soup.find_all('div',class_='result'):
            name_music=elem.find('div',class_='name').getText()
            name_music_k.append(name_music)
            count_music+=1            
            print('{} name: {}'.format(count_music,name_music))
        try:        
            select_music=int(input('\nEnter Your Desired Song Number:‌'))
            if select_music > count_music :
                print('Error input!! ')        
        except Exception:
            print('Error input!! ')
            select_music=int(input('\nPlease Give Me The Song Number:‌ '))
        driver.find_element_by_xpath('//*[@class="download {}"]'.format(select_music)).click()        
        time.sleep(4)
        soup2=BeautifulSoup(driver.page_source,'lxml')
        link_download=soup2.find('div',id='download_{}'.format(select_music)).find('div',class_='options').find('a',class_='url').get('href')        
        Download=wget.download(link_download,'Music/{}/{}.mp3'.format(name,name_music_k[select_music]))
        driver.close()
    except Exception:    
        print('Connection Error Please Checking The Network And Try Again.')
        driver.close()
        
def main():    
    if platform.system =='Windows':
        os.system('cls')
    else:
        os.system('clear')
    Music=input('Please enter the name of the singer or song or country you are looking for:\nEnter:')
    time.slepp(2)
    print('processing...\n')    
    if os.path.isdir('Music/{}'.format(Music)):
        pass
    else:
        os.mkdir('Music/{}'.format(Music))
    Download_Music(Music)

if __name__=='__main__':
    main()            
    
    





