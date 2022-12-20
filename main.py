import os
from pytube import YouTube

os.chdir("C:/Users/przem")


while True:
    try:
        user_link = input("Wklej link z Youtuba:")
        yt = YouTube(user_link)
        print("Title: ", yt.title)
        print("Lenght:", yt.length, "sec")
        mp3 = yt.streams.get_audio_only()
        downloaded_mp3 = mp3.download(output_path="./PobraneMP3/")
        base, ext = os.path.splitext(downloaded_mp3)
        new_file = base + ".mp3"
        os.rename(downloaded_mp3, new_file)
    except:
        print("Podałeś nieprawidłowy link")



