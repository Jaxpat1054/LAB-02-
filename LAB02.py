def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'Full name' : 'Jaxay Dilipkumar Patel',
        'firstname' : 'Jaxay',
        'Student ID' : '10285868',
        'pizza toppings' : [
            'Green pepper',
            'Onion',
            'Black olives',

        ],      
        'movies' : [
            {
                'title' : 'Extraction', #about_me['movies'][0]['title']
                'genre' : 'adventerous' #about_me['movies'][0]['genre']
            },
            {
                'title' : 'Battelship', #about_me['movies'][1]['title'] 
                'genre' : 'thriller'    #about_me['movies'][1]['genre'] 
            }

                ]                 

    }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title' : 'harry potter', 'genre' : 'mysterious'})

    
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('jalapeno', 'green olives', 'mushroom' ))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)
    return
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f"My full name is {about_me['Full name']}, but you can call me jalim {about_me['firstname']}",end='.\n')
    print(f"My student ID is {about_me['Student ID']}",end='.\n')
    return

    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza toppings'].extend(toppings)
    about_me['pizza toppings'].sort()
   
    for a,t in enumerate( about_me['pizza toppings']):
        if a <= 3:
            about_me['pizza toppings'][a] =t
            break
        print(f'- {t}').upper()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    #about_me['pizza toppings']
    about_me['pizza toppings'].sort()
    print(f'\nMy favourite pizza toppings are: ')
    for t in  (about_me['pizza toppings']):
        #about_me['pizza toppings']
        print(f'- {t.lower()}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    #print(f"Some of my favourite movies are {about_me['movies']}", end=" ")

    genres = [m['genre'] for m in about_me['movies']]
    print(f"\nI like to watch {', '.join(genres)} movies",end='.\n') 
    #print(', '.join(genres) , end=' ')
    return 



# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    movies = [l['title'] for l in about_me['movies']]
    print(f"\nSome of my favourites movies are {', '.join(movies).title()}",end='!')
    return
    
if __name__ == '__main__':
    main()