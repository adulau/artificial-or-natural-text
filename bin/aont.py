#
# Test script to evaluate a full dataset of Pastebin-like items
# and calculate the various potential ranking.

import textstat
import os
import json
import signal
import sys


content = sys.stdin.read() 
lexicon = textstat.lexicon_count(content, removepunct=True)
syllabe = textstat.syllable_count(content, lang='en_US')
sentence = textstat.sentence_count(content)
# consensus = textstat.text_standard(content, float_output=False)
# print ("sentence={}, syllabe={}, lexicon={}, flesch_reading_score={},{}".format(sentence, syllabe, lexicon, textstat.flesch_reading_ease(content), currentfile))
analysis = {}
analysis['sentence'] = sentence
analysis['syllabe'] = syllabe
analysis['lexicon'] = lexicon
analysis['flesch_reading_ease'] = textstat.flesch_reading_ease(content)
analysis['filename'] = 'stdin' 
analysis['length'] = len(content)
analysis['extract'] = content[:100]

#rank = (analysis['flesch_reading_ease']+analysis['flesch_reading_ease']+analysis['lexicon'])*analysis['sentence']
rank = analysis['flesch_reading_ease']
if analysis['flesch_reading_ease'] >= 0 and analysis['flesch_reading_ease'] <= 900:
    print(json.dumps(analysis))
    #print("rank:{}".format(rank))
else:
    #print("missed: {}".format(content[:100]))
    print("missed rank:{}".format(rank))
# print ("{}, {}, {}, {}".format(sentence, syllabe, lexicon, textstat.flesch_reading_ease(content), currentfile))
