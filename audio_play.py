import pygame
import time

pygame.mixer.init()
pygame.mixer.set_num_channels(8)

#loading audio
drums = pygame.mixer.Sound("music/drums.wav")
bass = pygame.mixer.Sound("music/bass.wav")
synths = pygame.mixer.Sound("music/synths.wav")

#channel for each audio
drums_channel = pygame.mixer.Channel(0)
bass_channel = pygame.mixer.Channel(1)
synths_channel = pygame.mixer.Channel(2)

#looping
drums_channel.play(drums,loops=-1)
bass_channel.play(bass,loops=-1)
synths_channel.play(synths,loops=-1)

#mute at start
drums_channel.set_volume(0.0)
bass_channel.set_volume(0.0)
synths_channel.set_volume(0.0)

def drums_set(x):
    drums_channel.set_volume(x)

def bass_set(x):
    bass_channel.set_volume(x)

def synths_set(x):
    synths_channel.set_volume(x)

def stop_music():
    pygame.mixer.stop()

