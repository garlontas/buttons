import os

if __name__ == "__main__":
    with open("README.md", "a") as readme:
        for i in os.listdir("buttons/150x44/"):
            mdline = "[![Button](https://raw.githubusercontent.com/garlontas/buttons/main/buttons/150x44/{0})](https://github.com/garlontas/buttons#svg-buttons)".format(i)
            readme.write(mdline)
            readme.write("\n")
            readme.write("Embed this button with: ```{}```".format(mdline).replace("Button", "Description here").replace("https://github.com/garlontas/buttons#svg-buttons", "<Your Link here>"))
            readme.write("\n\n\n")