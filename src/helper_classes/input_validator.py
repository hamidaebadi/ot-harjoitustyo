class InputValidator:
    """class InputValidor is a helper class for forms's inputs validations
    """

    @classmethod
    def is_entry_empty(cls, entry):
        """class method ensuring that provided input is not empty

        Args:
            entry : form's input

        Returns :Returns True if input is empty, otherwise False
        """
        if len(entry.get()) == 0:
            return True
        return False
