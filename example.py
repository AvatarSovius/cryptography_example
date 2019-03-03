keys_secret = {

    "A":"V",
    "D":"X",
    "H":"B",
    "I":"G",
    "K":"J",
    "M":"C",
    "O":"Q",
    "R":"L",
    "S":"N",
    "U":"E",
    "W":"F",
    "Y":"P",
    "Z":"T",
    "V":"A",
    "X":"D",
    "B":"H",
    "G":"I",
    "J":"K",
    "C":"M",
    "Q":"O",
    "L":"R",
    "N":"S",
    "E":"U",
    "F":"W",
    "P":"Y",
    "T":"Z",
    " ": " "

}


input_text = str(input())
output_text = []

for i in input_text.upper():
    output_text.append(keys_secret[i])

print(input_text)
print(len(input_text) * "=")

for i in output_text:
    print(i,end = '')
