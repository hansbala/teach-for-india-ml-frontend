
#!/bin/bash
#Getting the files
wget "http://www.dropbox.com/sh/vfvw7k4ikjgyb7f/AABQ7-NZkX9Xex5X-WEWr2D9a?dl=1" -O ~/Downloads/tfipy.zip
mkdir ~/.tfipy
unzip ~/Downloads/tfipy.zip -d ~/.tfipy

#Getting the executable
wget "http://www.dropbox.com/s/yyj4qb4mt1s08pv/TFI_Platform_v1.0_Linux?dl=1" -O ~/Downloads/TFIexec
cp ~/Downloads/TFIexec ~/.tfipy/CodingPlatform
chmod +x ~/.tfipy/CodingPlatform
ln -s ~/.tfipy/CodingPlatform ~/Desktop

clear
echo "ALL DONE"
echo "LAUNCH IT BY CLICKING ON THE FILE ON YOUR DESKTOP"