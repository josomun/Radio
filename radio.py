import time
import tkinter as tk
import vlc

HEIGHT = 400
WIDTH = 600

url = 'https://stream-relay-geo.ntslive.net/stream'
#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
#Define VLC player
player=instance.media_player_new()
#Define VLC media
media=instance.media_new(url)
#Set player media
player.set_media(media)
playing = False

#define when radio plays and stops
def toggle_radio_on(): 
  global playing
  if not playing:
    player.play()
    playing = True
  else:
    player.stop()
    playing= False

def toggle_radio_off():
  global playing
  if not playing:
    player.play()
    playing = False
  else:
    player.stop()
    playing= True

#create window
root = tk.Tk()

canvas = tk.Canvas(height=HEIGHT, width=WIDTH)
canvas.pack()
# background_image = tk.PhotoImage(file='background_on.png')
# background_label= tk.Label(image=background_image)
# background_label.place(relwidth=1, relheight=1)

# playButtonImage = tk.PhotoImage(file="background_off.png")
# playButton = tk.Button(root, command = toggle_radio_off)
# playButton.config(image = playButtonImage)
# playButton.place(x=0, y=0)

stopButtonImage = tk.PhotoImage(file="background_on.png")
stopButton = tk.Button(root, command = toggle_radio_on)
stopButton.config(image = stopButtonImage)
stopButton.place(x=0, y=0)
# playButton.place(x=375, y=225)


root.mainloop()
