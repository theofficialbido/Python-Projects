import pytube
url = input('Enter Video URL: ')
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()
print('Done!')