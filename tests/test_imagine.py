# -*- coding: utf-8 -*-

import unittest
from PIL import Image, ImageDraw
from imagine.primitives import Position, TextPrimitive, ImagePrimitive, ImageCombine

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
        image_primitive = ImagePrimitive(
            position=Position(50, 50),
            filename=TEST_DATA['image_path'],
            re_size=(400, 400),
            crop_coords=(50, 0, 350, 400)
        )

        name1 = TextPrimitive(
            text=u'Федосов Артем',
            position=Position(450, 50),
            font_path=TEST_DATA['font_path_bold'],
            font_size=50,
            color='black'
        )

        name2 = TextPrimitive(
            text=u'Борисович',
            position=Position(450, 110),
            font_path=TEST_DATA['font_path_bold'],
            font_size=50,
            color='black'
        )

        position = TextPrimitive(
            text=u'Босс мафии',
            position=Position(450, 170),
            font_path=TEST_DATA['font_path_light'],
            font_size=30,
            color='grey'
        )

        contacts1 = TextPrimitive(
            text=u'тел: +7 985 123 4567',
            position=Position(550, 350),
            font_path=TEST_DATA['font_path_light'],
            font_size=20,
            color='grey'
        )

        contacts2 = TextPrimitive(
            text=u'email: boss.mafii@owndomain.ru',
            position=Position(550, 370),
            font_path=TEST_DATA['font_path_light'],
            font_size=20,
            color='grey'
        )

        contacts3 = TextPrimitive(
            text=u'Рязань, ул. Пушкина 29/1',
            position=Position(550, 390),
            font_path=TEST_DATA['font_path_light'],
            font_size=20,
            color='grey'
        )

        primitives = [image_primitive, name1, name2, position, contacts1, contacts2, contacts3]

        combine = ImageCombine(primitives, (900, 500), bg_color='white')  # Размер визитки - 90 х 50 мм
        combine.save_to('test_image.png')