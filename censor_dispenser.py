# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor(text, word):
    text_censored = text.replace(word, 'CENSORED')
    return text_censored
email_one_censored = censor(email_one, 'learning algorithms')
print(email_one_censored)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


def censor_two(text, censor_list):
    text = text.lower()
    for i in range(len(censor_list)):
        text = text.replace(censor_list[i], 'CENSORED')
    return text
print(censor_two(email_two, proprietary_terms))


    
    
