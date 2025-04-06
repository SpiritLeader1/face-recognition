# Import necessary modules
import pygame
import random
import time
import csv2

# Experiment setup
num_trials = 10
stimuli = ['circle', 'square', 'triangle'] * (num_trials // 3)
random.shuffle(stimuli)

# Initialize pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Experiment")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Set up clock for frame rate control
clock = pygame.time.Clock()

# Data storage
data = []

# Instructions
print("Experiment Instructions:")
print("Respond to each shape as quickly as possible.")
print("Press any key to respond, or press ESC to exit.")

# Experiment loop
for trial, stimulus in enumerate(stimuli):
    # Clear screen
    screen.fill(white)
    
    # Draw stimulus
    if stimulus == 'circle':
        pygame.draw.circle(screen, red, (screen_width // 2, screen_height // 2), 50)
    elif stimulus == 'square':
        pygame.draw.rect(screen, blue, (screen_width // 2 - 50, screen_height // 2 - 50, 100, 100))
    elif stimulus == 'triangle':
        pygame.draw.polygon(screen, green, [
            (screen_width // 2, screen_height // 2 - 50), 
            (screen_width // 2 - 50, screen_height // 2 + 50), 
            (screen_width // 2 + 50, screen_height // 2 + 50)
        ])
    
    # Update the display to show the stimulus
    pygame.display.flip()
    
    # Start timing for reaction time
    start_time = time.time()
    
    # Wait for response
    response = None
    reaction_time = None
    
    # Collect response or exit if ESC is pressed
    collecting_response = True
    while collecting_response:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Experiment aborted by user.")
                    collecting_response = False
                    pygame.quit()
                    exit()
                else:
                    reaction_time = time.time() - start_time
                    response = pygame.key.name(event.key)
                    collecting_response = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # Control frame rate
        clock.tick(60)
    
    # Log data for this trial
    data.append({
        'trial': trial + 1,
        'stimulus': stimulus,
        'reaction_time': reaction_time,
        'response': response
    })

# End of experiment
print("Experiment complete. Saving data...")

# Save data to CSV
with open("experiment_data.csv", "w", newline='') as csvfile:
    fieldnames = ['trial', 'stimulus', 'reaction_time', 'response']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Cleanup
pygame.quit()
print("Data saved to experiment_data.csv")
