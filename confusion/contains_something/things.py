class Something:
    def __init__(self, value: str):
        self.value = value

def convert(value: str) -> Something:
    return Something(value)

reveal_type(convert)
