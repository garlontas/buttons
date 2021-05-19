import os

if __name__ == "__main__":
    with open("README.md", "a") as readme:
        for i in os.listdir("buttons/150x44/"):
            readme.write("[![Button](https://raw.githubusercontent.com/garlontas/buttons/main/buttons/150x44/{0})](https://github.com/garlontas/buttons#readme)".format(i))
            readme.write("\n")