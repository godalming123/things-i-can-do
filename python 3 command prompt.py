esc = False

def execCode(code, autoEscape = True):
    if code == "esc" and autoEscape:
        esc = True

    else:
        try :
            exec(code)

        except Exception as e:
            print (e)

def main () :
    while not esc :
      try :
        execCode(input (": "))
        
      except Exception as e:
        print (e)

if __name__ == "__main__" :
    main ()