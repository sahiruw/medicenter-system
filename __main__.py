from utils.authentication import Authentication

if __name__ == '__main__':
    auth = Authentication()
    user = auth.login()

    print(f"\nWelcome {user.getusername()} Follow the instructions.")

    while True:
        user.work()

