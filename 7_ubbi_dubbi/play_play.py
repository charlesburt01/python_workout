class Human:
    species = "bromo-sapien"
    words = "bleh"
    def __init__(self, name, song):
        self.name = name
        self._age = 0
        self.song = song

    @property
    def age(self):
        return self._age

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def get_song(self):
        return self.song

    def sing(self):
        return self.words


class FastWalker(Human):
    def __init__(self, name, song):
        super().__init__(name, song)
        self.fictional = True
        self.words = "yap"
    def sing(self):
        print(super().sing())
        return 'overridden fool'



new = FastWalker("this dude", "my song")
print(new.sing())
