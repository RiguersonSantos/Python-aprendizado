import pygame;

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(R"c:\Users\Gamer\Downloads\Ela - Sorriso Maroto, Ferrugem (Sorriso Eu Gosto No Pagode) - Sorriso Maroto (youtube).mp3")
pygame.mixer.music.play()


print("Tocando...")
input("Pressione Enter para sair")


