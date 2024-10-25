def number_of_years(years): 
    if years <= 2:
        print("Here are the 11 step of archary success:")
        x = 1
        for i in step:
            print(f"{x} {i}")
            x = x + 1 
    else:
        print("As a refresher, here are the 11 step of archary success:")
        x = 1
        for i in step:
            print(f"{x} {i}")
            x = x + 1 


archary = True

while archary:

    print("Enter shot to exit ")
    name = input("Hi what is your name: ")

            # print("Have a grat time shoting ")

    step = ["Stance", "Nock Arrow", "Draw Hand Placement", "Bow Hand Placement", "Pre-Draw", "Draw", "Anchor" , "Aiming", "Shot SetUp", "Release", "Follow Through & Reflect"]
    years = int(input(f"{name} how manny yers have you been doing archary: "))

    if years == 'shot':
            print("Have a grat time shoting ")
    else:
        number_of_years(years)
    shot = input("Are you done for the day (yes or no): ").lower()
    if shot == 'yes':
        archary = False

print("Thank you for using the archary app")













