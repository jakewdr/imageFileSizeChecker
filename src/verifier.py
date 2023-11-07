import os 

def verifier ():
    if os.path.exists("ENIAC-changing_a_tube.jpg") == True:
        import checker
        checker.fileSizeChecker("ENIAC-changing_a_tube.jpg")
    else:
        print("Image not found!")