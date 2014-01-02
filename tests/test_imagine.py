# -*- coding: utf-8 -*-

import unittest
from PIL import Image, ImageDraw
from imagine.primitives import Position, TextPrimitive, ImagePrimitive

TEST_DATA = dict(
    font_path='./font/Exo2-BoldItalic.ttf',
    image_path='./images/my-face.jpg',
)


class TestPrimitives(unittest.TestCase):
    def setUp(self):
        self.canvas = Image.new("RGB", [2000, 1000], color='white')

    def tearDown(self):
        del self.canvas

    def test_text_primitive(self):
        text_primitive = TextPrimitive(
            text=u'Привет медвед!',
            position=Position(10, 10),
            font_path=TEST_DATA['font_path'],
            font_size=14,
            color='black'
        )

        text_primitive.add_to_canvas(self.canvas)

    def test_image_primitive(self):
        image_primitive = ImagePrimitive(
            position=Position(10, 10),
            filename=TEST_DATA['image_path'],
            re_size=(120, 120),
            crop_coords=(20, 20, 100, 100)
        )

        image_primitive.add_to_canvas(self.canvas)
        # self.canvas.show()

