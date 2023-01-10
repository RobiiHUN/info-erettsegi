import youtube_dl 
import os
import platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')




if os.path.exists('zenek link.txt'):

    #üres sorok és felesleges enterek törlése
    with open('zenek link.txt', 'r') as f:
        lines = f.read().splitlines()


    lines = [line for line in lines if line]


    with open('zenek link.txt', 'w') as f:
        f.write('\n'.join(lines))



#loop használata több zenéhez

    linkek = open('zenek link.txt', 'r')

    for sor in linkek:


        
        if sor != '/n':
        


            def download_audio(yt_url):
                ydl_opts = {
                    'format': 'bestaudio/best',
                    
                    #'restrictfilenames': True,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',            #mp4 ha videot akarunk
                        'preferredquality': '192',
                    }],
                    'outtmpl': '\\frissen letoltve\\%(title)s.%(ext)s'      #célkönyvtár meghatározása
                }

                
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([yt_url])


            yt_url = sor
            download_audio(yt_url)

            print("")
            print("")

else:
    print("Nem talalom a letoltendo linkeket")