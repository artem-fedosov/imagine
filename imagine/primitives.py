# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw


class Position(object):
    def __init__(self, x, y, order=0):
        self.x = x
        self.y = y
        self.order = order

    def top_left(self):
        """ Coordinates of top left corner"""
        return self.x, self.y

    def right_bottom(self, size):
        """ Coordinates of top right"""
        x, y = size
        return self.x + x, self.y + y


class ImagePrimitive(object):
    def __init__(self, position, filename, crop_coords=None, re_size=None):
        self.position = position
        self.crop_coords = crop_coords
        self.re_size = re_size
        self._filename = filename
        self._image = None

    @property
    def image(self):
        if self._image is None:
            self._image = Image.open(self._filename)
        return self._image

    def resize(self, size):
        if size is not None and size != self.image.size:
            self._image = self.image.resize(size, Image.ANTIALIAS)

    def crop(self, crop_coords):
        if crop_coords:
            self._image = self.image.crop(crop_coords)

    def add_to_canvas(self, canvas):
        self.resize(self.re_size)
        self.crop(self.crop_coords)
        canvas.paste(self.image, self.position.top_left() + self.position.right_bottom(size=self.image.size))


class TextPrimitive(object):
    def __init__(self, text, position, font_path, font_size, color):
        self.text = text
        self.position = position
        self.color = color  # RGB tuple  ex. (255, 255, 255)
        self._fontpath = font_path
        self._fontsize = font_size
        self._font = None

    @property
    def font(self):
        if self._font is None:
            self._font = ImageFont.truetype(filename=self._fontpath, size=self._fontsize, encoding='unic')
        return self._font

    def add_to_canvas(self, canvas):
        draw = ImageDraw.Draw(canvas)
        draw.text(self.position.top_left(), self.text, self.color, font=self.font)
        del draw


class ImageCombine(object):
    def __init__(self, primitives, size, bg_color="white"):
        self.size = size
        self.bg_color = bg_color
        self.primitives = list(sorted(primitives, key=lambda x: x.position.order))

    def save_to(self, filename):
        canvas = Image.new("RGB", self.size, self.bg_color)
        for primitive in self.primitives:
            primitive.add_to_canvas(canvas)
        canvas.save(filename)
