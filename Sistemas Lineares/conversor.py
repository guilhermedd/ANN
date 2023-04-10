cu =  [7, 9, 11, 12, 17, 18, 19, 22, 24, 26, 27, 29]

pipi = '{'

try:
     for c in cu:
          for p in c:
               pipi += str(p)
               if p is not c[len(c)-1]:
                    pipi += ','
          
          pipi += '},{'
except:
     for p in cu:
          pipi += str(p)
          if p is not cu[len(cu)-1]:
               pipi += ','
     
     pipi += '},{'
print(pipi, len(cu))