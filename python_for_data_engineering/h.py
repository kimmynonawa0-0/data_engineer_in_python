users = {}  # ← Defined OUTSIDE the loop — persists across iterations

while True:
    print("\n1. Create Account")
    print("2. Log In")
    print("3. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        name = input("Enter your name: ").strip()
        if name in users:
            print("Username already exists.")
            continue
        password = input("Enter your password: ").strip()
        users[name] = password   # ✅ Stores using the actual name as key
        print("Account created!")

    elif choice == 2:
        name = input("Enter your name: ").strip()
        password = input("Enter your password: ").strip()
        if name in users and users[name] == password:
            print(f"Welcome back, {name}!")
        else:
            print("Invalid username or password.")

    elif choice == 3:
        print(users)
        break