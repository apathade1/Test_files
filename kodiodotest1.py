# Q2 VOWELS 


def Check_Vow(string, vowels): 

    string = string.casefold()

    count = {}.fromkeys(vowels, 0)


    for character in string:

        if character in count:

            count[character] += 1   

    return count


vowels = 'aeiou'

string = "Hi, My name is Akanksha and Yours ? "

print (Check_Vow(string, vowels))






































































