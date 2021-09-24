def start():
    print("Welcome. Choose One of The Following Options:")
    print("   1. TMW Checker")
    print("   2. Help")
    print("   3. Contact")
    print("   4. Exit")
    choice = input("Your Choice: ")
    while True:
        if choice == "1":
            checker()
            break
        elif choice == "2":
            helpp()
            break
        elif choice == "3":
            contact()
            break
        elif choice == "4":
            input("Press any key to exit.")
            break
        print("Invalid Choice. Choose one of the options and press Enter.")
        choice = input("Your Choice: ")





def checker():
    import time

    first = []
    second = []

    ##SUMMARY VARIABLES##
    strMissing = ""
    strMoved = ""
    intMissing = 0
    intMoved = 0
    ##SUMMARY VARIABLES##

    print("Add loads from --TMW WORKSHEET--")
    while True:
        firstInput = input()
        if firstInput.lower() != "start":
            first.append(firstInput)
        elif firstInput.lower() == "start":
            first = list(filter(None, first))
            # print(first)
            break
        else:
            print("Unexpected Error. Check your inputs.")
            break

    print("\n\n\nNumber of loads added: " + str(len(first)))
    print("Proceed to enter loads from --MGL SPREADSHEET--\n\n\n")
    while True:
        secondInput = input()
        if secondInput.lower() != "start":
            second.append(secondInput)
        elif secondInput.lower() == "start":
            second = list(filter(None, second))
            # print(second)
            break
        else:
            second = list(filter(secondInput, second))
            print("Unexpected Error. Check your inputs.")
            break

    print("\n\n\nNumber of loads added: " + str(len(second)))
    # print("Array1: " + str(first))
    # print("Array2: " + str(second))
    print("\n\n")

    if len(first) - len(second) != 0:
        diff = abs(len(first) - len(second))
        print("WARNING: %d load/s diffrence." % diff)
        print("\n\nSee Bellow...\u001b[0m")
    else:
        print("Load Count is Matching.")

    if len(first) - len(second) <= 0:
        intMissing = 0
    else:
        intMissing = len(first) - len(second)

    i = 0
    notPresent = []

    while i < len(first):
        if first[i] in second:
            print(first[i] + "   <== PASS")
            time.sleep(0.2)
            i = i + 1
        else:
            print(first[i] + "   <== REQUIRING ATTENTION")
            notPresent.append(first[i])
            time.sleep(0.2)
            i = i + 1

    print("Loads not Present (NOT ADDED): " + str(notPresent))
    strMissing = str(notPresent)
    print("\n\nBegining Second Check...")
    print(
        "Second Check compares loads that are in Spreadsheet, but not in TMW for today (Loads from the past, wrong PU date, Pushed loads, or closed in TMW)")
    time.sleep(4)

    i = 0
    notPresent = []

    while i < len(second):
        if second[i] in first:
            print(second[i] + "   <== PASS")
            time.sleep(0.2)
            i = i + 1
        else:
            print(second[i] + "   <== REQUIRING ATTENTION")
            notPresent.append(second[i])
            time.sleep(0.2)
            i = i + 1

    print("Count: %d" % len(notPresent))
    print("Loads which need attention: " + str(notPresent))

    intMoved = len(notPresent)
    strMoved = str(notPresent)
    print("\n\n\n")
    print("::: SUMMARY :::")
    print("Loads Missing from Spreadsheet, but are in TMW: %d" % intMissing)
    print("Loads Missing: " + strMissing)
    print("Loads In Spreadsheet, but are not present in TMW for today: %d" % intMoved)
    print("Loads Requiring Attention: " + strMoved)
    print("")
    print("")
    print("Returning to Main Menu in 15 sec...")
    time.sleep(15)
    start()






def helpp():
    print("-------------------")
    print("------= HELP =-----")
    print("-------------------")

    print("How to Use:")
    print("HOW TO COPY LOADS:")
    print(" 1. Open TMW and go to Planned Worksheets.")
    print(" 2. From the drop down menu, Select *Refrigerated loads.")
    print(" 3. Sort loads by earliest PU Date either in descending or ascending order.")
    print(" 4. Left Click the first load for today to mark it.")
    print(" 5. While holding down left shift, left click the last load for today to select all loads for today.")
    print(" 6. Right click on any of the marked loads, go to Export to Excel, and choose *Export Selected")
    print(" 7. A Microsoft Excel instance will open with all the loads we selected in step 4 & step 5.")
    print(" 8. Using a left mouse click, mark ONLY the LoadID from top to bottom.")
    print(" 9. Press CTRL + V.")
    print("")
    print("")
    print("HOW TO USE TMW CHECKER:")
    print(" 1. After TMW CHECKER starts, You will be required to post the loads you exported from TMW FIRST!")
    print(" 2. The Script runs in BASH so you have to use CTRL + SHIFT + V to paste your selection.")
    print(" 3.After you've pasted the loads, type START and press Enter.")
    print(" 4. Repeat steps 2 & 3 with the loads from the local MGL Spreadsheet.")
    print(" 5. After the program is done, check the summary.")
    print("")
    print("")
    print("IMPORTANT: THE ORDER THAT YOU INSERT THE LOADS IS ALWAYS TMW FIRST, MGL SPREADSHEET SECOND. OTHERWISE RESULTS WILL NOT BE ACCURATE!")
    print("")
    print("")
    print("")
    print("")
    start()


def contact():
    print("GITHUB: https://github.com/ARBOFF")
    print("INSTAGRAM: https://instagram.com/arboff.1337")
    print("Email: nikola.arbov@abv.bg")
    print("BTC Address: 0xf6af5320d5f4f97c77b273be577dda3e33ff91d9")
    start()

























