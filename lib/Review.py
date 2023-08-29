class Review:
    _all = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self.__class__._all.append(self)
    
    def rating(self):
        return self._rating
    
    @classmethod
    def all(cls):
        return cls._all
    
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant
