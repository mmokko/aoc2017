import operator
from day8_input import INPUT


VALID_COMMAND_LEN = 7

COMMAND_REGISTER_IDX = 0
COMMAND_OPERATOR_IDX = 1
COMMAND_VALUE_IDX = 2
COMMAND_IF_IDX = 3
COMMAND_COND1_IDX = 0
COMMAND_COND2_IDX = 1
COMMAND_COND3_IDX = 2


class Register(object):
    def __init__(self, name):
        self.name = name
        self.value = 0


class RegisterIterator(object):
    def __init__(self):
        self._registers = list()

    def __iter__(self):
        for register in self._registers:
            yield register

    def __getitem__(self, name):
        if name not in [register.name for register in self._registers]:
            self.append(Register(name))
        for register in self._registers:
            if name == register.name:
                return register

    def append(self, register):
        self._registers.append(register)


class OperatorFactory(object):
    @staticmethod
    def get_operator(op):
        if op == 'inc':
            return operator.add
        elif op == 'dec':
            return operator.sub


class ConditionOperatorFactory(object):
    @staticmethod
    def get_operator(op):
        if op == '>':
            return operator.gt
        elif op == '<':
            return operator.lt
        elif op == '>=':
            return operator.ge
        elif op == '==':
            return operator.eq
        elif op == '<=':
            return operator.le
        elif op == '!=':
            return operator.ne


class Condition(object):
    def __init__(self, condition_line, registers):
        condition = condition_line.split()
        self._register = registers[condition[COMMAND_COND1_IDX]]
        self._condition = ConditionOperatorFactory.get_operator(condition[COMMAND_COND2_IDX])
        self._value = int(condition[COMMAND_COND3_IDX])

    def is_true(self):
        if self._condition(self._register.value, self._value):
            return True
        return False


class Command(object):
    def __init__(self, command_line, registers):
        self._operator = None
        parameters = command_line.split()
        if len(parameters) == VALID_COMMAND_LEN and parameters[COMMAND_IF_IDX] == 'if':
            (command, condition) = command_line.split('if')
            self._create_command(command, registers)
            self._condition = Condition(condition, registers)

    def _create_command(self, command_line, registers):
        command = command_line.split()
        self.register = registers[command[COMMAND_REGISTER_IDX]]
        self._operator = OperatorFactory.get_operator(command[COMMAND_OPERATOR_IDX])
        self._value = int(command[COMMAND_VALUE_IDX])

    def execute(self):
        if self._condition.is_true():
            self.register.value = self._operator(self.register.value, self._value)


class RegisterCalculator(object):
    def __init__(self, commands):
        self.registers = RegisterIterator()
        self._commands = list()
        self._parse_commands(commands)
        self.highest_value = 0

    def _parse_commands(self, commands):
        for command_line in commands.split('\n'):
            self._commands.append(Command(command_line, self.registers))

    def execute_commands(self):
        for command in self._commands:
            command.execute()
            if command.register.value > self.highest_value:
                self.highest_value = command.register.value


def main():
    regCalc = RegisterCalculator(INPUT)
    regCalc.execute_commands()
    registers = sorted(regCalc.registers, key=lambda x:x.value, reverse=True)
    print(registers[0].value)
    print(regCalc.highest_value)


if __name__=='__main__':
    main()