name = input()
phone = input()
email = input()
vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
with open("contact.vcf", "w") as file:
    file.write(vcard)