from pygame import mixer

def create_sound(track):
    return mixer.Sound(track)

def play_sound(track):
    mixer.Sound.play(track)

def stop_sound(track):
    mixer.Sound.stop()

def set_volume(sound):
    sound.set_volume(mixer.music.get_volume())

if __name__ == "__main__":
    pass