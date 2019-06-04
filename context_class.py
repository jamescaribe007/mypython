#!/usr/local/bin/python3.7

class FileManager():
      def __init__(self, filename, mode):
          self.filename = filename
          self.mode = mode
          self.file = None
          
      def __enter__(self):
          self.file = open(self.filename, self.mode)
          return self.file
      
      def __exit__(self, type, value, traceback):
          self.file.close()
    
#Here is the usage of context class    
with FileManager('file.txt','w') as f:
     f.write('Ay nanita!!!')
   
print(f.closed)   
