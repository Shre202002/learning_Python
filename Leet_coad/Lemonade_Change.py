# # At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# # Note that you do not have any change in hand at first.

# # Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

# # Example 1:

# # Input: bills = [5,5,5,10,20]
# # Output: true
# # Explanation: 
# # From the first 3 customers, we collect three $5 bills in order.
# # From the fourth customer, we collect a $10 bill and give back a $5.
# # From the fifth customer, we give a $10 bill and a $5 bill.
# # Since all customers got correct change, we output true.
# # Example 2:

# # Input: bills = [5,5,10,10,20]
# # Output: false
# # Explanation: 
# # From the first two customers in order, we collect two $5 bills.
# # For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# # For the last customer, we can not give the change of $15 back because we only have two $10 bills.
# # Since not every customer received the correct change, the answer is false.


# cus = int(input("Enter the number of Coster "))
# cash = []

# def changes(self, cus[]):

#     for i in range(len(cus)):

#          if(cus[i] == 5):
#             f += 1
    
#          elif(cus[1] == 10):
             
#             if(f == 0): 
#               return False
#             else:
#                 f -=1 
        




# for i in range(cus):
#     c = int(input("Enter the amount payed: "))
#     cash.append(c)





def create_largest_number(number_list):
    
   number_list.sort(reversed = True)
   sum = " "
   for e in number_list:
      sum = sum + str(e)

   return int(sum) 
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number= create_largest_number(number_list)
print(largest_number) 