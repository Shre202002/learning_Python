#If the Given string contain paricular keyword then the String would considered as a span SPRING 

p1= " Click This "
p2= " Get Money"
p3= " Buy now"
p4= " payment Now"

message = input(" Enter Your Message: ")
 
if((p1 in message) or(p2 in message) or(p3 in message) or(p4 in message) ):
    print(" This message is Span")
else:
    print("NO This is not a span message")