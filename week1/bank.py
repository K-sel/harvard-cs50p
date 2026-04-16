str = input("Greeting : ").lower().strip()

match str:
    case "hey":
        print("$20")
    case "how you doing?":
        print("$20")
    case "what's happening?":
         print("$100")
    case "what's up?":
         print("$100")
    case _:
        print("$0")

