from typing import List
def encrypt(message : List[str]) -> List[str]:
    encrpytionMap = {"A":"!","B":"_","C":"-","D":"#","E":"¤","F":"%","G":"&","H":"/","I":"(","J":")","K":"=","L":"?","M":"+","N":"´","O":"`","P":"|","Q":"}","R":"]","S":"[","T":"{","U":"$","V":"£","W":"@","X":"^","Y":"¨","Z":"~"}
    encryptedMsg = ""
    for everyChar in message :
        encryptedMsg += encrpytionMap[everyChar]
    return encryptedMsg
def decrypt(encryptedMsg : List)->List[str]:
    decrpytionMap = {"!":"A","_":"B","-":"C","#":"D","¤":"E","%":"F","&":"G","/":"H","(":"I",")":"J","=":"K","?":"L","+":"M","´":"N","`":"O","|":"P","}":"Q","]":"R","[":"S","{":"T","$":"U","£":"V","@":"W","^":"X","¨":"Y","~":"Z"}
    decryptedMsg = ""
    for everyChar in encryptedMsg :
        decryptedMsg += decrpytionMap[everyChar]
    return decryptedMsg
message = "HELLO"
encryptedMsg = encrypt(message)
print("original message :",message)
print("encryted message :",encryptedMsg)
decryptedMsg = decrypt(encryptedMsg)
print("decrypted message :",decryptedMsg)

