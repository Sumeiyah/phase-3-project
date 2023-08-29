from Customers import Customers
from Restaurant import Restaurant
from Review import Review

# Create instances
customer1 = Customers("John", "Doe")
customer2 = Customers("Jane", "Smith")

restaurant1 = Restaurant("Sample Restaurant")
restaurant2 = Restaurant("sample Restaurant 2")
review1 = Review(customer1, restaurant1, 4)

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

    


    




# Print information
print(customer1.full_name())
print(restaurant1.name())
print(review1.rating())
print(restaurant1.name())   
print(restaurant1.reviews())   
print(restaurant1.customers())  
print(restaurant1.average_star_rating())  



