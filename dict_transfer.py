import codecs


fr_en_dict={}
f=codecs.open('tinelex_FR_EN.dix',mode='r',encoding='utf-8')

for line in f.readlines():
    s= line
    while s.find('?')!=-1:
        pos_q = s.find('?')
        pos_q_ends = s.find(':',pos_q,len(s))
        pos_q_next = s.find('?',pos_q_ends,len(s))
        fr_en_dict[s[pos_q+1:pos_q_ends]]=s[1:s.find(']')]
        if pos_q_next!=-1:
            s=s[0:s.find(']')+1]+ s[pos_q_next-1:len(s)]
        else:
            break
f_out=codecs.open('FR_EN.dict',encoding='utf-8',mode = 'w')
for f,e in fr_en_dict.items():
    line=f+':'+e+u'\n'
    f_out.write(line)

#f.close()
f_out.close()