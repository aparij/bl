__author__ = 'alex_p'


from Translate import Translate


tr = Translate()
tr.read_dict('FR','EN')
translated_string = tr.read_and_translate_file('proust_French.htm')
print len(tr.dictionary)
tr.write_file(translated_string)

