from steganography.steganography import Steganography                   # Importing module
from default_dict import spy_dict

print '\n \t \t WELCOME TO THE WORLD OF SPY \n'

# Lists
status_list = ['Online', 'Offline', 'Available', 'Unavailable', 'Busy', 'At Work', 'On a Secret Mission']
friend_list_name = ['John', 'Charlie', 'Lucifer', 'Alan', 'Walker']
friend_list_age = ['29', '35', '38', '22', '36']
friend_list_rating = ['4.2', '3.2', '4.5', '3.9', '4.8']
secret_msg = []
special_msg = ['SOS', 'Save Me', 'Danger', 'Fire in Hole']

# Selection of User
ask_user = raw_input ('Choose from the Following: \n1. Continue with Default User \n2. Create a Custom User \n')
if ask_user == '2':
    custom_user_name = raw_input ('Enter Name: \n')
    if len (custom_user_name) > 0:
        salutation = raw_input (custom_user_name + ', you are MALE or FEMALE? \nChoose m/f \n')
        if salutation == 'm':
            print 'Hello! Mr. ' + custom_user_name
            custom_user_age = int (raw_input ('Mr. ' + custom_user_name + ', enter your age \n'))
            if custom_user_age > 50 or custom_user_age < 12:
                print 'Access Denied!'
                exit ()
            else:
                custom_user_rating = float (raw_input ('Enter your Desired Rating \n'))
                if custom_user_rating > 3.5:
                    print 'You are Awesome! \n'
                else:
                    print 'Work Hard! \n'
        elif salutation == 'f':
            print 'Hello! Ms. ' + custom_user_name
            custom_user_age = int (raw_input ('Ms. ' + custom_user_name + ', enter your age \n'))
            if custom_user_age > 50 or custom_user_age < 12:
                print 'Access Denied!'
                exit ()
            else:
                custom_user_rating = float (raw_input ('Enter your Desired Rating Out of 5 \n'))
                if custom_user_rating > 3.5:
                    print 'You are Awesome! \n'
                else:
                    print 'Work Hard! \n'
        print 'WELCOME ' + custom_user_name + ' YOU ARE ' + salutation + ', YOU ARE ' + str (
            custom_user_age) + ' YEARS OLD & YOUR RATING IS ' + str (custom_user_rating)
    else:
        print 'Invalid Choice, Enter a Valid Name \n'

    # infinite loop to keep on repeating the menu, until the user chooses to exit
    infinite_loop = True
    while infinite_loop:
        choice = raw_input ('\nSelect your Desired Choice from below: \n1. ADD A STATUS UPDATE \n2. ADD A FRIEND \n3. '
                            'SEND A SECRET MESSAGE \n4. READ A SECRET MESSAGE \n5. READ CHATS FROM USER \n6. EXIT \n')
        if choice == '6':
            print 'You are Logged Out!'  # User Chooses to Exit
            infinite_loop = False

        elif choice == '1':
            print 'You Chose Status Update \n'  # User Chooses to Update Status
            print status_list

            # Select the Status
            spy_status = raw_input ('Select an Status from the above Status or Enter your Custom Status: \n')
            if spy_status in status_list:
                print 'Your Status is ' + spy_status  # Print the Status
            else:
                status_list.append (spy_status)
                print 'Your Current Updated Status is: ' + spy_status  # Update the Status to the List and Print it

        elif choice == '2':
            print 'You Chose to Add a Friend! \n'
            friend_name = raw_input ('Enter Friend\'s Name: \n')  # Enter the Friend's Name
            friend_age = raw_input ('Enter Friend\'s Age: \n')  # Enter the Friend's Age
            friend_rating = raw_input ('Enter Friend\'s Rating: \n')  # Enter the Friend's Rating
            if friend_name not in friend_list_name:  # Check if name exist in the list
                friend_list_name.append (friend_name)  # if not available append to the list
                print friend_list_name  # print the new updated list
            else:
                print 'Your Friend is Already in the List \n'
                if friend_age > 50 or friend_age < 12:
                    print 'Sorry! Generation Gap, Age Requirement not Fulfilled\n'
                else:
                    friend_list_age.append (friend_age)
                    print 'Your Friend List is as Follow: \n' + friend_list_age

                    # Print an appropriate message having all the details of Spy's Friend
            print 'Your Friend\'s Name is: ' + friend_name + ', Friend\'s age is: ' + friend_age + ', Friend\'s rating is: ' + friend_rating
            print '\nYou have ' + str (len (friend_list_name)) + ' Friends'

        elif choice == '3':
            print('You Chose to Send a Secret Message \n')

            # selecting the friend to whom a secret message has to be send
            select_a_friend = raw_input (str (friend_list_name) + '\nSelect the name of your friend whom you want to '
                                                                  'send a secret message: \n')
            if select_a_friend in friend_list_name:
                print 'Index of Selected Friend is: ' + str (friend_list_name.index (select_a_friend))
                input_image_path = raw_input ('\nEnter the the path of the image which you want to encode with a '
                                              'secret message: \n')  # Choose the Image which needs to be encoded
                text = raw_input ('Enter a Secret Message you want to Hide: \n')  # Enter the Secret Message
                output_image = raw_input (
                    'Enter output image name with .png extension: \n')  # Enter the Output Image path

                Steganography.encode (input_image_path, output_image, text)  # Steganography for encoding the image
                secret_text = Steganography.decode (output_image)  # Store in the image
                secret_msg.append (secret_text)
            else:
                print select_a_friend + ', is not in the list of your friends'  # if friend not in list
                friend_list_name.append (select_a_friend)       # Add friend to the existing list
                print str (friend_list_name) + '\nNew Friend added to the list, its index is: ' + str (
                    friend_list_name.index (select_a_friend))       # Print the Index of the Friend Name from the list
                input_image_path = raw_input ('\nEnter the the path of the image which you want to encode with a '
                                              'secret message: \n')         # Path of Image to be Encoded
                text = raw_input ('Enter a Secret Message you want to Hide: \n')       # Secret Message
                output_image = raw_input ('Enter output image name with .png extension: \n')       # Path of Output Image

                Steganography.encode (input_image_path, output_image, text)         # Steganography arguments
                secret_text = Steganography.decode (output_image)                   # Decoding the secret message
                secret_msg.append (secret_text)

        elif choice == '4':
            print 'You Chose to Read the Secret Message \n'                 # Chooses to read the Secret Message
            if secret_msg:
                print 'Your Secret Message is: \n' + str (secret_text)      # if message sent, Printing the Secret Message
            else:
                print 'No Message Received \n'                              # Else print no message received

        elif choice == '5':
            print 'You Chose to Read the Entire Chat History \n'            # Chooses to read the Entire Chat History
            if secret_msg:                                                  # If a Secret Message is sent, means the user is having a chat with a friend
                print 'You Contacted ' + str (select_a_friend) + ' and you sent him ' + str (secret_text)       # print the name of the user's friend and the secret message sent
            else:
                print 'No Chat History \n'

