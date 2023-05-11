import time

option_1 = "Python"
option_2 = "Javascript"

user_id = list(range(1,21))
number_of_voters = len(user_id)

def Voting_system ():
  option_1_votes = 0
  option_2_votes = 0

  while number_of_voters <= 20:
     if user_id == []:

        if option_1_votes > option_2_votes:
           percentage = (option_1_votes / number_of_voters) * 100
           print("We will be offering free " + option_1 + f" lectures as {percentage:.2f} % of voters chose to learn " + option_1 + ".")
           break

        elif option_2_votes > option_1_votes:
           percentage = (option_2_votes / number_of_voters) * 100
           print("We will be offering free " + option_2 + f" lectures as {percentage:.2f} % of voters chose to learn " + option_2 + ".")
           break

        else:
           print ("We have equal votes for " + option_1 + " and " + option_2 + ". Consequently,the poll will be reopened again soon. Thank you for voting")
           break

     else:

         try:
            id = int(input("Enter your user id: "))
            if id in user_id:
               user_id.remove(id)
               vote = int(input ("To select " + option_1 + " , enter 1\nTo select " + option_2 + " , enter 2\n"))
               if vote == 1:
                  option_1_votes += 1
                  print ("Thank you. Your vote has been recorded.")
                  time.sleep(1)
                  print (option_1 + " has ", option_1_votes , "votes.")
                  print(option_2 + " has ", option_2_votes , "votes.")

               elif vote == 2:
                  option_2_votes += 1
                  print ("Thank you. Your vote has been recorded.")
                  time.sleep(1)
                  print(option_1 + " has ", option_1_votes, "votes.")
                  print(option_2 + " has ", option_2_votes, "votes.")

               else:
                  user_id.append(id)
                  print ("Invalid selection.")

            else :
                  print("You are not an eligible voter or you already cast your vote.")

         except ValueError:
            print("ID can only be digits")

Voting_system()
    