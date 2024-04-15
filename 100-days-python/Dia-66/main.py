import tkinter as tk

# Creamos una ventana nueva
window = tk.Tk()
# Le colocamos un nombre a esa ventana
window.title("Python Calculator")
# Le asignamos un tamaño
window.geometry("400x400")  # Sets the size of the
window.configure(bg='white')  # Configuramos el color de fondo de la ventana

# Creamos un label que mostrará el valor total
answer = 0
operator = ''
total = 0
firstParam = 0
hello = tk.Label(
  window, text=answer, bg='black', fg='white', width=10, padx=0,
  pady=0)  # Configuramos el color de fondo y el color de texto del label
hello.grid(
  row=0,
  column=1)  # Añadimos relleno al label para que tenga espacio alrededor


def setAnswer(value):
  global answer
  answer = str(answer)
  answer = f"{answer}{value}"
  answer = int(answer)
  hello["text"] = answer


def setOperator(thisOperator):
  global answer, operator, total, firstParam
  if total == 0:
    firstParam = answer
    operator = thisOperator
    answer = 0
  else:
    firstParam = total
    operator = thisOperator
    answer = 0


def calc():
  global answer, operator, total, firstParam
  secondParam = answer
  total = f"{firstParam} {operator} {secondParam}"
  total = eval(total)
  firstParam = total
  answer = total
  hello["text"] = answer


def delete():
  global answer, operator, total, firstParam
  answer = 0
  operator = ''
  total = 0
  firstParam = 0
  hello['text'] = answer


numericButtons = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], [
  '0',
]]

operatorsButtons = ['+', '-', '*', '/']

for i, row in enumerate(numericButtons):
  for j, text in enumerate(row):
    button = tk.Button(text=text, command=lambda value=text: setAnswer(value))
    button.grid(row=i + 1, column=j)

for i, text in enumerate(operatorsButtons):
  button = tk.Button(text=text, command=lambda value=text: setOperator(value))
  button.grid(row=i + 1, column=4)

equalButton = tk.Button(text='=', command=lambda: calc())
equalButton.grid(row=4, column=2)

clearButton = tk.Button(text='C', command=lambda: delete())
clearButton.grid(row=4, column=1)

# Ejecutamos el bucle principal de la ventana
window.mainloop()
