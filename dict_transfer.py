fr_en_dict={}
f=open('tinelex_FR_EN.dix','r')

for line in f.readlines():
    s=str(line)
    while s.find('?')!=-1:
        pos_q = s.find('?')
        pos_q_ends = s.find(':',pos_q,len(s))
        pos_q_next = s.find('?',pos_q_ends,len(s))
        fr_en_dict[s[pos_q+1:pos_q_ends]]=s[1:s.find(']')]
        if pos_q_next!=-1:
            s=s[0:s.find(']')+1]+ s[pos_q_next-1:len(s)]
        else:
            break
f_out=open('FR_EN.dict','w')
for f,e in fr_en_dict.items():
    line=f+':'+e+'\n'
    f_out.write(line)

#f.close()
f_out.close()