class subjects():
      
    def __init__(self, branch, staff):
        self.branch=branch
        self.staff=staff
        
    
    def branch_category(self):
        self.branch="biotechnology"
        self.staff="vijaya"
        self.marks=70

class sub_subj(subjects):
    
    def another_branch(self):
        self.branch="microbiology"
        self.staff="vijayalakshmi"
        self.marks=80
    
st2=subjects("chemistry","Gouse")
st2.marks=90
print("this is the first instance:", "\n",st2.branch,"\n",st2.staff,"\n",st2.marks)

st2.branch_category()
print("This is second instance:","\n",st2.branch,"\n",st2.staff,"\n",st2.marks)

st3=sub_subj("botany","sasikala")
print("This is the sub class instance:","\n", st3.branch,"\n", st3.staff)

st3.another_branch()
print("This is the sub class method:","\n", st3.branch,"\n", st3.staff,"\n", st3.marks)

st3.branch_category()
print("This is the sub class method:","\n", st3.branch,"\n", st3.staff,"\n", st3.marks)




    
