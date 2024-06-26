from brave import brave_req, summarizer, concat_brave_search_results
from groq_completion import groq_completion
from groq_prompts import answer_question_prompt, entry_prompt

ulys_txt = ''' Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed. A yellow dressinggown, ungirdled, was sustained gently behind him on the mild morning air. He held the bowl aloft and intoned:
—Introibo ad altare Dei.
Halted, he peered down the dark winding stairs and called out coarsely:
—Come up, Kinch! Come up, you fearful jesuit!
Solemnly he came forward and mounted the round gunrest. He faced about and blessed gravely thrice the tower, the surrounding land and the awaking mountains. Then, catching sight of Stephen Dedalus, he bent towards him and made rapid crosses in the air, gurgling in his throat and shaking his head. Stephen Dedalus, displeased and sleepy, leaned his arms on the top of the staircase and looked coldly at the shaking gurgling face that blessed him, equine in its length, and at the light untonsured hair, grained and hued like pale oak.
Buck Mulligan peeped an instant under the mirror and then covered the bowl smartly.
—Back to barracks! he said sternly.
He added in a preacher’s tone:
—For this, O dearly beloved, is the genuine Christine: body and soul and blood and ouns. Slow music, please. Shut your eyes, gents. One moment. A little trouble about those white corpuscles. Silence, all. '''

shel_silverstein = '''MAGIC
Sandra's seen a leprechaun,
Eddie touched a troll,
Laurie danced with witches once,
Charlie found some goblins' gold.
Donald heard a mermaid sing,
Susy spied an elf.
But all the magic I have known
I've had to make myself'''

# user_questino = "What does Introibo ad altare Dei mean?"
# b = groq_completion(user_questino, ulys_txt)
# print(b)

init_prompt = entry_prompt("what books has shel silverstein written in the past year?", shel_silverstein)
grr = groq_completion(init_prompt)



p = brave_req("what books has shel silverstein written in the past year?")
# print(p)

ss = concat_brave_search_results(p)
# print(ss)

thep = answer_question_prompt(ss, "what books has shel silverstein written in the past year?")

groq_res = groq_completion(thep)
print(groq_res)
