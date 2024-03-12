class TextOperation:
    def __init__(self, type, value):
        self.type = type
        self.display = value

class RecordHistory:
    def __init__(self):
        self.stack = []

    def AddText(self, char):
        # Don't continue if over one character inputted
        if len(char) > 1:
            return None

        # Don't try to look at top of stack if there's nothing in it
        if len(self.stack) == 0:
            display = ""
        else:
            display = self.stack[-1].display

        self.stack.append(TextOperation("addText", display + char))
        self.Display()

    def RemoveText(self):
        # Checks if there's anything in the stack to look up
        if len(self.stack) == 0:
            return None

        latestDisplay = self.stack[-1].display

        # Checks to see if there's anything to return first
        if len(latestDisplay) < 1:
            return None
        self.stack.append(TextOperation("removeText", latestDisplay[:len(latestDisplay)-1]))
        self.Display()

    def Undo(self):
        # Checks if there's anything in stack first
        if len(self.stack) == 0:
            return None
        self.stack.pop()
        self.Display()

    def Display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        print(self.stack[-1].display)


Record = RecordHistory()

# Basic testing
Record.AddText("a")
Record.AddText("b")
Record.AddText("c")

Record.RemoveText()
Record.RemoveText()

# Looks like undoing too much wont cause an error
Record.Undo()
Record.Undo()
Record.Undo()
Record.Undo()
Record.Undo()
Record.Undo()
Record.Undo()
Record.Display()

# This doesn't get added
Record.AddText("abc")
Record.Display()