elif ask_user == '1':               # If Choice is default user
    print 'You Choose to Continue with Default User \n'
    print 'Your Name is: \n'
    print spy_dict.keys() + spy_dict.values()
    # infinite loop to keep on repeating the menu, until the user chooses to exit
    infinite_loop = True
    while infinite_loop:
        choice = raw_input ('\nSelect your Desired Choice from below: \n1. ADD A STATUS UPDATE \n2. ADD A FRIEND \n3. '
                            'SEND A SECRET MESSAGE \n4. READ A SECRET MESSAGE \n5. READ CHATS FROM USER \n6. EXIT \n')
        if choice == '6':
            print 'You are Logged Out!'  # User Chooses to Exit
            infinite_loop = False

        elif choice == '1':
            print 'You Chose Status Update \n'  # User Chooses to Update Status
            print status_list

            # Select the Status
            spy_status = raw_input ('Select an Status from the above Status or Enter your Custom Status: \n')
            if spy_status in status_list:
                print 'Your Status is ' + spy_status  # Print the Status
            else:
                status_list.append (spy_status)
                print 'Your Current Updated Status is: ' + spy_status  # Update the Status to the List and Print it

        elif choice == '2':
            print 'You Chose to Add a Friend! \n'
            friend_name = raw_input ('Enter Friend\'s Name: \n')  # Enter the Friend's Name
            friend_age = raw_input ('Enter Friend\'s Age: \n')  # Enter the Friend's Age
            friend_rating = raw_input ('Enter Friend\'s Rating: \n')  # Enter the Friend's Rating
            if friend_name not in friend_list_name:  # Check if name exist in the list
                friend_list_name.append (friend_name)  # if not available append to the list
                print friend_list_name  # print the new updated list
            else:
                print 'Your Friend is Already in the List \n'
                if friend_age > 50 or friend_age < 12:
                    print 'Sorry! Generation Gap, Age Requirement not Fulfilled\n'
                else:
                    friend_list_age.append (friend_age)
                    print 'Your Friend List is as Follow: \n' + friend_list_age

                    # Print an appropriate message having all the details of Spy's Friend
            print 'Your Friend\'s Name is: ' + friend_name + ', Friend\'s age is: ' + friend_age + ', Friend\'s rating is: ' + friend_rating
            print '\nYou have ' + str (len (friend_list_name)) + ' Friends'

        elif choice == '3':
            print('You Chose to Send a Secret Message \n')

            # selecting the friend to whom a secret message has to be send
            select_a_friend = raw_input (str (friend_list_name) + '\nSelect the name of your friend whom you want to '
                                                                  'send a secret message: \n')
            if select_a_friend in friend_list_name:
                print 'Index of Selected Friend is: ' + str (friend_list_name.index (select_a_friend))
                input_image_path = raw_input ('\nEnter the the path of the image which you want to encode with a '
                                              'secret message: \n')  # Choose the Image which needs to be encoded
                text = raw_input ('Enter a Secret Message you want to Hide: \n')  # Enter the Secret Message
                output_image = raw_input (
                    'Enter output image name with .png extension: \n')  # Enter the Output Image path

                Steganography.encode (input_image_path, output_image, text)  # Steganography for encoding the image
                secret_text = Steganography.decode (output_image)  # Store in the image
                secret_msg.append (secret_text)
            else:
                print select_a_friend + ', is not in the list of your friends'
                friend_list_name.append (select_a_friend)
                print str (friend_list_name) + '\nNew Friend added to the list, its index is: ' + str (
                    friend_list_name.index (select_a_friend))
                input_image_path = raw_input ('\nEnter the the path of the image which you want to encode with a '
                                              'secret message: \n')
                text = raw_input ('Enter a Secret Message you want to Hide: \n')
                output_image = raw_input ('Enter output image name with .png extension: \n')

                Steganography.encode (input_image_path, output_image, text)
                secret_text = Steganography.decode (output_image)
                secret_msg.append (secret_text)

        elif choice == '4':
            print 'You Chose to Read the Secret Message \n'
            if secret_msg:
                print 'Your Secret Message is: \n' + str (secret_text)
            else:
                print 'No Message Received \n'

        elif choice == '5':
            print 'You Chose to Read the Entire Chat History \n'
            if secret_msg:
                print 'You Contacted ' + str (select_a_friend) + ' and you sent him ' + str (secret_text)
            else:
                print 'No Chat History \n'
