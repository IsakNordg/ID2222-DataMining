# Purpose: Split the SMSSpamCollection.txt file into individual files for each line

filename = "Data4\sms+spam+collection\SMSSpamCollection.txt"

with open(filename, "r", encoding="utf8") as f:
    content = f.readlines()
    for i, line in enumerate(content):
        with open("Data4\sms+spam+collection\Split\SMS" + str(i) + ".txt", "w", encoding="utf8") as f:
            
            f.write(line.replace('\t', ' '))