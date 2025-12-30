This simple script was made for my personal use. It works on my machine, for my specific use case, at the time of writing.
It is NOT guaranteed (or expected) that it will work on your machine, for your specific use case, at the time of reading.
But it's here, in case anyone potentially gets some value out of it.

## This script is VERY fragile.
Even if everything works, it could easily download/not download some videos that it should not have because it makes heavy use of random patterns I found that aren't generally true for every case. 
If any change is made to WhatsApp, YouTube, yt-dlp or the python libraries I used, it could easily stop functioning properly.
There is also no error handling, it has to be force stopped by the user (CTRL + C or quit the browser opened by playwright),
The way it works is simple: It loads up a browser using playwright, collects all the links (HTML a tags) and converts the links one by one to a format that yt-dlp can handle, and then calls yt-dlp for every link.

## Dependencies
(these are the package names used by pacman)
python-playwright 
gtk4
icu
libxml2 
woff2 
libvpx 
flite 
enchant 
libmanette

## Setup
- Create a folder named "output".
- Create an empty file named "dlp_links.txt".
- Create an empty file named "seen_links.txt".

Also, the script should automatically create a folder named "whatsapp_profile".

## The environment I use the script in:
OS: Arch Linux
Python Version: 3.13.11
Playwright Version: 1.57.0

## License
Do whatever you want

Thank you for reading this! :)
