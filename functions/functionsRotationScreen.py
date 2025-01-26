from config.createObjects import player, computer

def rotationScreen():
    """
    Rotates the screen for the player and computer, and blits the 'start' sign for both.
    
    This function rotates the player's and computer's images by specified angles and then
    blits the 'start' sign onto their respective images.
    
    The player's image is rotated by -45 degrees, and the computer's image is rotated by 45 degrees.
    After rotation, the 'start' sign is blitted onto both images.
    """
    # Rotate the player's image by -45 degrees
    player.rotation(angle = -45)
    # Rotate the computer's image by 45 degrees
    computer.rotation(angle = 45)
    # Blit the 'start' sign onto the player's image
    player.update(sign = 'start')
    # Blit the 'start' sign onto the computer's image
    computer.update(sign = 'start')

