# Name:Arati Vijay Walte
# ASSIGNMENT No. 4 (a)
# Roll No. 67
# Batch : B4
# TITLE: Generating Unigrams,Bigrams and Trigrams in nltk (File).

from nltk import ngrams


def n_g(n):
  file = open("sample.txt")
  for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
      print("For sentence", counter + 1, n, "grams are: ")
      trigrams = ngrams(sentence.split(" "), n)
      for grams in trigrams:
        print(grams)
      counter += 1
      print()


print("Unigrams:")
n_g(1)
print("\nBigrams:")
n_g(2)
print("\nTrigrams:")
n_g(3)

#OUTPUT:
# Unigrams:
# For sentence 1 1 grams are:
# ('C#',)
# ('was',)
# ('designed',)
# ('as',)
# ('part',)
# ('of',)
# ('the',)
# ('Microsoft',)
# ('',)

# For sentence 2 1 grams are:
# ('NET',)
# ('platform,',)
# ('aiming',)
# ('to',)
# ('provide',)
# ('a',)
# ('versatile',)
# ('and',)
# ('powerful',)
# ('language',)
# ('for',)
# ('building',)
# ('Windows',)
# ('applications',)

# For sentence 3 1 grams are:
# ('\n',)

# For sentence 1 1 grams are:
# ('It',)
# ('is',)
# ('now',)
# ('used',)
# ('for',)
# ('a',)
# ('wide',)
# ('range',)
# ('of',)
# ('applications,',)
# ('including',)
# ('web',)
# ('development,',)
# ('desktop',)
# ('software,',)
# ('mobile',)
# ('apps',)
# ('(via',)
# ('Xamarin),',)
# ('cloud',)
# ('services,',)
# ('and',)
# ('more',)

# For sentence 2 1 grams are:
# ('C#',)
# ('syntax',)
# ('is',)
# ('similar',)
# ('to',)
# ('other',)
# ('C-style',)
# ('languages',)
# ('such',)
# ('as',)
# ('C++',)
# ('and',)
# ('Java,',)
# ('making',)
# ('it',)
# ('relatively',)
# ('easy',)
# ('for',)
# ('programmers',)
# ('familiar',)
# ('with',)
# ('those',)
# ('languages',)
# ('to',)
# ('transition',)
# ('to',)
# ('C#',)

# For sentence 3 1 grams are:
# ('',)

# Bigrams:
# For sentence 1 2 grams are:
# ('C#', 'was')
# ('was', 'designed')
# ('designed', 'as')
# ('as', 'part')
# ('part', 'of')
# ('of', 'the')
# ('the', 'Microsoft')
# ('Microsoft', '')

# For sentence 2 2 grams are:
# ('NET', 'platform,')
# ('platform,', 'aiming')
# ('aiming', 'to')
# ('to', 'provide')
# ('provide', 'a')
# ('a', 'versatile')
# ('versatile', 'and')
# ('and', 'powerful')
# ('powerful', 'language')
# ('language', 'for')
# ('for', 'building')
# ('building', 'Windows')
# ('Windows', 'applications')

# For sentence 3 2 grams are:

# For sentence 1 2 grams are:
# ('It', 'is')
# ('is', 'now')
# ('now', 'used')
# ('used', 'for')
# ('for', 'a')
# ('a', 'wide')
# ('wide', 'range')
# ('range', 'of')
# ('of', 'applications,')
# ('applications,', 'including')
# ('including', 'web')
# ('web', 'development,')
# ('development,', 'desktop')
# ('desktop', 'software,')
# ('software,', 'mobile')
# ('mobile', 'apps')
# ('apps', '(via')
# ('(via', 'Xamarin),')
# ('Xamarin),', 'cloud')
# ('cloud', 'services,')
# ('services,', 'and')
# ('and', 'more')

# For sentence 2 2 grams are:
# ('C#', 'syntax')
# ('syntax', 'is')
# ('is', 'similar')
# ('similar', 'to')
# ('to', 'other')
# ('other', 'C-style')
# ('C-style', 'languages')
# ('languages', 'such')
# ('such', 'as')
# ('as', 'C++')
# ('C++', 'and')
# ('and', 'Java,')
# ('Java,', 'making')
# ('making', 'it')
# ('it', 'relatively')
# ('relatively', 'easy')
# ('easy', 'for')
# ('for', 'programmers')
# ('programmers', 'familiar')
# ('familiar', 'with')
# ('with', 'those')
# ('those', 'languages')
# ('languages', 'to')
# ('to', 'transition')
# ('transition', 'to')
# ('to', 'C#')

# For sentence 3 2 grams are:

# Trigrams:
# For sentence 1 3 grams are:
# ('C#', 'was', 'designed')
# ('was', 'designed', 'as')
# ('designed', 'as', 'part')
# ('as', 'part', 'of')
# ('part', 'of', 'the')
# ('of', 'the', 'Microsoft')
# ('the', 'Microsoft', '')

# For sentence 2 3 grams are:
# ('NET', 'platform,', 'aiming')
# ('platform,', 'aiming', 'to')
# ('aiming', 'to', 'provide')
# ('to', 'provide', 'a')
# ('provide', 'a', 'versatile')
# ('a', 'versatile', 'and')
# ('versatile', 'and', 'powerful')
# ('and', 'powerful', 'language')
# ('powerful', 'language', 'for')
# ('language', 'for', 'building')
# ('for', 'building', 'Windows')
# ('building', 'Windows', 'applications')

# For sentence 3 3 grams are:

# For sentence 1 3 grams are:
# ('It', 'is', 'now')
# ('is', 'now', 'used')
# ('now', 'used', 'for')
# ('used', 'for', 'a')
# ('for', 'a', 'wide')
# ('a', 'wide', 'range')
# ('wide', 'range', 'of')
# ('range', 'of', 'applications,')
# ('of', 'applications,', 'including')
# ('applications,', 'including', 'web')
# ('including', 'web', 'development,')
# ('web', 'development,', 'desktop')
# ('development,', 'desktop', 'software,')
# ('desktop', 'software,', 'mobile')
# ('software,', 'mobile', 'apps')
# ('mobile', 'apps', '(via')
# ('apps', '(via', 'Xamarin),')
# ('(via', 'Xamarin),', 'cloud')
# ('Xamarin),', 'cloud', 'services,')
# ('cloud', 'services,', 'and')
# ('services,', 'and', 'more')

# For sentence 2 3 grams are:
# ('C#', 'syntax', 'is')
# ('syntax', 'is', 'similar')
# ('is', 'similar', 'to')
# ('similar', 'to', 'other')
# ('to', 'other', 'C-style')
# ('other', 'C-style', 'languages')
# ('C-style', 'languages', 'such')
# ('languages', 'such', 'as')
# ('such', 'as', 'C++')
# ('as', 'C++', 'and')
# ('C++', 'and', 'Java,')
# ('and', 'Java,', 'making')
# ('Java,', 'making', 'it')
# ('making', 'it', 'relatively')
# ('it', 'relatively', 'easy')
# ('relatively', 'easy', 'for')
# ('easy', 'for', 'programmers')
# ('for', 'programmers', 'familiar')
# ('programmers', 'familiar', 'with')
# ('familiar', 'with', 'those')
# ('with', 'those', 'languages')
# ('those', 'languages', 'to')
# ('languages', 'to', 'transition')
# ('to', 'transition', 'to')
# ('transition', 'to', 'C#')