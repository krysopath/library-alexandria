class Skeleton:
    export = []

    def __repr__(self):
        return str(self.__class__)

    def __iter__(self):
        for p in self.export:
            yield p, getattr(self, p)

    def __todict__(self):
        d = {}
        for p, v in self:
            d[p] = v
        return d

    def __hash__(self):
        return hash(
            self.__repr__()
        )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return self.__repr__()



