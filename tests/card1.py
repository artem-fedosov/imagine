from imagine.primitives import ImagePrimitive, TextPrimitive, Position
from imagine.combine import ImageCombine


class Card1(object):
    def __init__(
            self,
            text_bold1,
            text_bold2,
            text_light_grey1,
            text_small_grey1,
            text_small_grey2,
            text_small_grey3,
            font_path1,
            font_path2,
            image_path,
            image_re_size=None,
            image_crop_box=None,
    ):

        image_primitive = ImagePrimitive(
            position=Position(50, 50),
            filename=image_path,
            re_size=image_re_size,
            crop_box=image_crop_box
        )

        name1 = TextPrimitive(
            text=text_bold1,
            position=Position(450, 50),
            font_path=font_path1,
            font_size=50,
            color='black'
        )

        name2 = TextPrimitive(
            text=text_bold2,
            position=Position(450, 110),
            font_path=font_path1,
            font_size=50,
            color='black'
        )

        position = TextPrimitive(
            text=text_light_grey1,
            position=Position(450, 170),
            font_path=font_path2,
            font_size=30,
            color='grey'
        )

        contacts1 = TextPrimitive(
            text=text_small_grey1,
            position=Position(550, 385),
            font_path=font_path2,
            font_size=20,
            color='grey'
        )

        contacts2 = TextPrimitive(
            text=text_small_grey2,
            position=Position(550, 405),
            font_path=font_path2,
            font_size=20,
            color='grey'
        )

        contacts3 = TextPrimitive(
            text=text_small_grey3,
            position=Position(550, 425),
            font_path=font_path2,
            font_size=20,
            color='grey'
        )

        primitives = [image_primitive, name1, name2, position, contacts1, contacts2, contacts3]
        self.combine = ImageCombine(primitives, (900, 500), bg_color='white')

    def save_to(self, filename):
        self.combine.save_to(filename)