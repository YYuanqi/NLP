#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(text):
    encoded_text = []
    for i in range(len(text)):
        if 'a' <= text[i] <= 'z':
            encoded_text.append(str(219 - ord(text[i])))
        else:
            encoded_text.append(text[i])
    return (''.join(encoded_text))

print (cipher('adfqqqqqqio1341lZKJFWOer1LJKLFJSODFU9239054'))