def greet(user_name: str) -> None:
    print(f"Hallo, {user_name}!")


name: str = input("Enter your name: ").strip()
greet(name)
