import os

class TuringMachine:
    RIGHT = 1
    LEFT = -1
    BLANK = '$'

    def __init__(self, states, input_symbols, tape_symbols, transitions, initial_state, blank_symbol, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.tape_symbols = tape_symbols
        self.transitions = transitions
        self.current_state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states
        self.tape = []
        self.head_position = 0

    def load_tape(self, input_string):
        self.tape = list(input_string) + [self.blank_symbol]

    def step(self):
        current_symbol = self.tape[self.head_position]
        state_transitions = self.transitions.get(self.current_state, {})
        
        if current_symbol not in state_transitions:
            raise ValueError(f"Sem transição para o estado {self.current_state} e símbolo {current_symbol}")
        
        next_state, write_symbol, direction = state_transitions[current_symbol]
        self.tape[self.head_position] = write_symbol
        self.current_state = next_state
        self.head_position += direction

    def run(self):
        while self.current_state not in self.final_states:
            if self.tape[self.head_position] == '@':  # Parada ao encontrar '@'
                break
            self.step()

    def get_tape_content(self):
        return ''.join(self.tape).strip(self.blank_symbol)

    def get_clean_output(self):
        # Remove símbolos de controle (., -, /, @) para exibir apenas a saída decodificada
        return ''.join([char for char in self.tape if char.isalpha() or char == ' '])


# Função para ler os arquivos .dat da pasta do projeto
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

# Configuração da Máquina de Turing
states = [
    'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 
    'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 
    'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 
    'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40'
]
input_symbols = ['|', '-', '.', '/', '@']
tape_symbols = input_symbols + ['|', '-', '.', '/', '@', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$']
transitions = {
    'q0': {
        '|': ('q0', '|', TuringMachine.RIGHT),
        '.': ('q1', '.', TuringMachine.RIGHT),
        '-': ('q4', '-', TuringMachine.RIGHT),
        '/': ('q0', ' ', TuringMachine.RIGHT),  
        ' ': ('q6', ' ', TuringMachine.RIGHT),  
        '@': ('q40', '@', TuringMachine.RIGHT)
    },
    'q1': {
        '-': ('q3', '-', TuringMachine.RIGHT),
        '.': ('q2', '.', TuringMachine.RIGHT),
        '|': ('q0', 'E', TuringMachine.RIGHT)
    },
    'q2': {
        '.': ('q11', '.', TuringMachine.RIGHT),
        '-': ('q12', '-', TuringMachine.RIGHT),
        '|': ('q0', 'I', TuringMachine.RIGHT)
    },
    'q3': {
        '.': ('q10', '.', TuringMachine.RIGHT),
        '-': ('q13', '-', TuringMachine.RIGHT),
        '|': ('q0', 'A', TuringMachine.RIGHT)
    },
    'q4': {
        '.': ('q6', '.', TuringMachine.RIGHT),
        '-': ('q5', '-', TuringMachine.RIGHT),
        '|': ('q0', 'T', TuringMachine.RIGHT)
    },
    'q5': {
        '.': ('q14', '.', TuringMachine.RIGHT),
        '-': ('q9', '-', TuringMachine.RIGHT),
        '|': ('q0', 'M', TuringMachine.RIGHT)
    },
    'q6': {
        '.': ('q7', '.', TuringMachine.RIGHT),
        '-': ('q8', '-', TuringMachine.RIGHT),
        '|': ('q0', 'N', TuringMachine.RIGHT)
    },
    'q7': {
        '.': ('q15', '.', TuringMachine.RIGHT),
        '-': ('q16', '-', TuringMachine.RIGHT),
        '|': ('q0', 'D', TuringMachine.RIGHT)
    },
    'q8': {
        '.': ('q17', '.', TuringMachine.RIGHT),
        '-': ('q18', '-', TuringMachine.RIGHT),
        '|': ('q0', 'Y', TuringMachine.RIGHT)
    },
    'q9': {
        '.': ('q36', '.', TuringMachine.RIGHT),
        '-': ('q33', '-', TuringMachine.RIGHT),
        '|': ('q0', 'O', TuringMachine.RIGHT)
    },
    'q10': {
        '.': ('q26', '.', TuringMachine.RIGHT),
        '|': ('q0', 'R', TuringMachine.RIGHT)
    },
    'q11': {
        '.': ('q20', '.', TuringMachine.RIGHT),
        '-': ('q21', '-', TuringMachine.RIGHT),
        '|': ('q0', 'S', TuringMachine.RIGHT)
    },
    'q12': {
        '.': ('q19', '.', TuringMachine.RIGHT),
        '-': ('q20', '-', TuringMachine.RIGHT),
        '|': ('q0', 'U', TuringMachine.RIGHT)
    },
    'q13': {
        '.': ('q23', '.', TuringMachine.RIGHT),
        '-': ('q22', '-', TuringMachine.RIGHT),
        '|': ('q0', 'W', TuringMachine.RIGHT)
    },
    'q14': {
        '.': ('q25', '.', TuringMachine.RIGHT),
        '-': ('q25', '-', TuringMachine.RIGHT),
        '|': ('q0', 'G', TuringMachine.RIGHT)
    },
    'q15': {
        '.': ('q39', '.', TuringMachine.RIGHT),
        '|': ('q0', 'B', TuringMachine.RIGHT)
    },
    'q16': {
        '|': ('q0', 'X', TuringMachine.RIGHT)
    },
    'q17': {
        '|': ('q0', 'C', TuringMachine.RIGHT)
    },
    'q18': {
        '|': ('q0', 'Y', TuringMachine.RIGHT)
    },
    'q19': {
        '|': ('q0', 'F', TuringMachine.RIGHT)
    },
    'q20': {
        '.': ('q27', '.', TuringMachine.RIGHT),
        '-': ('q28', '-', TuringMachine.RIGHT),
        '|': ('q0', 'H', TuringMachine.RIGHT)
    },
    'q21': {
        '-': ('q29', '-', TuringMachine.RIGHT),
        '|': ('q0', 'V', TuringMachine.RIGHT)
    },
    'q22': {
        '-': ('q32', '-', TuringMachine.RIGHT),
        '|': ('q0', 'J', TuringMachine.RIGHT)
    },
    'q23': {
        '|': ('q0', 'P', TuringMachine.RIGHT)
    },
    'q24': {
        '|': ('q0', 'Q', TuringMachine.RIGHT)
    },
    'q25': {
        '.': ('q38', '.', TuringMachine.RIGHT),
        '|': ('q0', 'Z', TuringMachine.RIGHT)
    },
    'q26': {
        '|': ('q0', 'L', TuringMachine.RIGHT)
    },
    'q27': {
        '|': ('q0', '5', TuringMachine.RIGHT)
    },
    'q28': {
        '|': ('q0', '4', TuringMachine.RIGHT)
    },
    'q29': {
        '|': ('q0', '3', TuringMachine.RIGHT)
    },
    'q30': {
        '-': ('q31', '-', TuringMachine.RIGHT)
    },
    'q31': {
        '|': ('q0', '2', TuringMachine.RIGHT)
    },
    'q32': {
        '|': ('q0', '1', TuringMachine.RIGHT)
    },
    'q33': {
        '.': ('q35', '.', TuringMachine.RIGHT),
        '-': ('q36', '-', TuringMachine.RIGHT),
        '|': ('q0', 'T', TuringMachine.RIGHT)
    },
    'q34': {
        '-': ('q37', '-', TuringMachine.RIGHT),
        '|': ('q0', 'S', TuringMachine.RIGHT)
    },
    'q35': {
        '|': ('q0', '9', TuringMachine.RIGHT)
    },
    'q36': {
        '|': ('q0', '8', TuringMachine.RIGHT)
    },
    'q37': {
        '|': ('q0', '7', TuringMachine.RIGHT)
    },
    'q38': {
        '|': ('q0', '6', TuringMachine.RIGHT)
    },
    'q39': {
        '|': ('q0', 'O', TuringMachine.RIGHT)
    },
    'q40': {
        '|': ('q0', '0', TuringMachine.RIGHT)
    }
}
initial_state = 'q0'
blank_symbol = '$'
final_states = ['q40']

# Perguntar ao usuário qual fita ele deseja ler
def ask_for_tape():
    print("Escolha qual fita ler:")
    print("1 - fita01.dat")
    print("2 - fita02.dat")
    print("3 - fita03.dat")

    choice = input("Digite o número da fita (1, 2 ou 3): ")

    if choice == "1":
        return 'fita01.dat'
    elif choice == "2":
        return 'fita02.dat'
    elif choice == "3":
        return 'fita03.dat'
    else:
        print("Escolha inválida. Usando fita01.dat por padrão.")
        return 'fita01.dat'


file_name = ask_for_tape()


if os.path.exists(file_name):
    print(f"\nProcessando {file_name}...")

    # Lê o conteúdo do arquivo
    tape_content = read_file(file_name)
    
    # Criação e execução da máquina para cada fita
    tm = TuringMachine(states, input_symbols, tape_symbols, transitions, initial_state, blank_symbol, final_states)

    # Carrega a fita na máquina
    tm.load_tape(tape_content)

    # Executa a máquina
    tm.run()

    # Exibe o processamento completo
    print("Processamento:", tm.get_tape_content())

    # Exibe apenas a saída limpa
    print("Saída Final:", tm.get_clean_output())
else:
    print(f"Arquivo {file_name} não encontrado.")
