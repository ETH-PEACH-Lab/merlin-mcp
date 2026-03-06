from numbers import Number
from pydantic import BaseModel, model_validator
from typing import Union

ValueType = Union[int | float | str | None]
ColorType = Union[str | None]

class ID(BaseModel):
    value: str
    @model_validator(mode='before')
    @classmethod
    def from_str(cls, data):
        # This allows the LLM/Inspector to pass a plain string
        if isinstance(data, str):
            return {"value": data}
        return data
    def __str__(self):
        return self.value

class Edge(BaseModel):
    source: ID
    target: ID
    def __str__(self):
        return str(self.source) + "-" + str(self.target)

# Converts the input from a python value to emmited Merlin code
def to_merlin(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return str(value)
    if isinstance(value, ID):
        return str(value)
    if isinstance(value, str):
        return '"' + value + '"'
    if isinstance(value, Edge):
        return str(value)
    if isinstance(value, list):
        converted_items = map(to_merlin, value)
        return '[' + ", ".join(converted_items) + ']'
    raise Exception(f"Unknown type: {type(value)}")

if __name__ == "__main__":
    print(to_merlin(None))
    print(to_merlin(True))
    print(to_merlin(42))
    print(to_merlin(3.14))
    print(to_merlin(ID(value = "A")))
    edge = Edge(source = ID(value = "B"), target = ID(value = "C"))
    print(to_merlin(edge))
    print(to_merlin("Merlin"))
    print(to_merlin([1, None, "_", "Merlin"]))
    print(to_merlin([[1, 2, 3], [1, None, 3], [1, "Fish", 3]]))