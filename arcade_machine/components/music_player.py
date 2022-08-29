from pygame import mixer

def load_music(track):
    if mixer.get_busy():
        stop_music()
    mixer.music.load(track)

def play_music(loops):
    mixer.music.play(loops)

def stop_music():
    mixer.music.stop()

def music_volume(value):
    mixer.music.set_volume(value)

def get_volume():
    return mixer.music.get_volume()

if __name__ == "__main__":
    pass