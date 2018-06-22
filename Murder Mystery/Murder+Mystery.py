from TextSample import *



def get_average_sentence_length(text):
    #This function returns the average length of a sentence in the text
    sentence_in_text = []
    token = "##"
    total_length = 0
    text = text.replace(".", token)
    text = text.replace("?", token)
    text = text.replace("!",token)
    #print(text)
    sentence_in_text = text.split(token)
    #print(sentence_in_text)
    count = len(sentence_in_text)
    #print(count)
    for a_sentence in sentence_in_text:
        #print(a_sentence + "\n has length of {l}".format(l=len(a_sentence)))
        total_length += len(a_sentence)
      
    average_length = total_length/count
    
    return average_length

def frequency_comparison(table1, table2):
    score = 0
    appearances = 0
    mutual_appearances = 0
    """Iterate through table1's keys and check if table2 has the same key defined. If it is, compare the two values for the key -- the smaller value should get added to mutual_appearances and the larger should get added to appearances. If the key doesn't exist in table2 the value for the key in table1 should be added to appearances."""
    for key, value in table1.items():
        if key in table2:
            #print("Key :"+ key + "Value: "+ str(value))
            if table2[key] > value:
                appearances = appearances+ value
                #print("In key: {k} is greater than value: {val} and apper: {ap}".format(k=key, val=value, ap= appearances ))
            elif table2[key] < value:
                mutual_appearances = mutual_appearances + value
                #print("In key: {k} is less than value: {val} and apper: {ap}".format(k=key, val=value, ap= mutual_appearances ))
            elif table2[key] == value:
                appearances += value
                mutual_appearances += value
        elif key not in table2:
            appearances = appearances + table1[key]
            #print("In key: {k} not in table2 than value: {val} and apper: {ap}".format(k=key, val=value, ap= appearances ))
    #iterate through all of table2's keys that aren't in table1 and add those to appearances as well
    for key,value in table2.items():
        if key not in table1:
            appearances =appearances +  value
            #print("In key: {k} not in table1 than value: {val} and apper: {ap}".format(k=table2[key], val=value, ap= appearances ))
   
    score = mutual_appearances / appearances
    
    return  score

def percent_difference(avgsentence1, avgsentence2):
    result = abs(avgsentence1-avgsentence2)/((avgsentence1+avgsentence2)/2)
    return result

def find_text_similarity(text_sample1, text_sample2):
    result = float(0)
    
    #calculate percent difference
    avg_sentence1_len = get_average_sentence_length(text_sample1.raw_text)
    avg_sentence2_len = get_average_sentence_length(text_sample2.raw_text)
    sentence_length_difference = percent_difference(avg_sentence1_len,avg_sentence2_len)
    sentence_length_similarity = abs(1-sentence_length_difference)
    
    
    #calculate the difference between frequency comparaison
    my_twogram_text_sample1 = text_sample1.ngram_creator()
    my_twogram_text_sample2 = text_sample2.ngram_creator()
   
    mb_frequency_text1 = text_sample1.build_frequency_table()
    mb_frequency_text2 = text_sample1.build_frequency_table()    
    word_count_similarity = frequency_comparison(mb_frequency_text1,mb_frequency_text2)
    
    #Calculate the difference between their two-word ngram using
    ngram_similarity = frequency_comparison(mb_frequency_text1 , mb_frequency_text2)
    
    result = (sentence_length_similarity+ word_count_similarity + ngram_similarity )/3
   
    return result

def who_dunnit(score1, score2,score3):
     if score1 > score2:
         if score1> score3:
             return score1
         elif score3 > score1:
            return score3
     elif score2 > score1:
        if score2 > score3:
            return score2
        else:
            return score3
        
def main():
   murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT?! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."
   lily_trebuchet_intro= "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
   myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a \"walk\". A \"walk\" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
   gregg_t_fishy_intro = "A most good day to you all, I am Gregg T. Fishy, of the Fishy Enterprise fortune. I am 37 years young, an adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might find yourself asking? Why, I happen to always be fishing for compliments of course! I have a stunning pair of radiant blue eyes that will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television, I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life, every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on the television program A Jay To Remember, it certainly seems like a grand time to explore life and love."

#code_author will save the similarity code associated with the author
   code_author = {}
 
   lily_sample =TextSample(lily_trebuchet_intro, "Lily Trebuchet", get_average_sentence_length(lily_trebuchet_intro))
   myrtle_sample =TextSample(myrtle_beech_intro,"Myrtle Beech", get_average_sentence_length(myrtle_beech_intro))
   gregg_sample =TextSample(gregg_t_fishy_intro, "Gregg T. Fishy", get_average_sentence_length(gregg_t_fishy_intro))
   murderer_sample =TextSample(murder_note, "Murder's Note", get_average_sentence_length(murder_note))

   #Find text similarity between author's note and the murdere's note
   lily_text_similarity_code = find_text_similarity(murderer_sample, lily_sample)
   code_author[lily_text_similarity_code] = lily_sample.author

   myrtle_text_similarity_code = find_text_similarity(murderer_sample, myrtle_sample)
   code_author[myrtle_text_similarity_code] = myrtle_sample.author

   gregg_text_similarity_code = find_text_similarity(murderer_sample, gregg_sample)
   code_author[gregg_text_similarity_code] = gregg_sample.author

   print("Author's name: {sample} \nThe similarity score to the murder letter is: {s}\n".format(sample = lily_sample.author , s=lily_text_similarity_code))
   print( "Author's name: {sample} \nThe similarity score to the murder letter is: {s}\n".format(sample = myrtle_sample.author ,s=myrtle_text_similarity_code))
   print( "Author's name: {sample} \nThe similarity score to the murder letter is: {s}\n".format(sample = gregg_sample.author ,s=gregg_text_similarity_code))

   code = who_dunnit(lily_text_similarity_code,myrtle_text_similarity_code,gregg_text_similarity_code)

   print("The person who killed Jay Stacksby is {name}".format(name=code_author[code]))
   
# # Who Dunnit?
# 
# In the cell below, print the name of the person who killed Jay Stacksby.
if __name__== "__main__":
  main()
