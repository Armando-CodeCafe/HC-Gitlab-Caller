import makedirs

members = "members.json"
if __name__ == "__main__":
    with open(members) as  file:
        makedirs.makedirs(file)
