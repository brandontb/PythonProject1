class Customer:

    def __init__(self, customer_email):
        self.email = customer_email
        self.age = "0"
        self.password = ""
        self.card_number = ""
        self.security_code = ""
        self.first_name = ""
        self.last_name = ""

# =====================================================================================================

    def Input_age(self):
        self.age = raw_input("Enter your age: ")
        while self.age.isalpha() or int(self.age) < 0:
            print("Age must be a positive number.")
            self.age = raw_input("Enter your age: ")

# =====================================================================================================

    def Input_password(self):
        self.password = raw_input("Enter password:")

        correct_length = False
        one_uppercase = False
        one_lowercase = False
        one_number = False

        while one_uppercase == False or one_lowercase == False or one_number == False or correct_length == False:

            one_uppercase = False
            one_lowercase = False
            one_number = False
            correct_length = False

            for i in self.password:
                if i.isupper():
                    one_uppercase = True
                if i.islower():
                    one_lowercase = True
                if i.isdigit():
                    one_number = True

            if one_uppercase == False:
                print("Must have uppercase letter")
                self.password = raw_input("Enter password: ")

            if one_lowercase == False:
                print("Must have lowercase letter.")
                self.password = raw_input("Enter password: ")

            if one_number == False:
                print("Must have one number.")
                self.password = raw_input("Enter password: ")

            if 8 <= len(self.password) <= 12:
                correct_length = True
            else:
                print("Must be between 8 and 12 characters.")
                self.password = raw_input("Enter password: ")

        # print(one_uppercase)
        # print(one_lowercase)
        # print(one_number)

# =====================================================================================================

    def Input_card_number(self):
        self.card_number = raw_input("Enter card number: ")

        card_length = False
        card_letter = True

        while card_length == False or card_letter == True:

            card_length = False
            card_letter = False

            for i in self.card_number:
                if i.isalpha() == True:
                    card_letter = True

            if card_letter == True:
                print("Card number must contain numbers only.")
                self.card_number = raw_input("Enter card number: ")

            if len(self.card_number) == 16:
                card_length = True
            else:
                print("Card number must be 16 digits long.")
                self.card_number = raw_input("Enter card number: ")

# =====================================================================================================

    def Input_security_code(self):
        self.security_code = raw_input("Enter security code: ")

        security_length = False
        security_letter = True

        while security_length == False or security_letter == True:

            security_length = False
            security_letter = False

            for i in self.security_code:
                if i.isalpha() == True:
                    security_letter = True

            if security_letter == True:
                print("Security code must contain numbers only.")
                self.security_code = raw_input("Enter security code: ")

            if len(self.security_code) == 3:
                security_length = True
            else:
                print("Security code must be 3 digits long.")
                self.security_code = raw_input("Enter security code: ")

# =====================================================================================================

    def Input_info(self):
        self.first_name = raw_input("Enter first name: ")
        self.last_name = raw_input("Enter last name: ")

        self.Input_age()
        self.Input_password()
        self.Input_card_number()
        self.Input_security_code()

# =====================================================================================================

    def Verify_info(self):

        print("1. First Name: ", self.first_name)
        print("2. Last Name: ", self.last_name)
        print("3. Email: ", self.email)
        print("4. Age: ", self.age)
        print("5. Password: ", self.password)
        print("6. Card Number: ", self.card_number)
        print("7. Security Code: ", self.security_code)

        correct_entry = int(input("To correct any entry enter the corresponding number, 0 if everything is correct."))

        while correct_entry != 0:

            if correct_entry == 1:
                self.first_name = raw_input("Enter first name: ")
            elif correct_entry == 2:
                self.last_name = raw_input("Enter last name: ")
            elif correct_entry == 3:
                self.email = raw_input("Enter email: ")
            elif correct_entry == 4:
                self.Input_age()
            elif correct_entry == 5:
                self.Input_password()
            elif correct_entry == 6:
                self.Input_card_number()
            elif correct_entry == 7:
                self.Input_security_code()

            print("1. First Name: ", self.first_name)
            print("2. Last Name: ", self.last_name)
            print("3. Email: ", self.email)
            print("4. Age: ", self.age)
            print("5. Password: ", self.password)
            print("6. Card Number: ", self.card_number)
            print("7. Security Code: ", self.security_code)

            correct_entry = int(input("To correct any entry enter the corresponding number, 0 if everything is correct."))

        print("Registration and verification completed for this user.")

# =====================================================================================================

    def Output_info(self):
        customer_info = self.first_name + ", " + self.last_name + ", " + self.age + ", " + self.email + ", " + self.password + ", " + self.card_number + ", " + self.security_code + "\n"
        output_file = open('/Users/brandonbobbitt/Desktop/customers.txt', 'a')
        output_file.write(customer_info)
        output_file.close()












