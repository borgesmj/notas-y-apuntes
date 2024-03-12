print("""
  ##########################################
  #                                        #
  # ¿Qué personaje de los Vengadores eres? #
  #                                        #
  ##########################################
""")
print()
print("Responde las siguientes preguntas con un si o un no")
print()
yesOrNo = input('¿Eres del Planeta tierra? ')
if yesOrNo == 'si':
    yesOrNo = input('¿Eres rico? ')
    if yesOrNo == 'si':
        print('Eres Ironman')
    else:
        yesOrNo = input('¿Tienes mas de 70 años? ')
        if yesOrNo == 'si':
            print('Eres Capitan America')
        else:
            yesOrNo = input('¿Eres un cientifico nuclear? ')
            if yesOrNo == 'si':
                print('Eres Hulk')
            else:
                yesOrNo = input('¿Manejas arco y flacha? ')
                if yesOrNo == 'si':
                  print('Eres Hawkeye')
                else:
                  yesOrNo = input('¿Eres Black Widow? ')
                  if yesOrNo == 'si':
                    print('Adiviné!!')
                  else:
                    finalAnswer = input('Me rindo, ¿Quien eres? ')
                    print(f"""AAAAAAAHHHH, eres {finalAnswer}, no lo había pensado""")
else:
    yesOrNo = input('¿Eres un dios nordico? ')
    if yesOrNo == 'si':
      print('Eres Thor!')
    else:
      finalAnswer = input('No se, ¿quien eres? ')
      print(f"""AAAAAAAHHHH, eres {finalAnswer}, no lo había pensado""")