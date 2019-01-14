from cut_word import Cutword
from text2wordlist import Text2wordlist
import time

a = Cutword()
b = Text2wordlist()
text = [i.strip().replace(" ","") for i in open('train1.txt', 'r', encoding='utf8')]
label = [i.strip() for i in open('label1.txt', 'r', encoding='utf8')]
l = time.time()
# p_cut = a.pkuseg_cut(text)
m = time.time()
jie_cut = a.jieba_cut(text)
n = time.time()
print(m-l," ",n-m)
a1,a2,a3,a4, num = b.wordlist(jie_cut,label,1000,lb_mode ="B")

pass