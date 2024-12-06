import pygame
import sys

class PreloadAnimation:
    def __init__(self, width, height, callback):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Loading Animation")
        self.clock = pygame.time.Clock()
        self.alpha = 255  # Start with full black
        self.running = True
        self.callback = callback  # Store the callback function

    def preload(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fade-out logic
            self.alpha -= 5  # Adjust speed
            if self.alpha <= 0:
                self.running = False  # End the fade-out

            # Update background color
            fade_color = (255 - self.alpha, 255 - self.alpha, 255 - self.alpha)
            self.screen.fill(fade_color)

            # Show text
            font = pygame.font.Font(None, 74)
            text = font.render("Loading, please wait...", True, (self.alpha, self.alpha, self.alpha))
            text_rect = text.get_rect(center=(400, 300))
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(60)  # Cap at 60 FPS

        # Call the callback method (home method of GUI)
        self.callback()  # This will call the home method after the preload animation
