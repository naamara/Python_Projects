#THIS PROJECT COUNTS THE NUMBER OF WORDS/CHARACTERS IN A TEXT AND CALCULATES THE TRANSLATION PRICE ACCORDINGLY

# guide the user on how to input file path correctly
print("kindly input your file path in this format: " + "\n" + "\n" +
          'C:\\Users\\user\\Desktop\\filename.extension')

print("\n" + "the above format was just an example")

while True:
    try:
        count = 0 


# open file and read
        with open(input(),encoding='utf8', newline='\n') as filename:
                   

# splits each line into words
                words = filename.read().split()

    
    
# counts each word in individual lines
                count = count + len(words);
        print ("\n" + "Number of words present in your file is  " + str(count))


#  a translator charges average of 0.04 USD per word for translation
        price = 0.04 * int(count)
        print("\n" + f"to translate your {count} words, its gonna cost you   {price} dollars")
        
        break
        
    except FileNotFoundError:
        print("\n kindly input the correct file path \n")
    
    except UnicodeDecodeError:
        print("\n The file should have a .txt entension \n")
    
    except:
        break
# end of code