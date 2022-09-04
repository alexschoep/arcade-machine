from pygame import mixer

def create_sound(track):
    return mixer.Sound(track)

def play_sound(track):
    mixer.Sound.play(track)

def stop_sound(track):
    mixer.Sound.stop()

if __name__ == "__main__":
    pass