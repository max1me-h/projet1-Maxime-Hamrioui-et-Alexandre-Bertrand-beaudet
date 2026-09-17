# ======================== platforms.py ========================

import os
import random
import pygame
from config import ASSETS_DIR, PLATFORM_SIZE, MOVING_PLATFORM_SPEED

# Chargement des différentes images de plateformes
platform_green_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_green.png"))
platform_green_img = pygame.transform.scale(platform_green_img, PLATFORM_SIZE)

platform_blue_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_blue.png"))
platform_blue_img = pygame.transform.scale(platform_blue_img, PLATFORM_SIZE)

platform_brown_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_brown.png"))
platform_brown_img = pygame.transform.scale(platform_brown_img, PLATFORM_SIZE)

platform_spring_img = pygame.image.load(os.path.join(ASSETS_DIR, "platform_spring.png"))
platform_spring_img = pygame.transform.scale(platform_spring_img, (PLATFORM_SIZE[0], PLATFORM_SIZE[1] + 10))

# Dictionnaire d'accès aux images selon le type de plateforme
platform_images = {
    "green": platform_green_img,
    "blue": platform_blue_img,
    "brown": platform_brown_img,
    "spring": platform_spring_img
}


# ======================== PARTIE 2.1 ========================
def create_platform(x, y, platform_type="green"):
    """
    Crée et retourne un dictionnaire représentant une plateforme.

    Le dictionnaire ci-dessous représente pour l'instant correctement une
    plateforme verte. Votre travail consiste à le généraliser afin qu'il
    représente aussi correctement les plateformes bleues, marron et à ressort.
    """

    height = PLATFORM_SIZE[1] + 10 if platform_type == "spring" else PLATFORM_SIZE[1]
    vx = MOVING_PLATFORM_SPEED if platform_type == "blue" else 0.0

    platform = {
        "x": float(x),
        "y": float(y),
        "type": platform_type,
        "image": platform_images[platform_type],
        "vx": vx,
        "active": True,
        "width": PLATFORM_SIZE[0],
        "height": height
    }

    return platform

# ===========================================================


# ======================== PARTIE 2.2 ========================
def choose_platform_type(green_probability, blue_probability, spring_probability):
    """
    Choisit aléatoirement un type de plateforme.

    Les trois paramètres donnent les probabilités respectives des plateformes
    verte, bleue et à ressort. La probabilité restante correspond à une
    plateforme marron.
    """

    roll = random.random()

    green_threshold = green_probability
    blue_threshold = green_threshold + blue_probability
    spring_threshold = blue_threshold + spring_probability

    if roll < green_threshold:
        return "green"
    elif roll < blue_threshold:
        return "blue"
    elif roll < spring_threshold:
        return "spring"
    else:
        return "brown"

# ===========================================================

