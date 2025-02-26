import time as tm

while True:
    try:
        inp = str(input("Mathematical Problem: "))
        print(f"\n------------------------------\n\nProblem:\n{inp}\n\nResult:\n{eval(inp)}")
        error_code = "\n"
        break
    except ZeroDivisionError:
        print("∞ Infinite Impossibilities")
    
    except SyntaxError:
        print("YOU wrote it WRONG")
    
    except:
        print("Idk what went wrong but the reason is always", end="", flush=True)

        tm.sleep(1)
        print(".", end="", flush=True)
        tm.sleep(1)
        print(".", end="", flush=True)
        tm.sleep(1)
        print(". ", end="", flush=True)
        tm.sleep(4)
        print("Y", end="", flush=True)
        tm.sleep(0.8)
        print("O", end="", flush=True)
        tm.sleep(0.8)
        print("U", end="\n\n", flush=True)
        tm.sleep(5)