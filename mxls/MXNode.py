from mxls.MXAttribute import MXAttribute

class MXNode(object):

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.level = 0
        self.attributes = []
        self.children = []

        if parent != None:
            self.level = parent.getLevel() + 1

    def addAttribute(self, attribute):
        self.attributes.append(attribute)

    def addAttribute2(self, name, value):
        attribute = MXAttribute(name, value)
        self.attributes.append(attribute)

    def addChildNode(self, node):
        node.level = self.level + 1
        self.children.append(node)

    def removeLastChildNode(self):
        self.children.pop()

    def addChildNodeNE(self, node):
        if len(self.children) > 0:

            lastNode = self.children[(len(self.children)-1)]
    
            if (lastNode.equals(node)):
                return lastNode

        node.setLevel(node.getLevel() + 1)

        self.children.append(node)

        return node

    def equals(self, compareNode):
        if self.name != compareNode.name or len(self.attributes) != len(compareNode.attributes):
            return False
        
        i=0

        for attribute in self.attributes:
            
            if attribute.value != compareNode.attributes[i].value:
                return False

            i=i + 1

        return True

    def toXml(self):
        
        if self.parent == None:
            xml = ''
        else:
            xml = '<' + self.name + ' action="AddChange">'

        for attribute in self.attributes:
            xml = xml + attribute.toXml()

        for childNode in self.children:
            xml = xml + childNode.toXml()

        
        if self.parent == None:
            xml = xml
        else:
             xml = xml + '</' + self.name + '>'

        return xml


    def setLevel(self, level):    
        self.level = level
    def getLevel(self):
        return self.level

    def setSheetRow(self, sheetRow):    
        self.sheetRow = sheetRow
    def getSheetRow(self):
        return self.sheetRow 
