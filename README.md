# A python script designed to download every YouTube video and convert it to an mp3 from a WhatsApp Web conversation using yt-dlp. 
Running the script opens up Firefox and takes you to WhatsApp web. Sign in (you only need to do this once), and click on a conversation. Any youtube.com or youtu.be link in that conversation (either sent by you or the other person) will be downloaded and converted to mp3 in the directory where the script is, in a folder called "output".  
**You can easily change the format and other properties of the downloaded video by changing the argument of the os.system() function in the script. It's just yt-dlp**  

This simple script was made for my personal use. It works on my machine, for my specific use case, at the time of writing.  
It is NOT guaranteed (or expected) that it will work on your machine, for your specific use case, at the time of reading.  
But it's here, in case anyone potentially gets some value out of it.  

## Running
- Make sure python and all the dependencies are installed and working.
- Create an empty folder named "output".
- Create a file named "dlp_links.txt", containing exactly: set()
- Create a file named "seen_links.txt", containing exactly: set()
- Run the file using python in a terminal: `python script.py`

(Also, the script should automatically create a folder named "whatsapp_profile".)

## Platform Support
- **Linux**: Works (tested)
- **Mac**: Should work (untested)
- **Windows**: Will NOT work (uses bash-style `&&` in os.system). It should be an easy fix though, just change the argument of the os.system() function.

## This script is VERY fragile.
Even if everything works, it could easily download/not download some videos that it should not have because it makes heavy use of random patterns I found that aren't generally true for every case. 
If any change is made to WhatsApp, YouTube, yt-dlp or the python libraries I used, it could easily stop functioning properly.  
There is also no error handling, it has to be force stopped by the user (CTRL + C or quit the browser opened by playwright), and the user has almost no knowledge or control of what the script is doing.
The way it works is simple: It loads up a browser using playwright, collects all the links (HTML a tags) and converts the links one by one to a format that yt-dlp can handle, and then calls yt-dlp for every link.

## Dependencies
- Python 3.x
- yt-dlp  
- Playwright  

## The environment the script was tested in:
OS: Arch Linux  
Python Version: 3.13.11  
Playwright Version: 1.57.0  

## License
Do whatever you want  

Thank you for reading this! :)
