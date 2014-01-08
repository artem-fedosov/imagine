# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
from errors import ImagineJsonParseError


class Position(object):
    def __init__(self, x, y, order=0):
        self.x = x
        self.y = y
        self.order = order

    @classmethod
    def from_json(cls, json_dict):
        try:
            x = int(json_dict['x'])
            y = int(json_dict['y'])
        except (KeyError, ValueError), e:
            raise ImagineJsonParseError(e)
        order = json_dict.get('order')
        return cls(x, y, order)

    def top_left(self):
        """ Coordinates of top left corner"""
        return self.x, self.y

    def right_bottom(self, size):
        """ Coordinates of top right"""
        x, y = size
        return self.x + x, self.y + y


class ImagePrimitive(object):
    def __init__(self, position, filename, crop_box=None, re_size=None):
        self.position = position
        self.crop_box = crop_box
        self.re_size = re_size
        self._filename = filename
        self._image = None

    @property
    def image(self):
        if self._image is None:
            self._image = Image.open(self._filename)
        return self._image

    @classmethod
    def from_json(cls, json_dict):
        try:
            position = Position.from_json(json_dict['position'])
            filename = json_dict['filename']
        except KeyError, e:
            raise ImagineJsonParseError(e)

        try:
            crop_box = json_dict.get('crop_box')
            re_size = json_dict.get('re_size')
            if crop_box is not None:
                crop_box = map(int, crop_box)
            if re_size is not None:
                re_size = map(int, re_size)
        except ValueError, e:
            raise ImagineJsonParseError(e)
        
        return ImagePrimitive(position, filename, crop_box, re_size)

    def resize(self, size):
        if size is not None and size != self.image.size:
            self._image = self.image.resize(size, Image.ANTIALIAS)

    def crop(self, crop_box):
        if crop_box:
            self._image = self.image.crop(crop_box)

    def add_to_canvas(self, canvas):
        self.resize(self.re_size)
        self.crop(self.crop_box)
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

    @classmethod
    def from_json(cls, json_dict):
        try:
            text = json_dict['text']
            position = Position.from_json(json_dict['position'])
            font_path = json_dict['font_path']
            font_size = json_dict['font_size']
            color = json_dict['color']
        except KeyError, e:
            raise ImagineJsonParseError(e)
        return TextPrimitive(text, position, font_path, font_size, color)

    def add_to_canvas(self, canvas):
        draw = ImageDraw.Draw(canvas)
        draw.text(self.position.top_left(), self.text, self.color, font=self.font)
        del draw
