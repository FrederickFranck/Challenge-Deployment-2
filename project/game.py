from typing import Tuple


class Game:
    def __init__(self) -> None:
        self.id = 0
        self.name = ""
        self.developer = ""
        self.price = 0.0
        self.description = ""
        self.win_support = False
        self.mac_support = False
        self.linux_Sup = False
        self.positive_reviews = 0
        self.negative_reviews = 0

        self.genres = []
        self.categories = []
        self.languages = []

    def __init__(
        self,
        _id: int,
        _name: str,
        _developer: str,
        _price: float,
        _description: str,
        _win_support: bool,
        _mac_support: bool,
        _linux_support: bool,
        _positive_reviews: int,
        _negative_reviews: int,
    ) -> None:
        
        self.id = _id
        self.name = _name
        self.developer = _developer
        self.price = (_price / 100)
        self.description = _description
        self.win_support = _win_support
        self.mac_support = _mac_support
        self.linux_Sup = _linux_support
        self.positive_reviews = _positive_reviews
        self.negative_reviews = _negative_reviews
        

    def add_genre(self, genre : Tuple[int, str]):
        self.genres.append(genre)

    def add_category(self, category : Tuple[int, str]):
        self.categories.append(category)

    def add_languages(self, language : Tuple[int, str]):
        self.genres.append(language)
