def SortByHeight(a):
   b=sorted([i for i in a if i!=-1])
   for j,i in  enumerate(a):
      if i==-1:
         b.insert(j,i)
   print(b)
   return(b)
      
