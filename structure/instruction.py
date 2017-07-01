class Instruction:
    code = None
    cursor = None
    def __init__(self,code = None):
        if code != None:

    def setCursor(self,c):
        if c < 0 or c >= len(code):
            return False
        self.cursor = c
        return True
    def getCursor(self):
        return self.cursor
