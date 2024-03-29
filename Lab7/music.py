import pygame


pygame.init()
pygame.mixer.init()

songs = ["1.mp3", "2.mp3", "3.mp3"]
song_index = 0
current_song = songs[song_index]

def play():
    global songs, song_index, current_song
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()
def next():
    global songs, song_index, current_song
    song_index += 1
    if song_index > len(songs)-1:
        song_index = 0
        current_song = songs[song_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    else:
        current_song = songs[song_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
def previous():
    global songs, song_index, current_song
    song_index -= 1
    if song_index < 0:
        song_index = len(songs)-1
        current_song = songs[song_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    else:
        current_song = songs[song_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        
def pause():
    global songs, song_index, current_song
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


display = pygame.display.set_mode((600, 800))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            if event.key == pygame.K_RIGHT:
                next()
            if event.key == pygame.K_LEFT:
                previous()
            if event.key == pygame.K_SPACE:
                pause()
        
    display.fill((255, 255, 255))
    pygame.display.update()
                