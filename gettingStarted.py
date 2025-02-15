import hashlib


def welcome_assignment_answers(question):
    question = question.lower()
    if question == "in slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a ta?":
        answer = "pcap"
    elif question == "are encoding and encryption the same? - yes/no":
        answer = "No"
    elif question == "is it possible to decrypt a message without a key? - yes/no":
        answer = "No"
    elif question == "is it possible to decode a message without a key? - yes/no":
        answer = "Yes"
    elif question == "is a hashed message supposed to be un-hashed? - yes/no":
        answer = "No"
    elif question == "what is the sha256 hashing value of your nyu email and use the answer in your code - ":
        nyu_email = "it2284@nyu.edu"
        answer = hashlib.sha256(nyu_email.encode()).hexdigest()
    elif question == "is md5 a secured hashing algorithm? - yes/no":
        answer = "No"
    elif question == "what layer of the tcp/ip model does the protocol dns belong to? - the answer should be an integer number":
        answer = 5
    elif question == "what layer of the tcp/ip model does the protocol icmp belong to? - the answer should be an integer number":
        answer = 3
    else:  # Default case
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"

    return answer


# Complete all the questions.


if __name__ == "__main__":
    debug_question = "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    print(welcome_assignment_answers(debug_question))

#Questions:
#1"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#2"Are encoding and encryption the same? - Yes/No":
#3"Is it possible to decrypt a message without a key? - Yes/No":
#4"Is it possible to decode a message without a key? - Yes/No":
#5"Is a hashed message supposed to be un-hashed? - Yes/No":
#6"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#7"Is MD5 a secured hashing algorithm? - Yes/No":
#8"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#9"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
