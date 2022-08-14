from db import User, Post, Base, engine


def main():
    print("Creating database .....")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
