from .serial import (
    SerializationFormat,
)

for name in ['serial', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
