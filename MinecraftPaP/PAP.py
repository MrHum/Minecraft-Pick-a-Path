import pygame
import sys

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
            "Go into the dark cave": "Dark_Cave"
        },
        "image": None
    },
    "Dark_Cave": {
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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)

def draw_text_wrapped(text, x, y, width, font, color):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] > width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line

    lines.append(current_line)

    for line in lines:
        rendered_text = font.render(line, True, color)
        screen.blit(rendered_text, (x, y))
        y += font.get_linesize()

def draw_choices(choices):
    global selected_choice
    y_offset = 300 
    for i, (choice_text, next_scene) in enumerate(choices.items()):
        radio_x, radio_y = 50, y_offset
        pygame.draw.circle(screen, BLUE, (radio_x, radio_y), 15, 2)
        if selected_choice == next_scene:
            pygame.draw.circle(screen, BLUE, (radio_x, radio_y), 10)

        choice_surface = font.render(choice_text, True, WHITE)
        screen.blit(choice_surface, (radio_x + 30, y_offset - 10))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if (mouse_x - radio_x) ** 2 + (mouse_y - radio_y) ** 2 < 15 ** 2:
                selected_choice = next_scene

        y_offset += 50

def go_to_next_scene():
    global current_scene, selected_choice, show_play_again_button, end_scene_start_time
    if selected_choice:
        current_scene = selected_choice
        selected_choice = None
        show_play_again_button = False
        if current_scene in ["win", "game_over1", "game_over2", "game_over4"]:
            end_scene_start_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_text_wrapped(scenes[current_scene]["description"], 20, 50, 1040, font, WHITE)

    if current_scene not in ["game_over1", "game_over2", "game_over4", "win"]:
        draw_choices(scenes[current_scene]["choices"])

        continue_rect = pygame.Rect(450, 650, 200, 50)
        pygame.draw.rect(screen, GREEN, continue_rect)
        continue_text = font.render("Continue", True, BLACK)
        screen.blit(continue_text, (475, 660))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if continue_rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                go_to_next_scene()
    else:
        if pygame.time.get_ticks() - end_scene_start_time > 3000:
            show_play_again_button = True

        if show_play_again_button:
            play_again_rect = pygame.Rect(450, 650, 200, 50)
            pygame.draw.rect(screen, GREEN, play_again_rect)
            play_again_text = font.render("Play Again?", True, BLACK)
            screen.blit(play_again_text, (465, 660))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_again_rect.collidepoint(mouse_x, mouse_y):
                if pygame.mouse.get_pressed()[0]:
                    current_scene = "instructions"
                    show_play_again_button = False

    pygame.display.flip()

pygame.quit()
sys.exit()
