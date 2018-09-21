#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ
import random

def typoglycemia(text):
    text_list =  text.split()
    result_list = []
    for word in text_list:
        if len(word)>=4:
            temp_list = list(word)[1:-1]
            random.shuffle(temp_list)
            result_list.append(word[0]+''.join(temp_list)+word[len(word)-1])
        else:
            result_list.append(word)
    return (result_list)


a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print (typoglycemia(a))
