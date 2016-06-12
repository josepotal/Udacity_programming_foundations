import urllib

## the function 'open' is a built in function of the stardand pthon library
def read_text():
    quotes = open("C:\Users\Josep\Dropbox (Personal)\UDACITY\Programming foundations\lesson_4_profanity_words\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)
    
## 'open' function returns an object of the file type


def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if 'true' in output:
        print ('Profanity Alert!!')
    elif 'false' in output:
        print ('This document has no curse words!')
    else:
        print('Could not scan the document properly')
read_text()
