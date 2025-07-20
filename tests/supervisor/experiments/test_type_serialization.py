"""Test why type objects aren't serializable."""

import contextlib

import ormsgpack
from pydantic import BaseModel


class MyModel(BaseModel):
    name: str = "test"


def test_type_serialization():
    """Test serializing different representations of types."""
    test_cases = [
        ("int type", int),
        ("str type", str),
        ("list type", list),
        ("dict type", dict),
    ]

    for _name, obj in test_cases:
        with contextlib.suppress(Exception):
            ormsgpack.packb(obj)

    with contextlib.suppress(Exception):
        ormsgpack.packb(MyModel)

    instance = MyModel(name="test")
    with contextlib.suppress(Exception):
        ormsgpack.packb(instance)

    try:
        serialized = ormsgpack.packb(instance, option=ormsgpack.OPT_SERIALIZE_PYDANTIC)
        # Try to deserialize
        ormsgpack.unpackb(serialized)
    except Exception:
        pass

    # String representation
    with contextlib.suppress(Exception):
        ormsgpack.packb("MyModel")

    # Module + name
    try:
        class_ref = {"module": MyModel.__module__, "name": MyModel.__name__}
        ormsgpack.packb(class_ref)
    except Exception:
        pass

    # Schema representation
    try:
        schema = MyModel.model_json_schema()
        ormsgpack.packb(schema)
    except Exception:
        pass


if __name__ == "__main__":
    test_type_serialization()
