## script by intuol

import urllib.parse
from urllib.parse import quote
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def app():
     print(f"{Fore.GREEN}Paramount GLIM Video Downloader v3 (Howlin Out Edition)")
     print("1. UAT-Glim-OperationsConsole; (Good for Viacom Shows)")
     print("2. PitchNew; (Good for Syndicated Shows)")
     print("3. C3; (Good for VOD Archive)")
     url = int(input("Input CDN: \n"))
     if url == 1:
           endpoint = 'https://uat-glim-operationsconsole.paramountmsc.com'
           path = input("Input Path for Video File: \n")
           print("Encoding URL Path")
           encodedpath = quote(path)
           print(f'Checking Video Quality for {path}')
           subprocess.call(f'yt-dlp -F "{endpoint}/play/master.m3u8?path={encodedpath}&startFrame=0&frameCount=0&res=1920x1080,0x0&open=false"')
           quality = input(f'Pick Video Quality \n (bestvideo for Highest Video Quality): ')
           subprocess.call(f'yt-dlp --external-downloader ffmpeg -f {quality} "{endpoint}/play/master.m3u8?path={encodedpath}&startFrame=0&frameCount=0&res=1920x1080,0x0&open=false"')
           exit()
           
     elif url == 2:
           endpoint = 'https://pitchnew.paramount.tech/'
           path = input("Input Path for Video File: \n")
           print("Encoding URL Path")
           encodedpath = quote(path)
           print(f'Checking Video Quality for {path}')
           subprocess.call(f'yt-dlp -F "{endpoint}/play/master.m3u8?path={encodedpath}&startFrame=0&frameCount=0&res=1920x1080,0x0&open=false"')
           quality = input(f'Pick Video Quality \n (bestvideo for Highest Video Quality): ')
           subprocess.call(f'yt-dlp --external-downloader ffmpeg -f {quality} "{endpoint}/play/master.m3u8?path={encodedpath}&startFrame=0&frameCount=0&res=1920x1080,0x0&open=false"')
           exit()
           
     elif url == 3:
           endpoint = 'https://c3.paramount.tech/'
           path = input("Input Path for Video File: \n")
           print("Encoding URL Path")
           encodedpath = quote(path)
           print(f'Checking Video Quality for {path}')
           subprocess.call(f'yt-dlp -F "{endpoint}/play/master.m3u8?path={encodedpath}&startFrame=0&frameCount=0&res=1920x1080,0x0&open=false"')
           quality = input(f'Pick Video Quality \n (bestvideo for Highest Video Quality): ')
           subprocess.call(f'yt-dlp --external-downloader ffmpeg -f {quality} "{endpoint}/play/master.m3u8?path={encodedpath}&startFrame=0&frameCount=0&res=1920x1080,0x0&open=false"')
           exit()
           
     else:
           print(f'{Fore.RED}Error: Please select 1, 2, or 3.')
           exit()
print("This program is currently a work in progress. Do not expect everything to work 100%.")
print(f"{Fore.RED}Also note that this tool, and the various GLIM instances on Paramount's website, are not supposed to be seen by the general public. The general use of this tool is considered copyright infringement.")
yesno = input("With that being said, do you continue to use this downloader? (Type Y or N): \n")

if yesno == "Y":
      app()
else:
     exit()
