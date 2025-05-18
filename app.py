from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('C:/Users/admin/OneDrive/Desktop/Project/templates/popular.pkl', 'rb'))
pt = pickle.load(open('C:/Users/admin/OneDrive/Desktop/Project/templates/pt.pkl', 'rb'))
books = pickle.load(open('C:/Users/admin/OneDrive/Desktop/Project/templates/books.pkl', 'rb'))
similarity_scores = pickle.load(open('C:/Users/admin/OneDrive/Desktop/Project/templates/similarity_scores.pkl', 'rb'))

# mood_book_map = {
#     'happy': [
#         'The Alchemist',
#         'Harry Potter and the Sorcerer\'s Stone',
#         'The Secret',
#         'Eleanor Oliphant Is Completely Fine',
#         'The Rosie Project',
#         'Wonder',
#         'Good Omens',
#         'The Hitchhiker\'s Guide to the Galaxy',
#         'Bridget Jones\'s Diary',
#         'Bossypants',
#         'The Hunger Games',
#         'To Kill a Mockingbird',
#         'The Fault in Our Stars'
#     ],
#     'sad': [
#         'A Man Called Ove',
#         'The Fault in Our Stars',
#         'Me Before You',
#         'The Book Thief',
#         'Extremely Loud & Incredibly Close',
#         'The Lovely Bones',
#         'The Perks of Being a Wallflower',
#         'The Catcher in the Rye',
#         'The Kite Runner',
#         'Never Let Me Go',
#         'Les Misérables',
#         '1984',
#         'Of Mice and Men'
#     ],
#     'motivated': [
#         'Atomic Habits',
#         'Can\'t Hurt Me',
#         'Deep Work',
#         'Grit',
#         'Start with Why',
#         'The Power of Habit',
#         'Drive',
#         'Make Your Bed',
#         'Mindset',
#         'The 7 Habits of Highly Effective People',
#         'Think and Grow Rich',
#         'How to Win Friends and Influence People',
#         'You Are a Badass'
#     ],
#     'romantic': [
#         'Pride and Prejudice',
#         'The Notebook',
#         'Twilight',
#         'Outlander',
#         'Jane Eyre',
#         'Me Before You',
#         'The Time Traveler\'s Wife',
#         'Wuthering Heights',
#         'Love in the Time of Cholera',
#         'Anna Karenina',
#         'The Fault in Our Stars',
#         'Call Me by Your Name',
#         'The Great Gatsby'
#     ],
#     'adventure': [
#         'The Hobbit',
#         'Treasure Island',
#         'Life of Pi',
#         'The Call of the Wild',
#         'Into the Wild',
#         'Jurassic Park',
#         'The Martian',
#         'The Odyssey',
#         'Hatchet',
#         'The Jungle Book',
#         'Percy Jackson & the Olympians',
#         'The Maze Runner'
#     ],
#     'mystery': [
#         'Gone Girl',
#         'The Girl with the Dragon Tattoo',
#         'Sherlock Holmes: The Complete Novels and Stories',
#         'The Da Vinci Code',
#         'Big Little Lies',
#         'In the Woods',
#         'And Then There Were None',
#         'The Silence of the Lambs',
#         'The Woman in White',
#         'Rebecca',
#         'Agatha Christie’s Murder on the Orient Express',
#         'The Hound of the Baskervilles',
#         'Sharp Objects'
#     ],
#     'chill': [
#         'Norwegian Wood',
#         'The Secret Garden',
#         'The Wind in the Willows',
#         'The Little Prince',
#         'Where the Crawdads Sing',
#         'A Man Called Ove',
#         'Garden Spells',
#         'The House on Mango Street',
#         'Stardust',
#         'Anne of Green Gables'
#     ],
#     'inspirational': [
#         'The Power of Now',
#         'Man\'s Search for Meaning',
#         'The Four Agreements',
#         'Daring Greatly',
#         'The Untethered Soul',
#         'The Art of Happiness',
#         'You Can Heal Your Life',
#         'The Monk Who Sold His Ferrari',
#         'Big Magic',
#         'The Road Less Traveled'
#     ],
#     'thriller': [
#         'The Silent Patient',
#         'The Woman in Cabin 10',
#         'Before I Go to Sleep',
#         'Shutter Island',
#         'The Girl on the Train',
#         'Misery',
#         'The Reversal',
#         'The Bourne Identity',
#         'Dark Places',
#         'The Couple Next Door'
#     ],
#     'fantasy': [
#         'Harry Potter and the Sorcerer\'s Stone',
#         'The Name of the Wind',
#         'Mistborn',
#         'The Way of Kings',
#         'Eragon',
#         'The Lies of Locke Lamora',
#         'The Blade Itself',
#         'A Game of Thrones',
#         'The Wheel of Time',
#         'The Dark Tower'
#     ],
#     'sci-fi': [
#         'Dune',
#         'Ender\'s Game',
#         'Neuromancer',
#         'The Martian',
#         'Ready Player One',
#         'Snow Crash',
#         'Foundation',
#         'Altered Carbon',
#         'The Left Hand of Darkness',
#         'Hyperion'
#     ],
#     'historical': [
#         'All the Light We Cannot See',
#         'The Book Thief',
#         'Wolf Hall',
#         'The Pillars of the Earth',
#         'Gone with the Wind',
#         'The Help',
#         'A Tale of Two Cities',
#         'The Other Boleyn Girl',
#         'The Nightingale',
#         'Memoirs of a Geisha'
#     ],
#     'self-help': [
#         'How to Win Friends and Influence People',
#         'The 7 Habits of Highly Effective People',
#         'Think and Grow Rich',
#         'You Are a Badass',
#         'The Power of Habit',
#         'Awaken the Giant Within',
#         'The Subtle Art of Not Giving a F*ck',
#         'Make Your Bed',
#         'The Miracle Morning',
#         'Mindset'
#     ]
# }


