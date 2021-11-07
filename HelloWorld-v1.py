#!python3.9
#coding: UTF-8

## Hello_World.py ##
msg = "Bonjour Monde"
print("-01- " +msg)
print("-02- " +str(len(msg)))
print("-03- " +msg[2])
print("-04- " +msg[3:6])
print("-05- " +msg.upper())
print("-06- " +str(msg.count("o")))
print("-07- " +str(msg.find("u")))
print("-08- " +str(msg.find("z")))
msg1 = "hello"
msg2 = "world"
msg3 = "-09- {} {} coucou!".format(msg1 , msg2)
print(msg3)
msg4 = f"-10- {msg1} {msg2.upper()} coucou !"
print(msg4)
print("-----")
print(help(str.lower))
print("-----")