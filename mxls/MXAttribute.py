from xml.sax.saxutils import escape

class MXAttribute(object):

    def __init__(self, name, value):
        self.name = name
        self.value = str(value)

    def setName(self, name):    
        self.name = name
    def getName(self):
        return self.name 

    def setValue(self, value):    
        self.value = str(value)
    def getValue(self):
        return self.value 

    def toString(self):
        return self.name + '=' + self.value
    
    def toXml(self):
        xml = ''
        if self.value == '~NULL~':
            '<' + self.name.upper() + '></' + self.name.upper() + '<'
        elif self.value == None or self.value == 'None':
            xml = ''
        else:
            xml = '<' + self.name.upper() + '>' + escape(self.value) + '</' + self.name.upper() + '>'
        
        return xml