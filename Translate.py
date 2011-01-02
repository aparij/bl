import re
from datetime import datetime


class Translate:

    dictionary = {}
    book_file = None
    def __init__(self):
        '''
        '''
        
    
    def read_dict(self,from_lang, to_lang):
        '''
            
        '''
        f=open(from_lang+ '_' + to_lang + '.dict','r')
        for line in f.readlines():
            s=str(line)
            pos=s.find(':')
            self.dictionary[s[:pos]]=s[pos+1:len(s)-1]
        f.close()
            
    def read_and_translate_file(self,book_file):
        '''
        '''
        print datetime.now()
        self.book_file = book_file
        f = open(book_file,'r')
        translated_as_string = []
        translated_list = []
        for line in f.readlines():
            s=str(line)
            s.strip()
            token_list = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", s)
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

            translated_list.append('\n')
        translated_as_string = "".join(translated_list)
        f.close()
        print datetime.now()

        return translated_as_string

    def write_file(self,translated_string):
        '''
        '''
        f_out=open(self.book_file + '.TR','w')
        f_out.write(translated_string)
        f_out.close()

