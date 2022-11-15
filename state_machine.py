from typing import Callable

class StateMachine:

    #region Functions
    def __init__(self):
        '''
        Initializes the StateMachine class.
        '''
        self.states             = {}
        self.actions            = {}
        self.transition_table   = {}
        self.current_state      = None
    
    def add_state(self, name: str, action: Callable, initial: bool = False) -> None:
        '''
        Adds a new State.
        '''
        if name not in self.states:
            self.states[name] = self.State(name, action)
            if initial:
                self.current_state = self.states[name]
        else:
            print(f'Already have the State {name}')

    def add_action(self, name: str) -> None:
        '''
        Adds a new Action.
        '''
        if name not in self.actions:
            self.actions[name] = self.Action(name)
        else:
            print(f'Already have the Action {name}.')

    def perform_action(self, state: object):
        '''
        Carries out the embedded function of the given State.
        '''
        if type(state) == self.State:
            state.action()

    def transition(self, action: object) -> None:
        '''
        Transitions between two States, given some Action and the TransitionTable class.
        '''
        current_state = self.current_state
        transitioned_state = self.transition_table.get(action, None)

        if not transitioned_state:
            print('Not a valid transition given the current state.')
        else:
            self.current_state = transitioned_state
            self.perform_action(transitioned_state) 
    #endregion
    
    #region Nested Classes
    class State:
        def __init__(self, name: str, action: Callable) -> None:
            '''
            Initializes a State.
            '''
            self.name = name
            self.action = action
    
    class Action:
        def __init__(self, name: str) -> None:
            '''
            Initializes an action.
            '''
            self.name = name

    class TransitionTable:
        def __init__(self, state: object, action: object):
            '''
            Initializes a new TransitionTable.
            '''
            self.transition_table[action, state]
    #endregion

if __name__ == '__main__':

    def print_hello():
        print('Hello')

    state_machine = StateMachine()

    state_machine.add_state('Initialization', print_hello, True)

    state_machine.perform_action(state_machine.current_state)
