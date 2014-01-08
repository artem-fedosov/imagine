# -*- coding: utf-8 -*-

import unittest
from PIL import Image
from imagine.primitives import Position, TextPrimitive, ImagePrimitive
from imagine.combine import ImageCombine
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

    def test_create_text_primitive(self):
        text_primitive = TextPrimitive(
            text=u'Привет медвед!',
            position=Position(10, 10),
            font_path=TEST_DATA['font_path_bold'],
            font_size=14,
            color='black'
        )

        text_primitive.add_to_canvas(self.canvas)

    def test_text_primitive_from_json(self):
        position_dict = dict(x=10, y=10, order=10)
        json_dict = dict(
            type='text',
            text=u'Привет медвед!',
            position=position_dict,
            font_path=TEST_DATA['font_path_bold'],
            font_size=14,
            color='black'
        )
        text_primitive = TextPrimitive.from_json(json_dict)
        text_primitive.add_to_canvas(self.canvas)

    def test_create_image_primitive(self):
        image_primitive = ImagePrimitive(
            position=Position(10, 10),
            filename=TEST_DATA['image_path'],
            re_size=(120, 120),
            crop_box=(20, 20, 100, 100)
        )

        image_primitive.add_to_canvas(self.canvas)

    def test_image_primitive_from_json(self):
        position_dict = dict(x=10, y=10, order=10)
        json_dict = dict(
            type='image',
            position=position_dict,
            filename=TEST_DATA['image_path'],
            re_size=(120, 120),
            crop_box=(20, 20, 100, 100)
        )

        image_primitive = ImagePrimitive.from_json(json_dict)
        image_primitive.add_to_canvas(self.canvas)


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
            image_crop_box=(50, 0, 350, 400)
        )

        card.save_to('test_image.png')

    def test_combine_from_json(self):
        position_dict = dict(x=10, y=10, order=10)

        image_json_dict = dict(
            type='image',
            position=position_dict,
            filename=TEST_DATA['image_path'],
            re_size=(120, 120),
            crop_box=(20, 20, 100, 100)
        )

        text_json_dict = dict(
            type='text',
            text=u'Привет медвед!',
            position=position_dict,
            font_path=TEST_DATA['font_path_bold'],
            font_size=14,
            color='black'
        )

        json_dict = dict(
            size=[400, 400],
            bg_color='white',
            primitives=[image_json_dict, text_json_dict]
        )

        combine = ImageCombine.from_json(json_dict)

        combine.save_to('another_test_image.png')
