
import os
url = 'https://www.google.co.uk/imghp?hl=en&tab=wi'

os.system('curl \"' + url + '\" -o out.txt')