class InputValidator:
    def __init__(self):
        pass

    @classmethod
    def is_entry_empty(cls, entry):
        if len(entry.get()) == 0:
            return True
        return False
