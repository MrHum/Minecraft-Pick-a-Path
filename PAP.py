import pygame
import sys
import tkinter as tk

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Minecraft Pick-A-Path")

font = pygame.font.Font(None, 36)

images = {
    "instructions": pygame.image.load("Images/Introduction.png"),
    "start": pygame.image.load("Images/choice1.png"),
    "game_over1": pygame.image.load("Images/gameover1.png"),
    "Dark_Cave2": pygame.image.load("Images/choice2.png"),
    "game_over2": pygame.image.load("Images/gameover2.png"),
    "Diamonds": pygame.image.load("Images/choice3.png"),
    "game_over3": pygame.image.load("Images/gameover3.png"),
    "game_over4": pygame.image.load("Images/gameover4.png"),
    "win2": pygame.image.load("Images/win1.png")
}

scenes = {
    "instructions": {
        "description": "Welcome to Minecraft Pick-A-Path! Choose your path wisely. Each choice leads to a unique outcome. Survive and find the diamonds! Click 'Start Game' to begin.",
        "choices": {"Start Game": "start"}
    },
    "start": {
        "description": "You see a lit-up cave and a pitch-black cave. Where do you go?",
        "choices": {
            "Go to the lit-up cave": "game_over1",
            "Go into the dark cave": "Dark_Cave2"
        }
    },
    "Dark_Cave2": {
        "description": "You bravely go through the dark cave and find a light source. Now you find another dark cave above.",
        "choices": {
            "Go up into another dark cave": "game_over2",
            "Continue regular path": "Diamonds"
        }
    },
    "Diamonds": {
        "description": "You continued your path and found diamonds, but they are guarded by two skeletons and zombies. What will you do?",
        "choices": {
            "Fight the mobs with a damaged sword": "game_over3",
            "Fight the mobs with an axe you remembered": "win2",
            "Wait for the mobs to disappear": "game_over4"
        }
    },
    "game_over1": {"description": "Game Over! The light came from lava and you fell before you realized. Great environmental awareness."},
    "game_over2": {"description": "Game Over! You were ambushed by mobs. Take a torch next time."},
    "game_over3": {"description": "Game Over! Your sword broke, and the mobs counter-attacked. Great job."},
    "game_over4": {"description": "Game Over! You waited too long, and a creeper snuck up on you. Boom!"},
    "win2": {"description": "Congratulations! You pulled out your axe, defeated the mobs, and mined the diamonds. You won!"}
}

current_scene = "instructions"

def start_game():
    global current_scene
    current_scene = "start"
    root.quit()

root = tk.Tk()
root.title("Minecraft Pick-A-Path")
root.geometry("300x200")

intro_label = tk.Label(root, text=scenes["instructions"]["description"], wraplength=280, font=("Helvetica", 12))
intro_label.pack(pady=20)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

root.mainloop()

def draw_choices(choices, button_positions):
    for (choice_text, next_scene), pos in zip(choices.items(), button_positions):
        choice_surface = font.render(choice_text, True, (255, 255, 255))
        pygame.draw.circle(screen, (100, 100, 255), pos, 15, 2)
        screen.blit(choice_surface, (pos[0] + 30, pos[1] - 10))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if (mouse_x - pos[0]) ** 2 + (mouse_y - pos[1]) ** 2 < 15 ** 2:
                global current_scene
                current_scene = next_scene

button_positions = {
    "start": [(200, 400), (800, 400)],
    "Dark_Cave2": [(540, 200), (540, 600)],
    "Diamonds": [(400, 300), (700, 500), (540, 400)] 
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(images[current_scene], (0, 0))

    description_text = scenes[current_scene]["description"]
    y_offset = 50
    for line in description_text.split('\n'):
        rendered_text = font.render(line, True, (255, 255, 255))
        screen.blit(rendered_text, (20, y_offset))
        y_offset += font.get_linesize()

    if "choices" in scenes[current_scene]:
        draw_choices(scenes[current_scene]["choices"], button_positions.get(current_scene, []))

    pygame.display.flip()

pygame.quit()
sys.exit()
