
## BEGIN TEST SUITE ###########################################################
errors = 0


def test(trie, value, present):
    global errors
    if trie.find(value) != present:
        print("   ERROR:  Did not achieve:", end="")
        errors += 1
    if present:
        print("   trie contains", value)
    else:
        print("   trie does not contain", value)


def trieTest():
    global errors
    trie = Trie()
    print(trie.enumerate())
    print("empty trie")
    test(trie, "Programming", False)

    print("inserting Programming")
    trie.insert("Programming")
    test(trie, "Programming", True)
    test(trie, "Program", False)
    trie.insert("is")
    trie.insert("a")
    trie.insert("way")
    trie.insert("of")
    trie.insert("life")

    print("inserting Rocks")
    trie.insert("Rocks")
    test(trie, "Programming", True)
    test(trie, "Program", False)
    test(trie, "Rocks", True)

    print("inserting Program")
    trie.insert("Program")
    test(trie, "Programming", True)
    test(trie, "Program", True)
    test(trie, "Programs", False)

    print("insert Programs")
    trie.insert("Programs")
    test(trie, "Programming", True)
    test(trie, "Program", True)
    test(trie, "Programs", True)

    print("delete Rocks")
    trie.delete("Rocks")
    test(trie, "Programming", True)
    test(trie, "Rocks", False)

    print("delete Program")
    trie.delete("Program")
    test(trie, "Programming", True)
    test(trie, "Program", False)
    test(trie, "Programs", True)

    print("delete Programming")
    trie.delete("Programming")
    test(trie, "Programming", False)
    test(trie, "Program", False)
    test(trie, "Programs", True)

    print("try single letter already in trie")
    test(trie, "P", False)
    trie.insert("P")
    test(trie, "P", True)
    trie.delete("P")
    test(trie, "P", False)
    test(trie, "Programs", True)

    print("try single letter not already in trie")
    test(trie, "X", False)
    trie.insert("X")
    test(trie, "X", True)
    trie.delete("X")
    test(trie, "X", False)
    test(trie, "Programs", True)

    print("delete Programs")
    trie.delete("Programs")
    test(trie, "Programs", False)
    test(trie, "Programming", False)
    test(trie, "Program", False)
    test(trie, "P", False)

    print("enumerate")
    enumeration = trie.enumerate()
    print("   ", enumeration)
    if enumeration != ["a", "is", "life", "of", "way"]:
        errors += 1
        print("Error in trie enumeration")

    print("merge")
    trie2 = Trie()
    trie2.insert("now")
    trie2.insert("know")
    trie2.insert("knowledge")
    enumeration = trie2.enumerate()
    if enumeration != ["know", "knowledge", "now"]:
        errors += 1
        print("error in trie2 enumeration")
        print("we got", enumeration)

    trie2.merge(trie)
    enumeration = trie2.enumerate()
    print("   ", enumeration)
    if enumeration != ["a", "is", "know", "knowledge", "life", "now", "of", "way"]:
        errors += 1
        print("error in trie2 enumeration post merge")
        print("we got", enumeration)

    print("Errors Detected:", errors)


trieTest()
## END TEST SUITE #############################################################
