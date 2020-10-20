while True :
      prices = [input ("stocks on first day : "), input ("stocks on second day : "), input ("stocks on third day : "), input ("stocks on fourth day : ")]
      sell = []
      for i in range (len (prices) ) :
        try :
          if prices [i] < prices [i + 1] :
              sell.append ("buy (if you do not have any) on the " + str (i+1) + " day -" + str (prices [i]) )
          elif prices [i] > prices [i + 1] :
              sell.append ("sell (if you have any) on the " + str (i+1) + " day +" + str (prices [i]) )
          else :
                sell.append ("do nothing + 0")
        except : # if prices i + 1 does not exsist wich means we are done
          sell.append ("sell (if you have any) on the last day +" + str (prices [i]) )
          for i in sell :
            print (i)
