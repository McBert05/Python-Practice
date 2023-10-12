# this class we built in making_custom_containers.py has a tiny problem
class TagCloud:
    def __init__(self):
        # we use F2 o rename objects in VS Code
        # if we prefix certain methods/attributes in a class with double underscore it is considered private
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")

# this code will work just fine
print(cloud["PYTHON"])

# but if we are to switch it up and do something like this we get
# this will give us access to the underlying dictionary and generate an error because all the keys are lower case
# and there exists no key that is "PYTHON"
# print(cloud.tags["PYTHON"])
