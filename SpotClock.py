import tkinter as tk
from tkinter import *
import os
from time import strftime
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

root = tk.Tk()
root.title('Spotclock')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#1d1d1d')

root.attributes('-transparentcolor', 
                '#1d1d1d')

light = PhotoImage(file='brightness.png')
dark = PhotoImage(file='dark.png')

def toggle_dark_mode():
    if root['bg'] == '#1d1d1d':
        root['bg'] = 'white'
        tela['bg'] = 'white'
        saudacao['bg'] = 'white'
        data['bg'] = 'white'
        horas['bg'] = 'white'
        dark_mode_button['image'] = light
        dark_mode_button['bg'] = 'white'
    else:
        root['bg'] = '#1d1d1d'
        tela['bg'] = '#1d1d1d'
        saudacao['bg'] = '#1d1d1d'
        data['bg'] = '#1d1d1d'
        horas['bg'] = '#1d1d1d'
        dark_mode_button['image'] = dark
        dark_mode_button['bg'] = '#1d1d1d'

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Welcome, ' + nome_usuario)

def get_data():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

def get_current_track():
    try:
        current_track = sp.current_user_playing_track()
        if current_track is not None:
            return f"Now playing: {current_track['item']['name']} by {current_track['item']['artists'][0]['name']}"
        else:
            return "No music is currently playing."
    except Exception as e:
        print(f"Error: {e}")
        return "Error: Could not get current playing track."

def update_label():
    current_track = get_current_track()
    label.config(text=current_track)
    root.after(10000, update_label)

dark_mode_button = Button(root, command=toggle_dark_mode)
dark_mode_button.config(image=dark, bd=0, bg='#1d1d1d')
dark_mode_button.pack(pady=10)
tela = tk.Canvas(root, width=600, height=20, bg='#1d1d1d',
                 bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg='#1d1d1d', fg='#000000', font=('Montserrat', 16))
saudacao.pack()
data = Label(root, bg='#1d1d1d', fg='#000000', font=('Montserrat', 14))
data.pack(pady=2)
horas = Label(root, bg='#1d1d1d', fg='#000000',
              font=('Montserrat', 64, 'bold'))
horas.pack(pady=2)

client_id = 'your-client-id' #change for your Spotify Id
client_secret = 'your-client-secret' #change for your Spotify secret
redirect_uri = 'http://localhost:8888/callback'

sp = Spotify(auth_manager=SpotifyOAuth(client_id='your-client-id', #change for your Spotify Id
                                               client_secret='your-client-secret', #change for your Spotify secret
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-read-currently-playing'))


root.title("SpotClock")

label = tk.Label(root, text="", font=('Montserrat', 16))
label.pack(pady=20)



get_saudacao()
get_data()
get_horas()
update_label()
root.mainloop()
