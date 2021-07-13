current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Christmas Vacation': '5:00pm'
}

print('We are showing the following movies:')
for movie in current_movies:
    print(movie)

movie = input('\nWhat movie would you like to see? ')

showtime = current_movies.get(movie)
if showtime == None:
    print('Movie does not exist')
else:
    print('Movie plays at', showtime)