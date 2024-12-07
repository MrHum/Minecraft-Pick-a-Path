import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame

pygame.mixer.init()

base_path = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(base_path, "images")
audio_path = os.path.join(base_path, "audio")

background_music = os.path.join(audio_path, "background_music.wav")
win_music = os.path.join(audio_path, "win_music.ogg") 
game_over_sounds = {
    "game_over1": os.path.join(audio_path, "game_over1.ogg"),
    "game_over2": os.path.join(audio_path, "game_over2.ogg"),
    "game_over3": os.path.join(audio_path, "game_over3.ogg"),
    "game_over4": os.path.join(audio_path, "game_over4.ogg"),
}

scenes = {
    "instructions": {
        "description": "Welcome to Minecraft Pick-A-Path! Choose your path wisely. Each choice leads to a unique outcome. Survive and find the diamonds! Click 'Start Game' to begin.",
        "image": "Introduction.png",
        "choices": {"Start Game": "start"}
    },
    "start": {
        "description": "You see a lit-up cave and a pitch-black cave. Where do you go?",
        "image": "choice1.png",
        "choices": {
            "Go to the lit-up cave": "game_over1",
            "Go into the dark cave": "Dark_Cave2"
        }
    },
    "Dark_Cave2": {
        "description": "You bravely go through the dark cave and find a light source. Now you find another dark cave above.",
        "image": "choice2.png",
        "choices": {
            "Go up into another dark cave": "game_over2",
            "Continue regular path": "Diamonds"
        }
    },
    "Diamonds": {
        "description": "You continued your path and found diamonds, but they are guarded by two skeletons and zombies. What will you do?",
        "image": "choice3.png",
        "choices": {
            "Fight the mobs with a damaged sword": "game_over3",
            "Fight the mobs with an axe on the floor": "win2",
            "Wait for the mobs to disappear": "game_over4"
        }
    },
    "game_over1": {"description": "Game Over! The light came from lava and you fell before you realized.", "image": "gameover1.png"},
    "game_over2": {"description": "Game Over! You were ambushed by mobs. Be more careful next time.", "image": "gameover2.png"},
    "game_over3": {"description": "Game Over! Your sword broke mid-fight. The mobs counter-attacked.", "image": "gameover3.png"},
    "game_over4": {"description": "Game Over! A creeper snuck up on you. Boom!", "image": "gameover4.png"},
    "win2": {"description": "Congratulations! You defeated the mobs and mined the diamonds. You won!", "image": "win1.png"}
}

def play_music(file_path, loop=-1):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loop)

def stop_music():
    pygame.mixer.music.stop()

def play_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    sound.play()

def handle_scene_change(scene):
    """Manage audio transitions based on scene."""
    if scene == "instructions":
        play_music(background_music)
    elif scene in game_over_sounds:
        stop_music()
        play_sound(game_over_sounds[scene])
    elif scene == "win2":
        stop_music()
        play_music(win_music)
    elif scene == "instructions":
        stop_music()
        play_music(background_music)

class PickAPathGame:
    def __init__(self, briar):
        self.briar = briar
        self.briar.title("Minecraft Pick-A-Path")
        self.briar.geometry("1080x720")
        self.current_scene = "instructions"
        
        self.image_label = tk.Label(self.briar)
        self.image_label.pack()
        self.description_label = tk.Label(self.briar, wraplength=1000, font=("Helvetica", 16))
        self.description_label.pack(pady=10)
        self.button_frame = tk.Frame(self.briar)
        self.button_frame.pack()

        self.load_scene()

    def load_scene(self):
        scene = scenes[self.current_scene]

        handle_scene_change(self.current_scene)

        if "image" in scene:
            image_path = os.path.join(images_path, scene["image"])
            image = Image.open(image_path).resize((1080, 500), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

        self.description_label.config(text=scene["description"])

        for widget in self.button_frame.winfo_children():
            widget.destroy()

        if "choices" in scene:
            for choice_text, next_scene in scene["choices"].items():
                button = tk.Button(self.button_frame, text=choice_text, command=lambda n=next_scene: self.change_scene(n), font=("Helvetica", 14))
                button.pack(pady=5)
        else:
            restart_button = tk.Button(self.button_frame, text="Try Again", command=self.reset_game, font=("Helvetica", 14))
            restart_button.pack(pady=20)

    def change_scene(self, next_scene):
        self.current_scene = next_scene
        self.load_scene()

    def reset_game(self):
        self.current_scene = "instructions"
        self.load_scene()

if __name__ == "__main__":
    briar = tk.Tk()
    app = PickAPathGame(briar)
    briar.mainloop()
