text = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
fd = open("Python/Files/correos.txt", "w", encoding="utf-8")
emails = []
for x in text:
    if x.startswith("From:"):
        x = x[6:]
        emails.append(x)

sent = set(emails)
sent = list(sent)

for i in range(len(sent)-1, 0, -1):
    x = sent[i]
    print("Enviado OK\t", x.rstrip())

fd.writelines(sent)
text.close()