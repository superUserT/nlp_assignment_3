from collections import deque

class NFSA:
    """
    Object-oriented representation of a Non-Deterministic Finite State Automaton.
    """
    def __init__(self, states, start_state, accept_states, transitions):
        self.states = states
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

def nd_recognize(tape, machine, strategy="DFS"):
    """
    Executes the ND-RECOGNIZE state-space search algorithm using a double-ended queue[cite: 1].
    """
    agenda = deque()
    agenda.append((machine.start_state, 0))

    while agenda:
        # Stack behavior for DFS, Queue behavior for BFS[cite: 1]
        if strategy == "DFS":
            current_node, tape_ptr = agenda.pop()
        elif strategy == "BFS":
            current_node, tape_ptr = agenda.popleft()
        else:
            raise ValueError("Strategy must be 'DFS' or 'BFS'.")

        if tape_ptr == len(tape) and current_node in machine.accept_states:
            return True

        # 1. Explore Epsilon (ε) transitions[cite: 1]
        eps_key = (current_node, 'ε')
        if eps_key in machine.transitions:
            for next_state in machine.transitions[eps_key]:
                agenda.append((next_state, tape_ptr))

        # 2. Explore symbol-consuming transitions[cite: 1]
        if tape_ptr < len(tape):
            sym_key = (current_node, tape[tape_ptr])
            if sym_key in machine.transitions:
                for next_state in machine.transitions[sym_key]:
                    agenda.append((next_state, tape_ptr + 1))

    return False

def compile_sheeptalk_nfsa():
    """
    Compiles the textbook NFSA for 'baa*!' into the internal data structure[cite: 1].
    """
    transitions = {
        (0, 'b'): [1],
        (1, 'a'): [2],
        (2, 'a'): [2, 3],  # Non-deterministic branch point[cite: 1]
        (3, '!'): [4]
    }
    return NFSA(states={0, 1, 2, 3, 4}, start_state=0, accept_states={4}, transitions=transitions)
