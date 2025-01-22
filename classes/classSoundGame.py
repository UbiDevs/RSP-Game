import pygame as pg

pg.init()

class SoundGame:
    """
    SoundGame is a class designed to handle background music and game sound effects in a game application.
    
    Core functionalities:
    - playBackgroundMusic: Loads and plays background music with a specified volume.
    - playGameSound: Plays game sound effects with a specified volume.
    
    Example usage:
    
    Parameters:
    - backMusic (str): The path to the background music file.
    - volume (float): The volume level for the background music (default is 0.2).
    - sound (str): The path to the game sound effect file.
    """
    
    def playBackgroundMusic(self, backMusic = None, volume = 0.2):
        # Check if backMusic is not None
        if backMusic:
            # Load the background music
            self.backMusic = pg.mixer.music.load(backMusic)
            # Set the volume of the background music
            pg.mixer.music.set_volume(volume)
            # Play the background music indefinitely
            pg.mixer.music.play(-1)
    
    def playGameSound(self, sound = None, volume = 0.4):
        # Check if a sound is provided
        if sound:
            # Set the sound to the provided sound
            self.sound = pg.mixer.Sound(sound)
            # Set the volume of the sound
            pg.mixer.Sound.set_volume(self.sound, volume)
            # Play the sound
            pg.mixer.Sound.play(self.sound)
