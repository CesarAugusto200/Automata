import tkinter as tk

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                         'U', 'V', 'W', 'X', 'Y', 'Z', 
                         '-'}
        
        self.transitions = {
            'q0': {'F': 'q1','G': 'q13'},
            'q1': {'Y': 'q2','Z': 'q2'},
            'q2': {'-': 'q3'},
            'q3': {'0': 'q4','1': 'q10','2': 'q10','3': 'q10','4': 'q10','5': 'q10','6': 'q10','7': 'q10','8': 'q10','9': 'q10'},
            'q4': {'0': 'q5'},
            'q5': {'0': 'q6'},
            'q6': {'1': 'q7','2': 'q7','3': 'q7','4': 'q7','5': 'q7','6': 'q7','7': 'q7','8': 'q7','9': 'q7'},
            'q7': {'-': 'q8'},
            'q8': {'A': 'q9','B': 'q9','C': 'q9','D': 'q9','E': 'q9','F': 'q9','G': 'q9','H': 'q9','I': 'q9','J': 'q9','K': 'q9','L': 'q9','M': 'q9','N': 'q9','O': 'q9','P': 'q9','Q': 'q9',
                   'R': 'q9','S': 'q9','T': 'q9','U': 'q9','V': 'q9','W': 'q9','X': 'q9','Y': 'q9','Z': 'q9'},
            'q9': {},
            'q10': {'0': 'q11','1': 'q11','2': 'q11','3': 'q11','4': 'q11','5': 'q11','6': 'q11','7': 'q11','8': 'q11','9': 'q11'},
            'q11': {'0': 'q12','1': 'q12','2': 'q12','3': 'q12','4': 'q12','5': 'q12','6': 'q12','7': 'q12','8': 'q12','9': 'q12'},
            'q12': {'0': 'q7','1': 'q7','2': 'q7','3': 'q7','4': 'q7','5': 'q7','6': 'q7','7': 'q7','8': 'q7','9': 'q7'},
            'q13': {'A': 'q14','B': 'q14','C': 'q14','D': 'q14','E': 'q14','F': 'q14', 'G': 'q14','H': 'q14','I': 'q14','J': 'q14','K': 'q14','L': 'q14','M': 'q14','N': 'q14','O': 'q14','P': 'q14','Q': 'q14',
                   'R': 'q14','S': 'q14','T': 'q14','U': 'q14','V': 'q14','W': 'q14'},
            'q14': {'-': 'q3'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q9'}
        
    def validar(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if current_state not in self.states:
                return False
            current_state = self.transitions[current_state].get(symbol, None)
            if current_state is None:
                return False
            self.estadoR=self.transitions
        return current_state in self.accept_states
    
Afd = AFD()

def Validacion():
   current_state = Afd.start_state  # Inicializa el estado actual fuera de la función

def Validacion():
    input_string = Input.get()
    current_state = Afd.start_state
    visited_states = []  # Lista para almacenar los estados visitados

    for symbol in input_string:
        if not Afd.validar(symbol):
            Result.config(text=f"Tipo de cadena inválido: {symbol}")
        visited_states.append(current_state)  # Agrega el estado actual a la lista
        current_state = Afd.transitions.get(current_state, {}).get(symbol, None)
        if current_state is None:
            break

    visited_states.append(current_state)  # Agrega el último estado a la lista
    StateLabel.config(text=f"Estados visitados: {', '.join(visited_states)}")

    if current_state in Afd.accept_states:
        Result.config(text="Tipo de cadena válida.")
    else:
        Result.config(text="Tipo de cadena inválido.")


Window = tk.Tk()

Window.geometry("400x100")

Window.title("Automata")

etiqueta = tk.Label(Window, text="Ingrese una cadena:")
etiqueta.pack()

Input = tk.Entry(Window)
Input.pack()

Button = tk.Button(Window, text="Verificar", command=Validacion)
Button.pack()

Result = tk.Label(Window, text="")
Result.pack()

StateLabel = tk.Label(Window, text="Estado actual: q0")
StateLabel.pack()

Window.mainloop()