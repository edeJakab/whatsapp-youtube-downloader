"""
This simple script was made for my personal use. It works on my machine, for my specific use case, at the time of writing.
It is NOT guaranteed (or expected) that it will work on your machine, for your specific use case, at the time of reading.
But it's here, in case anyone potentially gets some value out of it.
"""

from playwright.sync_api import sync_playwright
import time
import ast
import os

INTERVAL = 3.0 # seconds. for the main loop
OUTPUT_FOLDER = "output" # relative path

print("IMPORTANT: You need to manually create some folders and files to make the script work properly, see README.md.", flush=True)

with sync_playwright() as p:
    context = p.firefox.launch_persistent_context(user_data_dir = "whatsapp_profile", headless=False)
    page = context.new_page()
    page.goto("https://web.whatsapp.com")

    # NOTE: i'm using raw python sets here which is a bit of a mess but it works
    seen_links = set() 
    dlp_links = set()
    
    # read in the previously processed links to avoid doing things twice
    with open("seen_links.txt") as file:
        seen_links = ast.literal_eval(file.read())
    
    with open("dlp_links.txt") as file:
        dlp_links = ast.literal_eval(file.read())

    while True:
        start = time.monotonic()

        # finds all the links in the page
        links = page.locator("a[href]")

        # put the links into a list (unique)
        for i in range(links.count()):
            link = links.nth(i).get_attribute("href")
            if link not in seen_links:
                seen_links.add(link)
                print("New link found: ", link, flush=True)
        
        # processing only youtube links
        # extracting the actual video_id from the ugly, tracker-ridden shared links that yt_dlp cant process (maybe it can)
        for link in seen_links:
            is_yt_link = False
            if "youtube.com" in link:
                is_yt_link = True
                pos = link.find("youtube.com")
                # 12 = len("youtube.com") + 1
                start = pos + 12

            if "youtu.be" in link:
                is_yt_link = True
                pos = link.find("youtu.be")
                # 9 = len("youtu.be") + 1
                start = pos + 9

            # e.g. https://youtu.be/u92JoL13T1M?si=SL2Y0YmyzsvGoXlu, start is the position of the second u character in the string.

            if is_yt_link:
                # the position of the character before the s in si=. -1 because it's *si=, where * seems to be either ? or &.
                # e.g. https://youtu.be/u92JoL13T1M?si=SL2Y0YmyzsvGoXlu, end is the position of the first and only ? character in the string.
                end = link.find("si=") - 1

                # a bit of redundancy in case the si= is missing from an otherwise acceptable link.
                if end != -1:
                    video_id = link[start:end]
                else:
                    video_id = link[start:]

                if "playlist" in video_id:
                    template = "https://www.youtube.com/"
                else:
                    template = "https://www.youtube.com/watch?v="

                dlp_link = template + video_id
                if dlp_link not in dlp_links:
                    os.system("cd " + OUTPUT_FOLDER + " && yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 --remote-components ejs:github " + dlp_link)
                    dlp_links.add(dlp_link)
                
        
        # saving the processed links.
        with open("seen_links.txt", "w") as file:
            file.write(str(seen_links))
        
        with open("dlp_links.txt", "w") as file:
            file.write(str(dlp_links))
            
        # limiting the loop to 1 cycle / INTERVAL
        elapsed = time.monotonic() - start
        time.sleep(max(0, INTERVAL - elapsed))
