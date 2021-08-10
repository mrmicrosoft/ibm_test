#This program mectracts words from a piece of text into a set data type 
#and removes profany words obtained from another set

input_text = """
We long for things that harm us and run from the things that grow and heal us
We think good is bad and bad is good fool
Just take my hand, lead, dance with me ... and i will simply fuck the blueness of the 
water, the nasty waves rolling free ... where the earth beneath my dirty feet and stars make 
my heart stupid again ... in long and priceless moments of shared solitude ...
"""
profany_words = {"stupid", "nasty", "fuck", "fool", "bad", "dirty"}

raw_words = input_text.split()
words = set()

for word in raw_words:
    if word != "...":
        words.add(word)

clean_words = words - profany_words
print("Clean Words:\n{}".format(clean_words))

