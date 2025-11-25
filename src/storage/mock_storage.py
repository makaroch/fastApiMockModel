from uuid import uuid4


class MockStorage:
    def __init__(self):
        self.data: dict[uuid4, list[str]] = {}

    def get(self, key: uuid4):
        return self.data.get(key, None)

    def set(self, key: uuid4, value: list[str]):
        self.data[key] = value


