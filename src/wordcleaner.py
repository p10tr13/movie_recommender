import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

class TitleCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.custom_stopwords = {
            'the', 'a', 'and', 'of', 'in', 'to', 'is', 'it', 'that',
            'for', 'on', '&', 'de', 'la', 'part', 'volume', 'chapter',
            'story', 'film', 'movie', 'series', 'season', 'episode',
            'part'
        }
        self.lemmatizer = WordNetLemmatizer()
        self.all_stopwords = self.stop_words.union(self.custom_stopwords)

    def clean_title(self, title):
        # Usuwanie roku produkcji
        title = re.sub(r'\(\d{4}\)', '', title)
        # Usuwanie znaków specjalnych
        title = re.sub(r'[^\w\s]', ' ', title)
        # Zamiana na małe litery
        title = title.lower()
        # Usuwanie stopwords i lematyzacja
        words = [
            self.lemmatizer.lemmatize(word) 
            for word in title.split() 
            if (word not in self.all_stopwords) and (len(word) > 2)
        ]
        return ' '.join(words)