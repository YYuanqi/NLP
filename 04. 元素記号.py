#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
Setence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
DataList = Setence.replace('.','',).split( )
element_table=dict()

for i, element in enumerate(DataList):
    if i == 0  or i == 4 or i == 5 or i == 6  or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        num = 1
        element_table.update([(i+1,element[0:num])])
    else:
        num = 2
        element_table.update([(i+1,element[0:num])])

for k, v in element_table.items():
    print(k,v)