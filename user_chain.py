class User:
    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = True
        self.gold_card_points = 200

    def display_info(self):
        print("--------------------------------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is reward member: {self.is_reward_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("--------------------------------")

# this method change the user's member status to
#  True and set their gold card points to 200.
    def enroll(self):
        # member check
        if self.is_reward_member:
            print("User already a member")
            return False
        self.is_reward_member = True
        self.gold_card_points = 200

# this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("not enough points.")
            return 
        self.gold_card_points -= amount


user_daniel = User("Daniel", "Flores", "daniel@email.com", 32)
user_daniel.display_info().enroll().spend_points(50).display_info()



class User2:
    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("--------------------------------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is reward member: {self.is_reward_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("--------------------------------")

# this method change the user's member status to
#  True and set their gold card points to 200.
    def enroll(self):
        # member check
        if self.is_reward_member:
            print("User already a member")
            return False
        self.is_reward_member = False
        self.gold_card_points = 200

# this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("not enough points.")
            return 
        self.gold_card_points -= amount


user_luis = User("Luis", "Flores", "luis@email.com", 39)
user_luis.display_info().enroll().display_info().spend_points(80).display_info()   




class User3:
    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("--------------------------------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is reward member: {self.is_reward_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("--------------------------------")

# this method change the user's member status to
#  True and set their gold card points to 200.
    def enroll(self):
        # member check
        if self.is_reward_member:
            print("User already a member")
            return False
        self.is_reward_member = True
        self.gold_card_points = 200

# this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("not enough points.")
            return 
        self.gold_card_points -= amount


user_doris = User("Doris", "Chang", "doris@email.com", 57)
user_doris.display_info().enroll().display_info().spend_points(100).display_info()