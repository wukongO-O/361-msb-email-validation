
def validate_email(user):
    done_validating = 0
    while done_validating != 1:
        email = user['email']
        comm_file = open('ev-service.txt', 'w')
        comm_file.write(email)
        comm_file.close()

        # get response from the service
        while True:
            response_file = open('ev-service.txt', 'r')
            response = response_file.readline()
            if response == "valid":
                done_validating = edit_email(user, email)
                break
            elif response == "invalid":
                print("Your email address is invalid. Please try again.")
                retry_email(user)
                break

    with open('ev-service.txt', 'w') as comm_file2:
        comm_file2.write('done')


def edit_email(user, email):
    user_input = input(f"Do you want to email cookies to the following address: {email}? Enter 'y' to confirm. Enter 'rm' to remove the email. Enter any other key to provide a different email." )
    command = user_input.lower()
    if command == "rm":
        user['email'] = ''
        print("Your email address is removed. You may proceed as a guest.")
        return 1
    elif command == "y":
        print("Your email address is saved. You may use it to get cookies later.")
        return 1
    else:
        retry_email(user)
        return 0


def retry_email(user):
    user_input = input("Please enter your email: ")
    user['email'] = user_input


def main(user):
    # sent request
    validate_email(user)



if __name__ == "__main__":
    main({'user': 'a', 'email': 'abcmail.com'})

