titles = ['awaken the giant within', 'One Minute Manager',
          'The Seven Habits a Highly Effective People']
authors = ['Anthony robbins', 'spencer johnson', 'stephen covey']
Published = ['AUG/2000', 'MAR/1982', 'JAN/1989']
ISBN = ['0-425-09847-8', '8601417008300', '9780606323185']



def chapter1(number):
    if number == 0:
        return ("A consistence man believe in destiny. We all have dreams. We all want to believe deep down in our souls that we have a special gift, that we can make a difference, that we can touch others in a special way, and that we can make the world a better place."
                "At one time in our lives, we all had a vision for the quality of life that we desire and deserve")
    elif number == 1:
        return ("ONCE there was a bright young man who was looking for an effective manager. He wanted to work for one. He wanted to become one.His search had taken him over many years to the far corners of the world"
                "He had been in small towns and in the capitals of powerful nations.")
    elif number == 2:
        return ("There is no real excellence in all this world which can be be seperated from right living.In more than 25 years of working with people in business, university,and marriage and family settings, I have come in contact with many individuals who have achieved an incredible degree of outward success "
                "but have found themselves struggling with an inner hunger, a deep need for personal congruency and effectiveness and for healthy, growing relationships with other people.")



def display_catalogue():
    print("AVAILABLE BOOKS;")
    print("\n")
    for num in range(0, len(titles)):
        print("Book Title: " + str(titles[num]))
        print("Book Author: " + str(authors[num]))
        print("Book Publish Date: " + str(Published[num]))
        print("ISBN Number: " + str(ISBN[num]))
        print("\n")

    
def titleSearch(search_item):
    for x in range(0, (len(titles))):
        if search_item in titles[x].upper():
            search = True
            break
        else:
            search = False
            
    while search == False:
        print("The book is not avaliable in the library")
        exit()

    for n in range(0, (len(titles))):
        if search_item not in titles[n].upper():
            continue
        print("TITLE: " + str(titles[n]))
        print("AUTHOR: " + str(authors[n]) + " (" + str(ISBN[n]) + ")" + " (" + Published[n] + ")")
        print("CHAPTER1: ")
        print(chapter1(n))
        print("\n")
        if n == len(titles):
            break
            

def authorSearch(search_item):
    for x in range(0, (len(authors))):
        if search_item in authors[x].upper():
            search = True
            break
        else:
            search = False

    while search == False:
        print("The book is not avaliable in the library")
        exit()

    for n in range(0, (len(authors))):
        if search_item not in authors[n].upper():
            continue
        print("TITLE: " + str(titles[n]))
        print("AUTHOR: " + str(authors[n]) + " (" + str(ISBN[n]) + ")" + " (" + Published[n] + ")")
        print("PROJECT ABSTRACT: ")
        print(chapter1(n))
        print("\n")
        if n == len(titles):
            break



def PublishedSearch(search_item):
    for x in range(0, (len(Published))):
        if search_item in Published[x].upper():
            search = True
            break
        else:
            search = False

    while search == False:
        print("The book is not avaliable in the library")
        exit()

    for n in range(0, (len(Published))):
        if search_item not in Published[n].upper():
            continue
        print("PROJECT TITLE: " + str(titles[n]))
        print("AUTHOR: " + str(authors[n]) + " (" + str(ISBN[n]) + ")" + " (" + Published[n] + ")")
        print("PROJECT ABSTRACT: ")
        print(chapter1(n))
        print("\n")
        if n == len(titles):
            break

            
print("WHAT DO YOU WANT TO DO?")
print("1: SEARCH FOR BOOK!")
print("2: DISPLAY BOOK CATALOGUE")

action_input = int(input("Enter what you want to do here: "))

if action_input == 1:
    print("1: SEARCH THE TITLE OF THE BOOK")
    print("2: SEARCH THE NAME OT THE AUTHOR OF THE BOOK")
    print("3: SEARCH THE YEAR THE BOOK WAS PUBLISHED")
    search_method = int(input("Enter the method you want to search here: "))
    
while action_input not in range(1, 3):
    print("Invalid action! Enter either 1 or 2!")
    search_method = int(input("Enter the action again (between 1 and 2): "))
    if search_method in range(1, 3):
        break

if action_input == 1:
    seach_query = input("Enter what you want to search here: ")

if action_input == 1:
    if search_method == 1:
        print("\n")
        print("SEARCH RESULTS ARE GIVEN BELOW:")
        print("==============================")
        print("\n")
        titleSearch(seach_query.upper())

    if search_method == 2:
        print("\n")
        print("SEARCH RESULTS ARE GIVEN BELOW:")
        print("==============================")
        print("\n")
        authorSearch(seach_query.upper())

    if search_method == 3:
        print("\n")
        print("SEARCH RESULTS ARE GIVEN BELOW:")
        print("==============================")
        print("\n")
        PublishedSearch(seach_query.upper())

if action_input == 2:
    display_catalogue()