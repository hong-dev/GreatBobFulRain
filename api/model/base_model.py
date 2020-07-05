class BaseModel:
    def __str__(self):
        return str(self.__dict__)

    def __eq__(self):
        return isinstance(other, self.__class___) and self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(frozenset(self.__dict__.items()))

    @classmethod
    def from_row(cls, row):
        params = { }
        for key in row.keys():
            params[key] = row[key]

        return cls(**params)