mood_book_map = {
    'happy': [
        'The Alchemist', 'Harry Potter and the Sorcerer\'s Stone', 'The Secret', 'Eleanor Oliphant Is Completely Fine',
        'Wonder', 'Good Omens', 'The Rosie Project', 'Bossypants', 'Yes Please', 'Where’d You Go, Bernadette',
        'The 100-Year-Old Man Who Climbed Out the Window and Disappeared', 'My Grandmother Asked Me to Tell You She’s Sorry',
        'Oona Out of Order', 'A Man Called Ove', 'Love Your Life'
    ],
    'sad': [
        'The Book Thief', 'Me Before You', 'The Lovely Bones', 'The Kite Runner', 'A Little Life',
        'Extremely Loud & Incredibly Close', 'The Light Between Oceans', 'Bridge to Terabithia', 'The Midnight Library',
        'The Art of Racing in the Rain', 'Room', 'My Sister’s Keeper', 'We Were Liars', 'They Both Die at the End',
        'If I Stay'
    ],
    'motivated': [
        'Atomic Habits', 'Deep Work', 'Grit', 'The Power of Habit', 'Can\'t Hurt Me', 'Make Your Bed',
        'Mindset', 'The 7 Habits of Highly Effective People', 'Think and Grow Rich', 'The Magic of Thinking Big',
        'The War of Art', 'Limitless', 'Drive', 'Start with Why', 'Do the Work'
    ],
    'romantic': [
        'Pride and Prejudice', 'The Notebook', 'The Time Traveler’s Wife', 'Call Me by Your Name', 'Red, White & Royal Blue',
        'Beach Read', 'Outlander', 'People We Meet on Vacation', 'The Kiss Quotient', 'It Ends with Us',
        'One Day', 'The Love Hypothesis', 'The Hating Game', 'Jane Eyre', 'Love and Other Words'
    ],
    'adventure': [
        'The Hobbit', 'Life of Pi', 'The Martian', 'Into the Wild', 'The Call of the Wild',
        'Treasure Island', 'Jurassic Park', 'Around the World in 80 Days', 'The Three Musketeers', 'The Maze Runner',
        'Percy Jackson & the Olympians', 'Ready Player One', 'Hatchet', 'Journey to the Center of the Earth',
        'The Golden Compass'
    ],
    'mystery': [
        'Gone Girl', 'The Girl with the Dragon Tattoo', 'The Da Vinci Code', 'In the Woods', 'The Silent Patient',
        'Big Little Lies', 'Sharp Objects', 'The Woman in White', 'The Girl on the Train', 'Before I Go to Sleep',
        'Behind Closed Doors', 'The Couple Next Door', 'The Family Upstairs', 'And Then There Were None',
        'The Hound of the Baskervilles'
    ],
    'chill': [
        'The Little Prince', 'The Secret Garden', 'Anne of Green Gables', 'The Wind in the Willows', 'Where the Crawdads Sing',
        'Stardust', 'Garden Spells', 'Norwegian Wood', 'Eleanor & Park', 'The House on Mango Street',
        'The Giver of Stars', 'Little Women', 'The Flatshare', 'Evvie Drake Starts Over', 'The Midnight Library'
    ],
    'inspirational': [
        'The Power of Now', 'Man\'s Search for Meaning', 'The Four Agreements', 'Daring Greatly', 'The Untethered Soul',
        'The Art of Happiness', 'You Can Heal Your Life', 'The Monk Who Sold His Ferrari', 'Big Magic', 'Tuesdays with Morrie',
        'The Last Lecture', 'The Gifts of Imperfection', 'The Road Less Traveled', 'Braving the Wilderness',
        'Think Like a Monk'
    ],
    'thriller': [
        'The Silent Patient', 'Shutter Island', 'Before I Go to Sleep', 'Misery', 'Behind Closed Doors',
        'The Girl on the Train', 'The Woman in Cabin 10', 'The Reversal', 'The Chain', 'I Am Watching You',
        'Verity', 'Home Before Dark', 'The Turn of the Key', 'The Girl Beneath the Sea', 'Final Girls'
    ],
    'fantasy': [
        'Harry Potter and the Sorcerer\'s Stone', 'A Game of Thrones', 'The Name of the Wind', 'The Way of Kings', 'Mistborn',
        'Eragon', 'The Lies of Locke Lamora', 'The Priory of the Orange Tree', 'Throne of Glass', 'Six of Crows',
        'The Dark Tower', 'The Wheel of Time', 'An Ember in the Ashes', 'The Night Circus', 'The House in the Cerulean Sea'
    ],
    'sci-fi': [
        'Dune', 'Ender\'s Game', 'The Martian', 'Neuromancer', 'Foundation', 'Snow Crash', 'Hyperion', 'The Left Hand of Darkness',
        'Ready Player One', 'Altered Carbon', 'The Three-Body Problem', 'Project Hail Mary', 'The Power', 'Red Mars',
        'Dark Matter'
    ],
    'historical': [
        'All the Light We Cannot See', 'The Book Thief', 'The Help', 'The Nightingale', 'Memoirs of a Geisha',
        'Wolf Hall', 'The Pillars of the Earth', 'The Tattooist of Auschwitz', 'The Paris Library', 'A Gentleman in Moscow',
        'The Alice Network', 'Beneath a Scarlet Sky', 'The Guernsey Literary and Potato Peel Pie Society',
        'The Other Boleyn Girl', 'A Tale of Two Cities'
    ],
    'self-help': [
        'How to Win Friends and Influence People', 'Think and Grow Rich', 'Atomic Habits', 'You Are a Badass',
        'The Subtle Art of Not Giving a F*ck', 'Awaken the Giant Within', 'The Power of Now', 'The 7 Habits of Highly Effective People',
        'Make Your Bed', 'Mindset', 'Can\'t Hurt Me', 'The Miracle Morning', 'Who Moved My Cheese?', 'Feel the Fear and Do It Anyway',
        'The Confidence Code'
    ]
}

