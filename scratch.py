from brave import brave_req, summarizer
from groq_completion import groq_completion

a = summarizer("Introibo ad altare Dei")
print(a)
# print()
# print('---------------------------------')
# print('---------------------------------')
# print()

# c = ("how many copies of Ulysses have been sold?")
# print(c)

# ulys_txt = ''' Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed. A yellow dressinggown, ungirdled, was sustained gently behind him on the mild morning air. He held the bowl aloft and intoned:

# —Introibo ad altare Dei.

# Halted, he peered down the dark winding stairs and called out coarsely:

# —Come up, Kinch! Come up, you fearful jesuit!

# Solemnly he came forward and mounted the round gunrest. He faced about and blessed gravely thrice the tower, the surrounding land and the awaking mountains. Then, catching sight of Stephen Dedalus, he bent towards him and made rapid crosses in the air, gurgling in his throat and shaking his head. Stephen Dedalus, displeased and sleepy, leaned his arms on the top of the staircase and looked coldly at the shaking gurgling face that blessed him, equine in its length, and at the light untonsured hair, grained and hued like pale oak.

# Buck Mulligan peeped an instant under the mirror and then covered the bowl smartly.

# —Back to barracks! he said sternly.

# He added in a preacher’s tone:

# —For this, O dearly beloved, is the genuine Christine: body and soul and blood and ouns. Slow music, please. Shut your eyes, gents. One moment. A little trouble about those white corpuscles. Silence, all. '''

# user_questino = "What does Introibo ad altare Dei mean?"
# b = groq_completion(user_questino, ulys_txt)
# print(b)