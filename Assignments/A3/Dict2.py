movies = ["Monty Python and the Holy Grail", "Monty Python's Life of Brian", "Monty Python's Meaning of Life", "And Now For Something Completely Different"]
grail_ratings = [9, 10, 9.5, 8.5, 3, 7.5, 8]
brian_ratings = [10, 10, 0, 9, 1, 8, 7.5 , 8, 6, 9]
life_ratings = [7, 6, 5]
different_ratings = [6, 5, 6, 6]
ratings = [grail_ratings,brian_ratings,life_ratings,different_ratings]
d = {}
for x,y in zip(movies,ratings):
    d[x] = y
for x,y in d.items():
    print(f'{x}: {(sum(y)/len(y)):1.1f}')