app = Flask(__name__)


@app.route('/')
def index():
        return render_template('index.html',
                            book_name=list(popular_df['Book-Title'].values),
                            author=list(popular_df['Book-Author'].values),
                            image=list(popular_df['Image-URL-M'].values),
                            votes=list(popular_df['num_ratings'].values), 
                            rating=list(popular_df['avg_rating'].values),
                                 )




@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

    
@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    
    if user_input not in pt.index:
        # Book not found
        return render_template('recommend.html', error="Book not found. Please try another title.")

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data, user_input=user_input)


import random
# @app.route('/get_books_from_mood', methods=['POST'])
# def get_books_from_mood():
#     mood = request.form.get('mood')
#     books_for_mood = mood_book_map.get(mood.lower(), [])

#     if not books_for_mood:
#         return render_template('select_book.html', mood=mood, books=[], error="No books available for this mood.")

#     # Select 4 random books (or fewer if less available)
#     selected_books = random.sample(books_for_mood, min(4, len(books_for_mood)))

#     # Get book details from the 'books' DataFrame
#     recommended_books = []
#     for book_title in selected_books:
#         temp_df = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')
#         if not temp_df.empty:
#             recommended_books.append({
#                 'title': temp_df['Book-Title'].values[0],
#                 'author': temp_df['Book-Author'].values[0],
#                 'image': temp_df['Image-URL-M'].values[0]
#             })

#     return render_template('select_book.html', mood=mood, books=recommended_books)

@app.route('/get_books_from_mood', methods=['POST'])
def get_books_from_mood():
    mood = request.form.get('mood')
    books_for_mood = mood_book_map.get(mood.lower(), [])

    if not books_for_mood:
        return render_template('select_book.html', mood=mood, books=[], error="No books available for this mood.")

    # Pick 3 random base books for the mood
    selected_books = random.sample(books_for_mood, min(3, len(books_for_mood)))

    recommended_books = []

    for mood_book in selected_books:
        if mood_book in pt.index:
            index = np.where(pt.index == mood_book)[0][0]
            # Get top 4 similar books for each mood book
            similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

            for i in similar_items:
                temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
                if not temp_df.empty:
                    recommended_books.append({
                        'base': mood_book,
                        'title': temp_df['Book-Title'].values[0],
                        'author': temp_df['Book-Author'].values[0],
                        'image': temp_df['Image-URL-M'].values[0]
                    })
        else:
            # If mood book not in pt, include it directly
            temp_df = books[books['Book-Title'] == mood_book].drop_duplicates('Book-Title')
            if not temp_df.empty:
                recommended_books.append({
                    'base': mood_book,
                    'title': temp_df['Book-Title'].values[0],
                    'author': temp_df['Book-Author'].values[0],
                    'image': temp_df['Image-URL-M'].values[0]
                })

    return render_template('select_book.html', mood=mood, books=recommended_books)


@app.route('/select_mood')
def select_mood():
    moods = list(mood_book_map.keys())  # List of all moods
    return render_template('select_mood.html', moods=moods)


if __name__ == '__main__':
    app.run(debug=True) 

