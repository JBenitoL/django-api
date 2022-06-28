class NewEnum:
    @classmethod
    def get_names(cls):
        return [key for key in cls.__dict__.keys() if "__" not in key and not callable(getattr(cls, key))]

    @classmethod
    def get_values(cls):
        return [getattr(cls, key) for key in cls.__dict__.keys() if "__" not in key and not callable(getattr(cls, key))]

    @classmethod
    def get_functions(cls):
        return [getattr(cls, key) for key in cls.__dict__.keys() if "__" not in key and  callable(getattr(cls, key))]