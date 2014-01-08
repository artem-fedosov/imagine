from PIL import Image
from primitives import ImagePrimitive, TextPrimitive
from errors import ImagineJsonParseError


class ImageCombine(object):
    PRIMITIVES_MAP = dict(
        text=TextPrimitive,
        image=ImagePrimitive
    )

    @classmethod
    def from_json(cls, json_dict):
        try:
            size = map(int, json_dict['size'])
            bg_color = json_dict['bg_color']
            primitives = []
            for primitive in json_dict['primitives']:
                Cls = cls.PRIMITIVES_MAP[primitive['type']]
                primitives.append(Cls.from_json(primitive))
        except (KeyError, ValueError), e:
            raise ImagineJsonParseError(e)

        return cls(primitives, size, bg_color)

    def __init__(self, primitives, size, bg_color="white"):
        self.size = size
        self.bg_color = bg_color
        self.primitives = list(sorted(primitives, key=lambda x: x.position.order))

    def save_to(self, filename):
        canvas = Image.new("RGB", self.size, self.bg_color)
        for primitive in self.primitives:
            primitive.add_to_canvas(canvas)
        canvas.save(filename)
