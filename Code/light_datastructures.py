
class Stack(object):
    def __init__(self):
        self.values = []
    def isEmpty(self):
        return self.values == []
    def push(self,  value):
        self.values.append(value)
    def pop(self):
        if(len(self.values) > 0):
            return self.values.pop()
        else :
            print("Empty Stack")
    def peek(self):
    	if(len(self.values) == 0):
    		return None
    	else:
        	return self.values[len(self.values)-1]
    def size(self):
        return len(self.values)
    def pprint(self):
        print self.values

class Queue(object):
    def __init__(self):
        self.values = []
    def isEmpty(self):
        return self.values == []
    def enqueue(self, value):
        self.values.insert(0,value)
    def dequeue(self):
        if(len(self.values) > 0):
            return self.values.pop()
        else :
            print("Empty Queue")
    def peek(self):
        return self.values[len(self.values)-1]
    def size(self):
        return len(self.values)

class HashTable(object):
    def __init__(self, size, hashValue):
        self.values = [[] for x in range(size)]
        self.hashValue = hashValue
        self.keyList = []

    def hashValueLocation(self, key):
        if(isinstance(key, str)):
            sum = 0
            for x in key:
                sum += ord(x)
            return sum % self.hashValue
        else:
            return key % self.hashValue

    def containsKey(self, key):
        if(self.values[self.hashValueLocation(key)] == []):
            return False
        else:
            for x in self.values[self.hashValueLocation(key)]:
                if (x[0] == key):
                    return True
            return False


    def put(self, key, value):
        self.values[self.hashValueLocation(key)].append((key, value))
        self.keyList.append(key)

    def get(self, key):
        if(self.values[self.hashValueLocation(key)] == []):
            return []
        else:
            for x in self.values[self.hashValueLocation(key)]:
                if (x[0] == key):
                    return x[1]
            return []

    def isEmpty(self):
        if len(self.keyList) > 0:
            return False
        else:
            return True

    def getKeys(self):
        return self.keyList

    def remove(self, key):
        if(self.values[self.hashValueLocation(key)] == []):
            return False
        else:
            for x in self.values[self.hashValueLocation(key)]:
                if (x[0] == key):
                    self.values[self.hashValueLocation(key)].remove((x[0], x[1]))
                    return True
            return False

    def size(self):
        return len(self.keyList)

    def printTable(self):
        for x in self.values:
            print("[]")
            for y in x:
                print(y)



# table = [[] for x in range(10)]
# print(table)

# myHashtable = HashTable(20,11)
# print(myHashtable.isEmpty())
# myHashtable.put("hello", 25)
# myHashtable.put("bye", 45)
# myHashtable.put("a", 2)
# myHashtable.put("b", 3)
# myHashtable.put("k", 4)
# myHashtable.put("i", 5)
# myHashtable.put("f", 6)
# myHashtable.put("e", 7)
# # colision a and l
# myHashtable.put("l", 8)



# print("PrintTable")
# myHashtable.printTable()

# print(" ")
# print(" ")

# print(myHashtable.get("l"))
# print(myHashtable.containsKey("a"))
# print(myHashtable.containsKey("z"))
# print(myHashtable.isEmpty())
# print(myHashtable.size())
# print(myHashtable.getKeys())

# print(" ")
# print(" ")

# mylist  = []
# mylist.append(("one", 1))
# mylist.append(("two", 2))
# mylist.append(("thee", 3))
# print(mylist)

# for x in mylist:
#     if(x[0] == "one"):
#         print("yesOne")
#         print(x)
#     else:
#         print("noOne")
#         print(x)

# print("")
# print("Stack")
# mystack = Stack()
# mystack.push(3)
# mystack.push(2)
# mystack.push(1)
# print mystack.isEmpty()
# print mystack.pop()
# print mystack.pop()
# print mystack.peek()
# print mystack.pop()
# print mystack.pop()
# print mystack.isEmpty()

# print("")
# print("Queue")
# myqueue = Queue()
# myqueue.enqueue(1)
# myqueue.enqueue(2)
# myqueue.enqueue(3)
# print myqueue.isEmpty()
# print(myqueue.dequeue())
# print(myqueue.dequeue())
# print(myqueue.isEmpty())
# print(myqueue.dequeue())
# print(myqueue.dequeue())
# print(myqueue.isEmpty())
