import random

# Sample Questions

maths_question = [
    "A woman bought a grinder for N60,000. \
    She sold it at a loss of 15%. How much did she sell it?",
    "Express the product of 0.00043 and 2000 in standard form.",
    "A man donates 10% of his monthly net earnings to his church. \
    If it amounts to N4,500, what is his net monthly income?",
    "If log7.5 = 0.8751, evaluate 2 log75 + log750",
    "Solve for x in 8x-2 = 2/25",
    "Factorize 2y2 - 15xy + 18x2",
    "y varies directly as w2. When y = 8, w = 2. Find y when w = 3",
    "The 4th term of an A.P. is 13 while the 10th term is 31. Find the 24th term.",
    "How many sides has a regular polygon whose interior angle is 135",
    "If P = {1,2,3,4,5} and P Q = {1,2,3,4,5,6,7}, list the elements in Q"
]

biology_question = [
    "Which of the following characterizes a mature plant cell?",
    "Which of the following is NOT a function of the nucleus of a cell?",
    "The dominant phase in the life cycle of a fern is the?",
    "Parental care is exhibited by",
    "Which of the following is true of the transverse section of a dicot system?",
    "Which of the following is lacking in the diet of a person with kwashiorkor?",
    "The mode of nutrition of sun dew and bladder wort can be described as",
    "When the mixture of a food substance and Benedict's solution was warmed, the solution changed from blue "
    "to black-red. This indicates the presence of",
    "The primary structure responsible for pumping blood for circulation through the mammalian circulatory systems is the",
    "Circulation of blood to all parts of the body except the lungs is through"
]

chemistry_question = [
    "Which of the following statements is NOT correct?",
    "Zinc Oxide is a",
    "When sodium chloride and metallic sodium are each dissolved in water",
    "The periodic classification of elements is an arrangement of the elements in order of their",
    "In the reaction between sodium hydroxide and sulphuric acid solutions, what volume of 0.5 molar sodium hydroxide would exactly neutralise 10cm3 of 1.25 molar sulphuric acid",
    "A small quantity of solid ammonium chloride (NH4Cl) was heated gently in a test tube, the solid gradually disappears to produce two gases. Later, a white cloudy deposit was observed on the cooler part of the test tube. The ammonium chloride is said to have undergone",
    " Elements P, Q, R, S have 6, 11, 15, 17 electrons respectively, therefore,",
    "An element X forms the following compounds with chlorine; XCl4, XCl3, XCl2. This illustrates the",
    "The oxidation state of chlorine in potassium chlorate is",
    "When air which contains the gases Oxygen, nitrogen, carbondioxide, water vapour and the rare gases, is passed through alkaline pyrogallol and then over quicklime, the only gases left are;",
]

english_question = [
    "Choose the option that best conveys the meaning of the underlined portion in the following sentence\n In the match against the uplanders team, the sub mariners turned out to be the  dark horse,",
    "Choose the option that best conveys the meaning of the underlined portion in the following sentence\n Only the small fry get punished for such social misdemeanors",
    "Choose the option that best conveys the meaning of the underlined portion in the following sentence\n He spoke with his heart in his mouth",
    "Choose the option that best conveys the meaning of the underlined portion in the following sentence\n From the ways my friend talks, you can see he is such a bore",
    "If my father had not arrived, I would have starved. This sentence means",
    "Choose the option that best conveys the meaning of the underlined portion in the following sentence\nThe two sprinters were running neck and neck",
    "Complete each of the following sentences by choosing the option that most suitably fills the space\nWhen the beggar was tired he ..... down by the roadside",
    "Complete each of the following sentences by choosing the option that most suitably fills the space;\nHe did not like .... leaving the class early",
    "Complete each of the following sentences by choosing the option that most suitably fills the space\nBefore the operation, the dentist found that his patient's teeth....",
    "Complete each of the following sentences by choosing the option that most suitably fills the space\nThe boy was born before his parents actually got married and so the court has declared him ...."
]

maths_answer_choices = [
    ["53000", "52000", "51000", "50000"],
    ["8.6 * 10-3", "8.3 * 10-2", "8.6 * 10-1", "8.6 * 10"],
    ["40500", "45000", "52500", "62000"],
    ["6.6252", "6.6253", "66.252", "66.253"],
    ["4", "6", "8", "10"],
    ["(2y - 3x) (y + 6x)", "(2y - 3x) (y - 6x)", "(2y + 3x) (y - 6x)", "(3y + 2x) (y - 6x)"],
    ["18", "12", "9", "6"],
    ["89", "75", "73", "69"],
    ["12", "10", "9", "8"],
    ["{6}", "{7}", "{6,7}", "{5,6}"]
]

