from pydantic import BaseModel, validator


class Point(BaseModel):
    x: int
    y: int


class Polygon(BaseModel):
    points: list[Point]

    @validator("points", pre=True, each_item=True)
    def each_element_should_be_a_point(cls, v):
        coords = v.split("|")
        point = Point(x=coords[0], y=coords[1])
        return point


poly = Polygon.parse_obj({"points": ["0|0", "1|0", "1|1"]})