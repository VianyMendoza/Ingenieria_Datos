def mail_final (mail):
    print(mail[:mail.find('@')] + "@ceu.es" )


print(mail_final(input("¿Cuál es tu mail? ")))


