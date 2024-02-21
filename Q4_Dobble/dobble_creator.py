# Cassandre Hamel, 20210863
# Viviane Binet, 20244728

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image, ImageOps
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        # TODO
        if not os.path.exists('results'):
            os.makedirs('results')
        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        with open(cards_file, 'r') as file:
            
            for line_number, line in enumerate(file, 1):
                # split numbers by space per line
                card_images = line.strip().split(' ')
                # fix width by the length of the images in the line
                card_width = self.pic_size * len(card_images) 
                # make a square card
                card = Image.new('RGB', (card_width, card_width), 'white')
                # add border
                card = ImageOps.expand(card, border=self.border_size + 2, fill='black')
                # get radius (D/2) but 3 because otherwise the images are too far apart
                radius = float((self.pic_size)*len(card_images) // 3 )
                
                # center of image / circle
                center_x, center_y = (self.pic_size)*len(card_images) // 2, (self.pic_size)*len(card_images) // 2  
                
                for index, number in enumerate(card_images):
                    # get name '_.png'
                    image_filename = f"{number}.png"
                    
                    try:
                        image_path = os.path.join('images/', image_filename)
                        with Image.open(image_path) as img:
                            # Rotate the image randomly: Image.rotate(angle, resample=Resampling.NEAREST, expand=0, center=None, translate=None, fillcolor=None)
                            img = img.rotate(random.randint(0, 360), expand=True)
                            # circuit = 2 * PI * R : https://stackoverflow.com/questions/67484376/how-to-paste-images-along-a-circular-path-in-python
                            # and https://stackoverflow.com/questions/13383112/python-arrange-images-on-canvas-in-a-circle
                            angle = 2 * math.pi / len(card_images) * index
                            # https://stackoverflow.com/questions/67484376/how-to-paste-images-along-a-circular-path-in-python
                            x = int(center_x + radius * math.cos(angle) - self.pic_size / 2)
                            y = int(center_y + radius * math.sin(angle) - self.pic_size / 2)
                            # Image.paste(im, box=None, mask=None) → None[source] : Pastes another image into this image. 
                            card.paste(img, (x, y), img)
                    except FileNotFoundError:
                        if verbose:
                            print(f"Image {image_filename} not found in 'images' folder.")

                #Image.save(fp, format=None, **params) → None[source] : Saves this image under the given filename
                card.save(os.path.join('results', f'card{line_number}.jpg'))


