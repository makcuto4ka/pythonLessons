import pygame
from mutagen.mp3 import MP3
import os
import time

class MP3Player:
    def __init__(self):
        pygame.mixer.init()


    def load(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} not found")
        
        self.file_path = file_path
        pygame.mixer.music.load(file_path)
        
        audio = MP3(file_path)
        self.duration = audio.info.length

    def play(self):
        pygame.mixer.music.play()
        self.is_paused = False


    def set_volume(self, volume):
        pygame.mixer.music.set_volume(0.5)



    def get_duration(self):
        return self.duration


player = MP3Player()
player.load("/home/maksim/ВУЗ/pythonLessons/ООП/test.mp3") 


volume1=float(input('Выберете громкость от 0 до 1: '))
print(f"Длительность трека: {player.get_duration():.2f} сек")
time_music=player.get_duration()
player.set_volume(volume1)
t= time.time()
player.play()

while time.time()-t < time_music:
        print(f"\rПроиграно: {round(time.time()-t,2)} сек / {player.get_duration():.2f} сек", end="")
        time.sleep(0.1)

    
