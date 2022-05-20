'''x = [ x1 : [ var1 var2 var3 var4 ]
      x2 : [ var1 var2 var3 var4 ] 
      x3 : [ var1 var2 var3 var4 ] ]
w = [ a
      b
      c ]
  = [ [ a a a a ] 
      [ b b b b ]  
      [ c c c c ] ]

w . a = [ a b c ] . [ x1 x2 x3 ]
      = a*x1 + b*x2 + c*x3

      = [ a*x1_var1 + a*x1_var2 + a*x1_var3 + a*x1_var4
          b*x2_var1 ... 
          c*x3_var1 ...]'''