biology_answer_choices = [
    ["the cytoplasm fills up the entire cell space".title(), "the nucleus is pushed to the centre of the cell".title(),
     "the cell wall is made up of cellulose".title(), "the nucleus is small and irregular in shape".title()],
    [
        "it controls the life processes of the cell".title(),
        "it translates genetic information for the manufacture of proteins".title(),
        "it stores and carries hereditary information".title(), "it is reservoir of energy for the cell".title()
    ],
    ["gametophyte".title(), "prothallus".title(), "sporophyte".title(), "antheridium".title()],
    ["toads".title(), "snails".title(), "earthworms".title(), "birds".title()],
    ["the epidermis is completely encircled by the cortex".title(), "the xylem is more interiorly located than the phloem".title(),
     "the cambium lies between the cortex and the vascular bundles".title(),
     "the vascular bundles are randomly scattered within the cortex".title()],
    ["vitamins".title(), "proteins".title(), "carbohydrate".title(), "vegetables".title()],
    ["autotrophic".title(), "saprophytic".title(), "holozoic".title(), "chemosynthetic".title()],
    ["reducing sugar".title(), "fatty acid".title(), "sucrose".title(), "amino acid".title()],
    ["veins".title(), "right auricle".title(), "arteries".title(), "left ventricle".title()],
    ["the pulmonary artery".title(), "systemic circulation".title(), "the lymphatic system".title(), "pulmonary circulation".title()]
]

chemistry_answer_choices = [
    ["The average kinetic energy of a gas is directly proportional to its temperature" ,"At constant tempearture, the volume of a gas increases as the pressure increases", "The pressure of a gas is inversely proportional to its volume", "The temperature of a gas is directly proportional to its volume"],
    ["Basic Oxide", "Acidic Oxide", "Amphoteric Oxide", "Neutral Oxide"],
    ["both processes are exothermic", "both processes are endothermic", "the dissolution of metallic sodium is endothermic", "the dissolution of metallic sodium is exothermic"],
    ["Atomic Weights", "Isotopic Weights", "Molecular Weights", "Atomic Numbers"],
    ["10cm3", "20cm3", "25cm3", "50cm3"],
    ["P will form an electrovalent bond with R", "Q will form a covalent bond with S", " R will form an electrovalent bond with S", "Q will form an electrovalent bond with S"],
    ["distillation", "sublimation", "precipitation", "evaporation"],
    ["law of multiple proportions", "law of chemical proportions", "law of simple proportions", " law of conservation of mass"],
    ["+1", "+2", "+3", "+5"],
    ["nitrogen and carbondioxide", "the rare gases", "nitrogen and oxygen", "nitrogen and the rare gases"]
]

english_answer_choices = [
    ["played most brilliantly", "played below their usual form", "won unexpectedly", "lost as expected"],
    ["small boys", "unimportant people", "frightened people", "frivolous people"],
    ["with such unusual cowardice", "with a lot of confusion in his speech", "without being able to make up his mind", "with fright and agitation"],
    ["rude", "brilliant", "uninteresting", "overbearing"],
    ["My father did arrive and I didn't starve", "I had to starve because my father didn't come", "my father didn't arrive and I didn't starve", "I should have starved but I didn't"],    ["exact level", "very slowly", "very fast", "with their necks together"],
    ["lied", "laid", "layed", "lay"],
    ["we","us", "our", "ourselves"],
    ["have long decayed", "have long been decayed", "have long being decayed", "had long decayed"],
    ["illegal", "illegitimate", "illicit", "unlawful"],
]

user_maths_answer = []

user_biology_answer = []

user_chemistry_answer = []

user_english_answer = []

user_answer = []

answer = []


correct_answers = [
    ["C", "C", "B", "B", "D", "B", "A", "C", "D", "C"],
    ["C", "D", "C", "D", "B", "B", "C", "A", "C", "B"],
    ["B", "C", "D", "D", "D", "D", "B", "A", "D", "D"],
    ["C", "B", "D", "C", "D", "A", "B", "B", "D", "B"]
]

final_answer = []

randomness = []

ques = 0

print("Welcome to Quiz Night")

# While loop to generate question randomly
while len(randomness) <= 19:
    x = random.randint(0, 9)
    randomness.append(x)
    if x in randomness:
        continue
    else:
        randomness.append(x)

