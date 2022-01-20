
## BEGIN TEST SUITE ###########################################################
errors = 0


def test(testcase, x, y):
    global errors
    if x != y:
        print(testcase, "expected", x, "but got", y)
        errors += 1


def pqTest():
    global errors
    print("Testing Priority Queue")

    pq = PriorityQueue()

    print("testing empty queue")
    test("enumerate empty queue", [], pq.enumerate())
    try:
        test("peek empty queue", None, pq.peek())
    except IndexError:
        print("peek empty queue", "IndexError")

    test("empty empty queue", True, pq.isEmpty())
    test("size empty queue", 0, pq.size())
    test("remove empty queue", None, pq.remove())

    print("inserting some values")

    pq.insert(3)
    pq.insert(1)
    pq.insert(4)
    pq.insert(1)
    pq.insert(-100)
    pq.insert(100)

    test("enumerate populated queue", [100, 4, 3, 1, 1, -100], pq.enumerate())
    test("peek populated queue", 100, pq.peek())
    test("empty populated queue", False, pq.isEmpty())
    test("size populated queue", 6, pq.size())

    print("removing some values")
    test("removing first value", 100, pq.remove())
    test("removing second value", 4, pq.remove())

    test("enumerate populated queue", [3, 1, 1, -100], pq.enumerate())
    test("peek populated queue", 3, pq.peek())
    test("empty populated queue", False, pq.isEmpty())
    test("size populated queue", 4, pq.size())

    print("removing the rest of the values")
    test("removing first value", 3, pq.remove())
    test("removing second value", 1, pq.remove())
    test("removing third value", 1, pq.remove())
    test("removing fourth value", -100, pq.remove())
    test("removing nonexistent value", None, pq.remove())

    test("enumerate emptied queue", [], pq.enumerate())
    try:
        test("peek emptied queue", None, pq.peek())
    except IndexError:
        print("peek empty queue", "IndexError")
    test("empty emptied queue", True, pq.isEmpty())
    test("size emptied queue", 0, pq.size())
    test("remove emptied queue", None, pq.remove())

    print("repopulating queue from a collection")
    pq.addAll([9, 4, 8, 7, 0, 7, 8])
    test("enumerate repopulated queue", [9, 8, 8, 7, 7, 4, 0], pq.enumerate())
    test("peek repopulated queue", 9, pq.peek())
    test("empty repopulated queue", False, pq.isEmpty())
    test("size populated queue", 7, pq.size())

    print("removing an element")
    test("removing the top element from the repopulation", 9, pq.remove())

    test("enumerate repopulated queue", [8, 8, 7, 7, 4, 0], pq.enumerate())
    test("peek repopulated queue", 8, pq.peek())
    test("empty repopulated queue", False, pq.isEmpty())
    test("size populated queue", 6, pq.size())

    print("test with strings too")
    pq2 = PriorityQueue()
    pq2.addAll(["huey", "louis", "dewey", "moe", "larry", "curly"])

    test(
        "enumerate string queue",
        ["moe", "louis", "larry", "huey", "dewey", "curly"],
        pq2.enumerate(),
    )
    test("peek string queue", "moe", pq2.peek())
    test("empty string queue", False, pq2.isEmpty())
    test("size string queue", 6, pq2.size())
    test("remove from string queue", "moe", pq2.remove())
    test(
        "enumerate string queue",
        ["louis", "larry", "huey", "dewey", "curly"],
        pq2.enumerate(),
    )
    test("peek string queue", "louis", pq2.peek())
    test("empty string queue", False, pq2.isEmpty())
    test("size string queue", 5, pq2.size())
    print("End of Priority Queue Test")
    print("Errors Detected:", errors)


pqTest()
## END TEST SUITE #############################################################
