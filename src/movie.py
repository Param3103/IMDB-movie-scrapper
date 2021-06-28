class Movie:
    def __init__(self, released_year, name, rating):
        self.released_year = released_year.replace("\n", "")
        self.name = name.replace("\n", "")[13:-1].strip()
        self.rating = rating.replace("\n", "")

    def __str__(self):
        return ",".join([self.released_year, self.name, self.rating])

    @classmethod
    def fromSoup(cls, container, rating):
        return cls(container.text[-6: -2], container.text[2: -6], rating.text)
