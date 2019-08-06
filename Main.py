from Customer import Customer

def main():

    email = raw_input("Enter customer email: ")
    customer1 = Customer(email)
    customer1.Input_info()
    customer1.Verify_info()
    customer1.Output_info()

    email = raw_input("Enter customer email: ")
    customer2 = Customer(email)
    customer2.Input_info()
    customer2.Verify_info()
    customer2.Output_info()

main()