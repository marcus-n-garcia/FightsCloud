##Script for crontab task automation
from datetime import datetime
from yt_dlp import YoutubeDL

#Shows current time
print("Current Time: " + datetime.now().strftime("%H:%M"))


#Opens URLS.txt
URLS = open('C:\\Users\\garciamarcu\\Documents\\Haxor\\URLS.txt', 'r')

#Parses URLS.txt and runs yt-dlp each loop with the current line as an argument
for line in URLS:
	print("\n" + line)
	html = line
	#runs yt-dlp for URL
	with YoutubeDL() as ydl:
		ydl.download(html)


#Have code that will take all .mp4 files and copy them to other directory for backups 

#Run this once or twice a week on a cloud server using cron to automate

#Have means of writing URLS to URLS.txt so the server can know what to download

#push downloads to local drive so I can backup 
		
#test commit