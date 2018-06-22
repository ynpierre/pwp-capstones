
class TextSample:
    def __repr__(self):
        return "Author Name: {n}\nAverage sentence length is: {a} ".format(n= self.author, a= self.avg_sentence_length)
     

    def __init__(self, text, author, avg_sentence_length, word_count_frequency=0):
        self.raw_text = text
        self.author = author
        self.avg_sentence_length = avg_sentence_length
        self.prepared_text = self.prepare_text(text)
        self.word_count_frequency =word_count_frequency
       
    def prepare_text(self, text):
        punctuations = [',',';','?','!','\"','.']
        text = text.lower()
        for punc in punctuations:
            #print(punc)
            text = text.replace(punc, '')
    
        return text.split(' ')
      
    def build_frequency_table(self):
        frequency_table = {}
        result = 0
        for word in self.prepared_text:
            #print(frequency_table.get(word))
            if(frequency_table.get(word) is not "None"):
                result = frequency_table.get(word, result)
                frequency_table[word] = result + 1

        return frequency_table

    def ngram_creator(self):
        count = 0
        result = ""
        list_of_ngrams =[]
        for word in self.prepared_text:
            if count >=  0 :
                if count == range(len(self.prepared_text)):
                    return list_of_ngrams
                try:
                    result = self.prepared_text[count] + " " + self.prepared_text[count+1]
                except IndexError :
                    continue
                #print(result)
                list_of_ngrams.append(result)
            count += 1
        #print(list_of_ngrams)
        return list_of_ngrams

