import os
import sys

import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, LabelBinarizer,LabelEncoder


class Text2wordlist():
    def __init__(self):
        self.file = sys.path[0]
    def wordlist(self,train,label,max_len,file = None,Word_percent = 0.95,lb_mode = None,test_size = 0.1):
        # train是要传入的分过词的文本列表，cutword 的结果。label 是对应的标签
        if file == None:
            file = self.file
        if lb_mode == "B":
            lb = LabelBinarizer()
        if lb_mode == "E":
            lb = LabelEncoder()
        if lb_mode == "M":
            lb = MultiLabelBinarizer()
            label = [tuple(i.split(" ")) for i in label]
        y_train = lb.fit_transform(label)
        joblib.dump(lb, os.path.join(file,'lb.model'))

        if os.path.exists(os.path.join(file,'tokenizer.model')):
            tokenizer = joblib.load(os.path.join(file,'tokenizer.model'))
        else:
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts(train)
            if Word_percent == 1:
                tokenizer.num_words = len(tokenizer.word_counts)
            else:
                num = sorted(tokenizer.word_counts.values(), reverse=True)
                count = int(np.sum(num) * Word_percent)
                a = 0
                for i in range(len(num)):
                    a += num[i]
                    if a > count:
                        tokenizer.num_words = i
                        break
            joblib.dump(tokenizer, os.path.join(file,'tokenizer.model'))
        train_list = tokenizer.texts_to_sequences(train)
        x_train = pad_sequences(train_list,max_len)
        train_x, test_x, train_y, test_y = train_test_split(x_train, y_train, test_size=test_size, random_state=10)
        return train_x, test_x, train_y, test_y,tokenizer.num_words