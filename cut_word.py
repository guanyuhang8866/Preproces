import os
import re
import sys

import jieba
from pkuseg import pkuseg


class Cutword:

    def __init__(self,name = "Cutword"):
        self.name = name
        self.pku_cut = pkuseg()
        self.file = sys.path[0]

    def jieba_cut(self,text,file = None):
        result = []
        if file == None:
            file = self.file
        txt = open(os.path.join(file,"CuttedWord.txt"),"w",encoding = "utf-8")
        for i in text:
            restr = '[0-9\s+\.\!\/_,$%^*();?:\-<>《》【】+\"\']+|[+——！，；。？：、~@#￥%……&*（）]+'
            resu = i.replace('|', '').replace('&nbsp;', '').replace('ldquo', '').replace('rdquo',
                                                                                            '').replace(
                'lsquo', '').replace('rsquo', '').replace('“', '').replace('”', '').replace('〔', '').replace('〕', '')
            resu = re.split(r'\s+', resu)
            dr = re.compile(r'<[^>]+>', re.S)
            dd = dr.sub('', ''.join(resu))
            line = re.sub(restr, '', dd)
            seg_list = jieba.lcut(line)
            out = " ".join(seg_list)
            result.append(out)
            txt.write(out + "\n")
        txt.close()
        return result

    def pkuseg_cut(self,text,file = "None"):
        result = []
        if file == None:
            file = self.file
        txt = open(os.path.join(file, "CuttedWord.txt"), "w", encoding="utf-8")
        for i in text:
            restr = '[0-9\s+\.\!\/_,$%^*();?:\-<>《》【】+\"\']+|[+——！，；。？：、~@#￥%……&*（）]+'
            resu = i.replace('|', '').replace('&nbsp;', '').replace('ldquo', '').replace('rdquo',
                                                                                         '').replace(
                'lsquo', '').replace('rsquo', '').replace('“', '').replace('”', '').replace('〔', '').replace('〕', '')
            resu = re.split(r'\s+', resu)
            dr = re.compile(r'<[^>]+>', re.S)
            dd = dr.sub('', ''.join(resu))
            line = re.sub(restr, '', dd)
            seg_list = self.pku_cut.cut(line)
            out = " ".join(seg_list)
            result.append(out)
            txt.write(out + "\n")
        txt.close()
        return result