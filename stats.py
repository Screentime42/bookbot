def word_count(text):
   num_words = len(text.split())
   print(f"{num_words} words found in the document")
   return num_words

def char_count(text):
   text = text.lower()
   chars = {}
   for char in text:
      if not char.isalpha():
         continue
      if char in chars: 
         chars[char] += 1
      else:
         chars[char] = 1
   return chars

def report(book_path, words, chars):
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}...")
   print("----------- Word Count ----------")
   print(f"Found {words} total words")
   print("--------- Character Count -------")
   sorted_chars = list(chars.items())
   sorted_chars.sort(key=lambda item: item[1], reverse=True)
   for char, count in sorted_chars:
      print(f"{char}: {count}")
   print("============= END ===============")