import pygame
import sys
import tkinter as tk

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Minecraft Pick-A-Path")

font = pygame.font.Font(None, 36)

scenes = {
    "instructions": {
        "description": "Welcome to Minecraft Pick-A-Path! Choose your path wisely. Each choice leads to a unique outcome. Survive and find the diamonds! Click 'Start Game' to begin.",
        "choices": {"Start Game": "start"},
        "image": None
    },
    "start": {
        "description": "You see a lit-up cave and a pitch-black cave. Where do you go?",
        "choices": {
            "Go to the lit-up cave": "game_over1",
            "Go into the dark cave": "Dark_Cave2"
        },
        "image": None
    },
    "Dark_Cave2": {
        "description": "You bravely go through the dark cave and find a light source. Now you find another dark cave above.",
        "choices": {
            "Go up into another dark cave": "game_over2",
            "Continue regular path": "Diamonds"
        },
        "image": None
    },
    "Diamonds": {
        "description": "You continued your path and found diamonds, but they are guarded by two skeletons and zombies. What will you do?",
        "choices": {
            "Fight the mobs with a damaged sword": "game_over3",
            "Fight the mobs with an axe you remembered": "win",
            "Wait out the mobs": "game_over4"
        },
        "image": None
    },
    "game_over1": {
        "description": "Game Over! The light came from lava and you fell before you realized. Great environmental awareness.",
        "choices": {},
        "image": None
    },
    "game_over2": {
        "description": "Game Over! You were ambushed by mobs. Take a torch next time.",
        "choices": {},
        "image": None
    },
    "game_over3": {
        "description": "Game Over! You forgot that the sword was badly damaged, it broke, and now the mobs counter-attack. Great job.",
        "choices": {},
        "image": None
    },
    "game_over4": {
        "description": "Game Over! You waited too long, and a creeper snuck up on you. Boom!",
        "choices": {},
        "image": None
    },
    "win": {
        "description": "Congratulations! You pulled out your axe, defeated the mobs, and mined the diamonds. You won!",
        "choices": {},
        "image": None
    }
}

current_scene = "instructions"
selected_choice = None
show_play_again_button = False
end_scene_start_time = 0

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

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    description_text = scenes[current_scene]["description"]
    y_offset = 50
    for line in description_text.split('\n'):
        rendered_text = font.render(line, True, (255, 255, 255))
        screen.blit(rendered_text, (20, y_offset))
        y_offset += font.get_linesize()

    if current_scene not in ["game_over1", "game_over2", "game_over4", "win"]:
        y_offset = 300
        for choice_text, next_scene in scenes[current_scene]["choices"].items():
            pygame.draw.circle(screen, (100, 100, 255), (50, y_offset), 15, 2)
            choice_surface = font.render(choice_text, True, (255, 255, 255))
            screen.blit(choice_surface, (80, y_offset - 10))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if (mouse_x - 50) ** 2 + (mouse_y - y_offset) ** 2 < 15 ** 2:
                    current_scene = next_scene

            y_offset += 50
    
    if current_scene in ["game_over1", "game_over2", "game_over3", "game_over4", "win"]:
        play_again_rect = pygame.Rect(450, 650, 200, 50)
        pygame.draw.rect(screen, (100, 255, 100), play_again_rect)
        play_again_text = font.render("Play Again?", True, (0, 0, 0))
        screen.blit(play_again_text, (465, 660))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if play_again_rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                current_scene = "start"

    pygame.display.flip()

pygame.quit()
sys.exit()
