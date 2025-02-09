class Prudoct:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def adding(self,review):
        self.reviews.append(review.feedbacks)

class Review:
    def __init__(self, rating, product, feedback,nameofcustomer):
        self.feedback = feedback
        self.feedbacks = {'name': nameofcustomer, 'rating': rating, 'feedback': feedback}
        self.rating = rating


class Calcul:
    def __init__(self,pruduct):
        sums = 0
        number = 0
        for i in pruduct.reviews:
            sums += i['rating']
            number += 1
        self.finalrating = sums / number

class show:
    def __init__(self,finalratings,prudoct,reviewamount):
        print(f'rating:{finalratings}\nnumber of revieews: {len(prudoct.reviews)}')
        for i in prudoct.reviews:
            print(f'{i}\n')
numberofreviews = 0
ratings = []
laptop = Prudoct('laptop')
review1 = Review(4, laptop, 'Great performance, but battery life could be better', 'customer1')
laptop.adding(review1)


review2 = Review(5, laptop, 'Excellent laptop, highly recommend', 'customer2')
laptop.adding(review2)
review3 = Review(3, laptop, 'Good value, but the screen is too dim', 'customer3')
laptop.adding(review3)

review4 = Review(2, laptop, 'Disappointed with the build quality', 'customer4')
laptop.adding(review4)

review5 = Review(4, laptop, 'Overall very satisfied, but it heats up quickly', 'customer5')
laptop.adding(review5)

for i in laptop.reviews:
        ratings.append(i['rating'])
finals = Calcul(laptop).finalrating
show(finals,laptop,numberofreviews)
