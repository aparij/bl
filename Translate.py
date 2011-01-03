import re
from datetime import datetime
import codecs

class Translate:

    dictionary = {}
    book_file = None
    def __init__(self):
        '''
        '''
        
    
    def read_dict(self,from_lang, to_lang):
        '''
            
        '''
        f=codecs.open(from_lang+ '_' + to_lang + '.dict',encoding='cp1252',mode='r')
        for line in f.readlines():
            s=line
            pos=s.find(':')
            key=s[:pos]
            self.dictionary[key.encode('cp1252')]=s[pos+1:len(s)-1]
        f.close()
            
    def read_and_translate_file(self,book_file):
        '''
        '''
        self.book_file = book_file
        f = codecs.open(book_file,encoding='cp1252',mode='r')
        translated_as_string = []
        translated_list = []
        for line in f.readlines():
            s=line
            s.strip()
            token_list = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", s , flags=re.UNICODE)
            for token in token_list:
                if token.lower() in self.dictionary:
                    translated_list.append(self.dictionary[token.lower()])
                    translated_list.append(' ')
                    #translated_line = translated_line + self.dictionary[token] + ' '
                else:
                    #go to google translate api and find the word, then add it to the dictionary
                    #and rebuild the dictionary
                    #possibly use [[1]] to set a space where later it will be substituted
                    #because it's better to translate from google in big batch of untranslated
                    #words
                    translated_list.append(token)
                    translated_list.append(' ')

            translated_list.append(u'\n')
        translated_as_string = "".join(translated_list)
        f.close()
        print datetime.now()

        return translated_as_string

    def write_file(self,translated_string):
        '''
        '''
        f_out=codecs.open(self.book_file + '.TR',encoding='cp1252',mode='w')
        f_out.write(translated_string)
        f_out.close()

