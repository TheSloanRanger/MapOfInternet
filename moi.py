from numpy import unicode_
import requests
import subprocess
import random
import os

scraped = list()



def scrape(url):

    global depth
    
    depth = depth + 1
    print(depth)
    
    scraped.append(url)

    os.system('curl \"' + url + '\" -o moi.txt')

    moi = open('moi.txt', 'r', errors="ignore")

    text = moi.read()

    text = text.split('>')



    for line in text:
        if "HREF=\"https" in line:
            print("Link Found!")
            position = line.find("HREF=\"https")
            string = ''
            for i in range(position+6, len(line)):
                if line[i] == '\"':
                    break
                string = string + line[i]
            print(string)
            

            new_url = url.replace('/', '-')
            new_url = new_url.replace(':', '=')
            new_url = new_url.replace('?', '')
            new_url = new_url.replace('&', 'and')

            # if string not in scraped and depth < 8:
            #     scrape(string) # recursively follow link
                

            string = string.replace(':', '=')

            string = string.replace('?', '')
            string = string.replace('&', 'and')
            string = string.replace('\n', '')
            
            out = open("C:\\Users\\mrben\\Desktop\\MapOfInternet\\" + new_url + ".md", 'a', encoding='windows-1252')
            out.write("[[" + string.replace('/', '-') + "]]\n")
            out.close()

            

                
        
        if "href=\"https" in line:
            position = line.find("href=\"https")
            string = ''
            for i in range(position+6, len(line)):
                if line[i] == '\"':
                    break
                string = string + line[i]
            print(string)

            new_url = url.replace('/', '-')
            new_url = new_url.replace(':', '=')
            new_url = new_url.replace('?', '')
            new_url = new_url.replace('&', 'and')

            # if string not in scraped and depth < 8:
            #     scrape(string) # recursively follow link


            string = string.replace(':', '=')

            string = string.replace('?', '')
            string = string.replace('&', 'and')
            string = string.replace('\n', '')
            
            
            out = open("C:\\Users\\mrben\\Desktop\\MapOfInternet\\" + new_url + ".md", 'a', encoding='windows-1252')
            out.write("[[" + string.replace('/', '-') + "]]\n")
            out.close()

    depth = 1

            



url_list = open('urls.txt', 'r', encoding='windows-1252')

u = url_list.readline()

depth = 1

while u:
    scrape('https://www.' + u.replace('\n', ''))
    u = url_list.readline()




    

# scrape('https://www.youtube.com')
# scrape("https://www.twitch.tv")
        