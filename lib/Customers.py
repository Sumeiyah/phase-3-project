from Review import Review 
class Customers:
    _all = []

    def __init__(self,given_name,family_name) :
        self.given_name = given_name
        self.family_name = family_name
    
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.given_name
    def full_name(self):
        return f'{self.given_name} {self.family_name}'
    
    @classmethod
    def all (cls):
        return cls.all
    
    def restaurants(self):
        return [review.restaurant() for review in self._reviews]
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)
    
    def num_reviews(self):
        return len(self._reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls._all if customer.given_name() == name]
