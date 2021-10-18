"""DBM"""
def my_top():
    """DBM"""
    name1 = input()
    name2 = input()
    name3 = input()
    name4 = input()
    skill1 = input().replace("Clodette", "healing")
    skill2 = input().replace("Jake", "silent")
    skill3 = input().replace("Megg", "juke")
    skill4 = input().replace("Dwight", "teamwork")
    skill1 = skill1.replace("Jake", "silent").replace("Megg", "juke")\
    .replace("Dwight", "teamwork")
    skill2 = skill2.replace("Clodette", "healing").replace("Megg", "juke")\
    .replace("Dwight", "teamwork")
    skill3 = skill3.replace("Clodette", "healing").replace("Jake", "silent")\
    .replace("Dwight", "teamwork")
    skill4 = skill4.replace("Clodette", "healing").replace("Jake", "silent")\
    .replace("Megg", "juke")
    print("I'm %s. I'm playing %s."%(name1, skill1))
    print("I'm %s. I'm playing %s."%(name2, skill2))
    print("I'm %s. I'm playing %s."%(name3, skill3))
    print("I'm %s. I'm playing %s."%(name4, skill4))
my_top()
