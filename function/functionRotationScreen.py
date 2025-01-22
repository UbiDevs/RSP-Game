from config.createObjects import player, computer

def rotationScreen():
    """
    Rotates the screen for the player and computer, and blits the 'start' sign for both.
    
    This function rotates the player's and computer's images by specified angles and then
    blits the 'start' sign onto their respective images.
    """
    player.rotation(angle = -45)
    computer.rotation(angle = 45)
    
    player.blitSign(sign = 'start')
    computer.blitSign(sign = 'start')
