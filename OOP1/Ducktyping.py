# Duck Typing : It is concept where the type of obj id determined 
# by its behaviour,not by its class

class inkjetPrinter:
    def printdocument(self,document):
        print("Inkjet printer printing :",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser printer printing :",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"Saving  :{document} as pdf")

def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    StartPrinting(inkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())


main()




