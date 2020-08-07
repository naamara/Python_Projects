#Online Admission Application System, the applicant's details is taken below

print('=' * 53)
print('Online Admission Application System'.center(50))
print('=' * 53)

print('\n\tThis program was created to ease the admission process done as a requirement into the tertiary institution without prejudice. Please provide the following valid details accordingly.')

print()
print('=' * 53)
print('Personal Details'.center(50))
print('=' * 53)

name_of_applicant = input('\nFull Name (Surname first): ')
DOB_year = input('Year of Birth: ')
DOB_dayandmonth = input('Day and Month: ')
address = input('Home Address: ')
phone_number = input('Phone Number: ')
email = input('Email Address: ')
gender = input('Gender: ')

print()
print('=' * 53)
print('Application Details'.center(50))
print('=' * 53)

jamb_registration_number = input('\nJamb Registration Number: ')
jamb_score = int(input('UTME Score: '))

cumulative_jamb = jamb_score/8 # aggregate jamb score is calculated
course_of_study_first_choice = input('First Choice Course of Study: ')
second_choice_course_of_study = input('Second Choice Course of Study: ')
# O/level details is provided
print('\nPROVIDE O/LEVEL DETAILS BELOW.') 
exam_type = input('\nExam Type (WAEC, NECO, NABTEB etc...): ')
exam_number = input('Exam Registration Number: ')
year_of_exam = input('Year of Examination: ')
 # the point for each grade is declared
olevel_grades = {'A' : 10, 'B' : 8, 'C' : 6, 'D' : 4, 'E' : 2, 'F' : 0}


print('\nPROVIDE O/LEVEL GRADES IN UPPER CASE LETTERS ONLY.')
mathematics = input('\nMathematics: ')
english = input('English: ')
biology = input('Biology: ')
chemistry = input('Chemistry: ')
physics = input('Physics: ')
# cumulative point of O/level grades is calculated
cumulative_olevel_grades = olevel_grades[mathematics] + olevel_grades[english] + olevel_grades[biology] + olevel_grades[chemistry] + olevel_grades[physics]


if mathematics in olevel_grades:
	if biology in olevel_grades:
		if chemistry in olevel_grades:
			if physics in olevel_grades:
				if english in olevel_grades:
					total_cumulative = cumulative_jamb + cumulative_olevel_grades
					print(f'\nTotal Aggregate Score (Jamb and O/level) is: {total_cumulative}')
	
# the total aggregate of both Jamb and O/level is calculated over 100									

#the cut off point for different course of study upon which a candidate will be offered admission based on his aggregate point

course = { 70 : 'MBBS', 65 : 'Pharmacy', 60 : 'Nursing', 50 : 'Biochemistry'}

# the condition upon which a candidate is going to be offered admission
if total_cumulative >69<100:
	print(f'\nCongratulations! {name_of_applicant} with the jamb registration number {jamb_registration_number} have been given admission to study', course[70])
	
elif total_cumulative >64<70:
	print(f'\nCongratulations! {name_of_applicant} with the jamb registration number {jamb_registration_number} have been given admission to study', course[65])

elif total_cumulative >59<65:
	print(f'\nCongratulations! {name_of_applicant} with the jamb registration number {jamb_registration_number} have been given admission to study', course[60])

elif total_cumulative >49<60:
	print(f'\nCongratulations! {name_of_applicant} with the jamb registration number {jamb_registration_number} have been given admission to study', course[50])

else:
	print('\nSorry, no admission is given because of low aggregate score.')
