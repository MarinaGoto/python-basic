#Encryption and Decryption



encryption_key = (('a','m'), ('b','h'), ('c','t'), ('d','f'), ('e','g'), ('f','k'), ('g','b'), ('h','p'), ('i','j'), ('j','w'), ('k','e'),('l','r'), ('m','q'), ('n','s'), ('o','l'), ('p','n'), ('q','i'), ('r','u'), ('s','o'), ('t','x'), ('u','z'), ('v','y'), ('w','v'), ('x','d'), ('y','c'), ('z','a'))

choice = input('Encryption (e) or Decryption(d): ')

message = input('Enter a message:  ')  
#output = []
output = ''

difference = ord('a')-ord('A')


for ch in message:
    print(ch)
    for pair in encryption_key:
        if choice == 'e':
            if('a' <= ch and ch <= 'z') and ch== pair[0]:
                 #output.append(pair[1])
                output = output + pair[1]
#chr change from incodding to character and back                     
            elif ('A' <= ch and ch <= 'Z') and (chr(ord(ch) + difference) == pair[0]):
               # output.append(chr(ord(pair[1]) - difference))        
                output = output + (chr(ord(pair[1]) - difference))
        elif choice == 'd':
            if('a' <= ch and ch <= 'z') and ch== pair[1]:
                # output.append(pair[0]) 
                  output = output + pair[0]   
            elif ('A' <= ch and ch <= 'Z') and (chr(ord(ch) + difference) == pair[1]):
                # output.append(chr(ord(pair[0]) - difference)) 
                 output = output + (chr(ord(pair[0]) - difference))
print(output)




    
    
