import os

modules = filter(
    lambda f: f.endswith(".py") and not f.startswith("_"), 
    os.listdir(".")
)

with open("full.txt", "w") as file:
    file.write("\n".join(m.rstrip(".py") for m in modules))