# While loop to ensure question generated in total is 20
while ques in range(0, 19):

    # loop to randomly print 5 maths questions
    if ques in range(0, 5):
        while ques <= 5:
            print(maths_question[randomness[ques]])
            print("A.", maths_answer_choices[randomness[ques]][0])
            print("B.", maths_answer_choices[randomness[ques]][1])
            print("C.", maths_answer_choices[randomness[ques]][2])
            print("D.", maths_answer_choices[randomness[ques]][3])
            x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))

            # loop to ensure user input is between 0 and 3
            if x == "A" or x == "B" or x == "C" or x == "D":
                user_maths_answer.append(x)

            else:
                while x != "A" or x != "B" or x != "C" or x != "D":
                    print("please input the proper answer")
                 
                    x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))
                    if x == "A" or x == "B" or x == "C" or x =="D":
                        user_maths_answer.append(x)
                        break
            ques += 1
            if ques == 5:
                break
    # loop to randomly print 5 biology questions
    elif ques in range(5, 10):
        while ques <= 10:
            print(biology_question[randomness[ques]])
            print("A.", biology_answer_choices[randomness[ques]][0])
            print("B.", biology_answer_choices[randomness[ques]][1])
            print("C.", biology_answer_choices[randomness[ques]][2])
            print("D.", biology_answer_choices[randomness[ques]][3])
       
            x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))

            # loop to ensure user input is between 0 and 3
            if x == "A" or x == "B" or x == "C" or x =="D":
                user_biology_answer.append(x)

            else:
                while x != "A" or x != "B" or x != "C" or x != "D":
                    print("please input the proper answer")
       
                    x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))
                    if x == "A" or x == "B" or x == "C" or x =="D":
                        user_biology_answer.append(x)
                        break
            ques += 1
            if ques == 10:
                break
    # loop to randomly print 5 chemistry questions
    elif ques in range(10, 15):
        while ques <= 15:
            print(chemistry_question[randomness[ques]])
            print("A.", chemistry_answer_choices[randomness[ques]][0])
            print("B.", chemistry_answer_choices[randomness[ques]][1])
            print("C.",chemistry_answer_choices[randomness[ques]][2])
            print("D.",chemistry_answer_choices[randomness[ques]][3])
            x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))

            # loop to ensure user input is between 0 and 3
            if x == "A" or x == "B" or x == "C" or x =="D":
                user_chemistry_answer.append(x)

            else:
                while x != "A" or x != "B" or x != "C" or x != "D":
                    print("please input the proper answer")
                    
                    x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))
                    if x == "A" or x == "B" or x == "C" or x =="D":
                        user_chemistry_answer.append(x)
                        break

            ques += 1
            if ques == 15:
                break
    # loop to randomly print 5 English questions
    elif ques in range(15, 20):
        while ques <= 20:
            print(english_question[randomness[ques]])
            print("A.", english_answer_choices[randomness[ques]][0])
            print("B.", english_answer_choices[randomness[ques]][1])
            print("C.", english_answer_choices[randomness[ques]][2])
            print("D.", english_answer_choices[randomness[ques]][3])
            x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))

            # loop to ensure user input is between 0 and 3
            if x == "A" or x == "B" or x == "C" or x =="D":
                user_english_answer.append(x)

            else:
                while x != "A" or x != "B" or x != "C" or x != "D":
                    print("please input the proper answer")
                   
                    x = str.upper(input("Enter an option between A,  B,  C  or  D\n"))
                    if x == "A" or x == "B" or x == "C" or x =="D":
                        user_english_answer.append(x)
                        break

            ques += 1
            if ques == 20:
                break

user_answer.append(user_maths_answer)
user_answer.append(user_biology_answer)
user_answer.append(user_chemistry_answer)
user_answer.append(user_english_answer)

for ans in user_answer:
    for a in ans:
        answer.append(a)

for answers in correct_answers:
    for ans in answers:
        final_answer.append(ans)
        

x = 0
score = 0

#loop to check if the user input equals answer
for i in randomness:
    if answer[x] == final_answer[i]:
        score += 5
    x += 1

else:
    pass


if score >= 80:
    print(f"You answered {int(score/5)} questions correctly.\nYou scored {score} /100\nJob Well Done")

elif 40 <= score < 80:
    print(f"You answered {int(score/5)} questions correctly.\nYou scored {score} /100\nYou can do better")

else:
    print(f"You answered {int(score/5)} questions correctly.\nYou scored {score} /100")