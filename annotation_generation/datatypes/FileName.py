from __future__ import annotations

class FileName:

    def __init__(self, name: str) -> None:
        # name should be a string
        self.name = name

    def __repr__(self):
        return str(self.name)

    def __eq__(self, other: FileName) -> bool:
        return self.name == other.name
