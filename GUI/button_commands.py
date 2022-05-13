import GUI.homescreen as homescreen

def Define():
    global ac 
    ac = homescreen.ui.textEdit_4.toPlainText()
    global attack_Bonus
    attack_Bonus = homescreen.ui.textEdit_3.toPlainText()
    global damage_string
    damage_string = homescreen.ui.textEdit_2.toPlainText()
    global minForCrit
    minForCrit = homescreen.ui.textEdit.toPlainText()
    global chance_to_hit 
    chance_to_hit = homescreen.ui.textEdit_5.toPlainText()
    
    # the checkboxes return true or false, true if checked false if not checked
    global adventage
    adventage = homescreen.ui.checkBox.isChecked() 
    global disadventage
    disadventage = homescreen.ui.checkBox_2.isChecked()
    global rerolls 
    rerolls = homescreen.ui.checkBox_3.isChecked()
    
    global avaregeDamage
    avaregeDamage = homescreen.ui.label_7
           
def whenPressed():
    Define()
    print(ac)
    print(attack_Bonus)
    print(damage_string)
    print(minForCrit)
    print(chance_to_hit)
    
    if adventage == True:
        print("true")
    
    x = int(ac) + int(attack_Bonus) + int(damage_string) + int(minForCrit) + int(chance_to_hit)
    avaregeDamage.setText(str(x))
        
 