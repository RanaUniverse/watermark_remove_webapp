"""
Thi sis utils/image_generation.py file
"""

import random


from PIL import Image


def generate_color_image(
    size: tuple[int, int] = (1000, 1000),
    color: tuple[int, int, int] | None = None,
) -> Image.Image:
    """
    It will make a colorful square image and return the image obj
    """

    if not color:
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
    img_obj = Image.new(
        mode="RGB",
        size=size,
        color=color,
    )
    return img_obj
