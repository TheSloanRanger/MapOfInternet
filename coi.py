
import os

scraped = list()

def scrape(url):

    global depth
    
    depth = depth + 1
    print("depth: ", depth)

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

            
                

            new_string = string.replace(':', '=')

            new_string = new_string.replace('?', '')
            new_string = new_string.replace('&', 'and')
            new_string = new_string.replace('\n', '')
            
            out = open("C:\\Users\\mrben\\Documents\\MOI\\" + new_url + ".md", 'a', encoding='windows-1252')
            out.write("[[" + new_string.replace('/', '-') + "]]\n")
            out.close()

            if string not in scraped and depth <= 1:
                scrape(string) # recursively follow link

            

                
        
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

            

            new_string = string.replace(':', '=')

            new_string = new_string.replace('?', '')
            new_string = new_string.replace('&', 'and')
            new_string = new_string.replace('\n', '')
            
            
            out = open("C:\\Users\\mrben\\Documents\\MOI\\" + new_url + ".md", 'a', encoding='windows-1252')
            out.write("[[" + new_string.replace('/', '-') + "]]\n")
            out.close()

            if string not in scraped and depth <= 1:
                scrape(string) # recursively follow link

    depth = 0

            

url_list = open('urls.txt', 'r', encoding='windows-1252')

u = url_list.readline()

depth = 0

scrape("https:/www.facebook.com")

    

# scrape('https://www.youtube.com')
# scrape("https://www.twitch.tv")
        