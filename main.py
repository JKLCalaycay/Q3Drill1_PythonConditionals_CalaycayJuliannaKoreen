
from pyscript import document, display 

def solving_for100 (e): #e for COMPUTATION
    grade1 = float(document.getElementById("input1").value)
    grade2 = float(document.getElementById("input2").value)
    answer = (grade1 + grade2)

    #I used if else statements to see if someone passed or not

    if answer == 100:
        display("YAY! thats right!", target="Status")

    else:
        display("AW! try again...", target="Status")

