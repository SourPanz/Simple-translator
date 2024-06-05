from vocab import vocabulary

class Translator:
    '''Some stupid conversion input string to gibberish and back'''
    def __init__(self, vocabulary) -> None:
        self.vocabulary = vocabulary
    
    def encrypt(self, sentence: str) -> str:
        #look for a suitable value by key in dict and replace char in input with it
        encoded_str = str()
        s = sentence.upper()
        
        for char in s:
            if char in self.vocabulary.keys():
                encoded_str += self.vocabulary[char]
            else:
                encoded_str += char
                
        return encoded_str.capitalize()
                 
    
    def decrypt(self, sentence: str) -> str:
        #check symbol. if letter, find same sequence in value and replace its key
        s = sentence.lower()
        decoded_str = str()
        items = list(self.vocabulary.items())
        i = 0
        
        while i < len(s):
            if s[i] in 'штныуо':
                for t in items:
                    try:
                        t.index(s[i:i+8])           
                    except ValueError:
                        continue
                    else:
                        decoded_str += t[0]
                        i = i + 8 
                        break
                    
            else:    
                decoded_str += s[i]
                i = i + 1
            
        return decoded_str.capitalize()
            
                
    
    def get_data(self) -> None:
        return input()


if __name__ == "__main__":
    C = Translator(vocabulary)    
    data = C.get_data()
    encrypt = C.encryptor(data)
    decrypt = C.decryptor(encrypt)
    print('translated text: ', encrypt)
    print('original text: ', decrypt)


