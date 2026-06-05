isPresent = False
# if else
if isPresent == True:
    print("Yes")
else:
    print("No")


userBuyAmount = 50
#if else if chain if else
if userBuyAmount > 1000:
    print("Congratulation you have got 20% discount")
elif userBuyAmount > 500:
    print("Congratulation you have got 10% discount")
elif userBuyAmount >= 100:
    print("Congratulation you have got 5% discount")
else:
    print("Sorry no discount")

# nested if else
isGuestUser = False
if isGuestUser == True:
    print("Welcome Guest user to free videos with ads")
else:
    userSubscription = "P"
    if userSubscription == "S":
        print("Welcome user to free + paid videos with ads")
    else:
        print("Welcome user to free + paid videos without ads")