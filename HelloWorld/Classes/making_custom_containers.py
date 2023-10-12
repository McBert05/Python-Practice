# in python there exists list, sets, dictionaries and so on
# these data structures or container types are pretty useful, and sufficient for most cases
# but there are times where you want to create your own custom container types
# for example here we have this class 'TagCloud' which we will implement from scratch
# with this class we can keep track of the number of various tags on a block
class TagCloud:
    # constructor, initialize tags attribute to an empty dictionary
    def __init__(self):
        self.tags = {}

    # '__add__' magic method, that takes in a tag
    # checks to see if tag is already in dictionary
    # if the value is present add it to dictionary, otherwise increment by 1
    # 'lower' method is implemented to bypass case-sensitivity
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # '__getitem__' magic method returns the count of a given tag
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # '__setitem__' magic method sets the count of a given tag
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # '__len__' magic method used to get the number of items in this Tag Cloud
    def __len__(self):
        return len(self.tags)

    # '__iter__' magic method used to generate one item at a time in a for loop
    def __iter__(self):
        # we use the iterator object and we call the 'iter' object and pass in the class tags
        iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
