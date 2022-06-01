import pafy
url = input('Enter your link: ')
video = pafy.new(url)
streams = video.streams
for s in streams:
   print(s)