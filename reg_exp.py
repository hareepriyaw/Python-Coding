import re

text_to_search = "I am a jeeva who is one among the 84 lakhs of jeevas. my phone number is 818-918-1482 my husband's phone number is 516-849-0271. my email ID is jahnavi.abhi@gmail.com my husband's email-ID is balaji.abhi@gmail.com. Our address is 8661 Aldershot drive, Henrico, Virginia 23294"

pat = re.compile(r"[a-n][-][A-J]")
mat=pat.finditer(text_to_search)
for m in mat:
    print(m)
   