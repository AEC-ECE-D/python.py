def rev_sentence(sentence): 
    words = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence 
if __name__ == "__main__": 
    str=input()
    print (rev_sentence(str))
