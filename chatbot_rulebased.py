import random
import re
#define a class for having the functions 
class Supportbot:
    negative_res=("no","nope","not a chance","may not","may","sorry")
    exit_res=("bye","Thank you","Exit","Pause")
    def __init__(self):
        self.support_res= {
        'ask_product': r'.*\s*product.*',
        'technical_support' : r'.*technical.*support.*',
        'return_policy' : r'.*\s*return policy.*',
        'general_query':r'.*help.*'
      }

    def greet(self):
        self.name=input("Hi welcome to our customer support.what's your name?\n")
        help=input(f"hi {self.name}.how can i assist you today?\n")
        if help in self.negative_res:
            print("Thank you! Have a great Day")
            return
        self.chat()
    def make_exit(self,reply):
        for res in self.exit_res:
            if res in reply:
                print("Thanks for reaching out!Have a great day")
                return True
            return False
    
    def chat(self):
        reply=input("Please tell me your query:").lower()
        while not self.make_exit(reply):
            reply=input(self.match_reply(reply))



    def match_reply(self,reply):
        for intent,regex_pat in self.support_res.items():
            found = re.search(regex_pat,reply)
            if found and intent =="ask_product":
                return self.ask_product()
            elif found and intent =="technical_support":
                return self.technical_support()
            elif found and intent=="return_policy":
                return self.return_policy()
            elif found and intent =="general_query":
                return self.general_query()
        return self.no_match_intent()


    def ask_product(self):
        responses=("The product has excellent reviews from the customers\n","You can buy the nproducts from our website\n")
        return random.choice(responses)

    def technical_support(self):
        responses=("Please visit our technical support page for more technical help\n",
               "You can call the customer service number for technical queries\n")
        return random.choice(responses)

    def return_policy(self):
        responses=("We have 10-day return policy for the product\n")
        return responses

    def general_query(self):
        responses=("How can I assit You further?\n",
               "Is there any other help you need?\n",
               "Looking for any other help?\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses=("My apologies,Can you please tell more details\n",
               "sorry,Can you please elaborate further?\n",
               "I'm sorry,I did'nt quite understand that,Can you rephrase it?\n")
        return random.choice(responses)

#create an object 
bot=Supportbot()
bot.greet()