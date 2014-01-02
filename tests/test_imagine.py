# -*- coding: utf-8 -*-

import unittest
from PIL import Image, ImageDraw
from imagine.primitives import Position, TextPrimitive, ImagePrimitive, ImageCombine
from card1 import Card1


TEST_DATA = dict(
    font_path_bold='./font/Exo2-Bold.ttf',
    font_path_light='./font/Exo2-Light.ttf',
    image_path='./images/my-face.jpg',
)


class TestPrimitives(unittest.TestCase):
    def setUp(self):
        self.canvas = Image.new("RGB", [200, 100], color='white')

    def tearDown(self):
        del self.canvas

    def test_text_primitive(self):
        text_primitive = TextPrimitive(
            text=u'Привет медвед!',
            position=Position(10, 10),
            font_path=TEST_DATA['font_path_bold'],
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


class TestCombine(unittest.TestCase):
    def test_combine(self):
        card = Card1(
            text_bold1=u'Федосов Артем',
            text_bold2=u'Борисович',
            text_light_grey1=u'Босс мафии',
            text_small_grey1=u'тел: +7 985 123 4567',
            text_small_grey2=u'email: boss.mafii@owndomain.ru',
            text_small_grey3=u'Рязань, ул. Пушкина 29/1',
            font_path1=TEST_DATA['font_path_bold'],
            font_path2=TEST_DATA['font_path_light'],
            image_path=TEST_DATA['image_path'],
            image_re_size=(400, 400),
            image_crop_coords=(50, 0, 350, 400)
        )

        card.save_to('test_image.png')