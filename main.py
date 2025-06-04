import sys
from stats import word_count
from stats import char_count
from stats import report

def main():
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   book_path = sys.argv[1]
   text = get_book_text(book_path)
   print(text)
   words = word_count(text)
   chars = char_count(text)
   report(book_path, words, chars)

def get_book_text(filepath):
   with open(filepath) as f:
      return f.read()



main()
