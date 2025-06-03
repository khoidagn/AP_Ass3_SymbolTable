from StaticError import *
from Symbol import *
from functools import *


def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.

    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """
    initial_scope = {'scope_level': 0, 'symbols': [], 'parent': None}
    initial_state = ([initial_scope], initial_scope, [], [])

    def is_valid_identifier(name):
        return name and name[0].islower() and reduce(lambda acc, c: acc and (c.isalnum() or c == '_'), name, True)
    def is_number(value):
        return value.isdigit()
    def is_string(value):
        return (
            len(value) >= 2 and
            value[0] == "'" and
            value[-1] == "'" and
            reduce(lambda acc, c: acc and c.isalnum(), value[1:-1], True)
        )
    def find_symbol(name, scope):
        return (
            lambda found: found if found 
            else (
                find_symbol(name, scope['parent']) if scope['parent'] else None))(
            next(filter(lambda s: s['name'] == name, reversed(scope['symbols'])), None)
        )
    def get_symbol_type(value, current_scope):
        if is_number(value):
            return 'number'
        if is_string(value):
            return 'string'
        sym = find_symbol(value, current_scope)
        return sym['type'] if sym else None
    def collect_symbols(scope):
        return [] if not scope else collect_symbols(scope['parent']) + scope['symbols']
    def visible_symbols(scope):
        collected = list(reversed(collect_symbols(scope)))
        def reducer(acc, sym):
            names = list(map(lambda s: s['name'], acc))
            return acc if sym['name'] in names else acc + [sym]
        return list(reversed(reduce(reducer, collected, [])))
    def visible_symbols_reverse(scope):
        collected_reverse = list(reversed(collect_symbols(scope)))
        def reducer(acc, sym):
            return acc if sym['name'] in list(map(lambda s: s['name'], acc)) else acc + [sym]
        return reduce(reducer, collected_reverse, [])

    def process(state, cmd):
        symbol_table, current_scope, output, open_blocks = state
        if not cmd.strip():
            raise InvalidInstruction("Invalid command")
        if cmd.startswith(' '):
            raise InvalidInstruction("Invalid command")
        parts = cmd.strip().split()

        instruction = parts[0]
        if instruction not in ('INSERT', 'ASSIGN', 'BEGIN', 'END', 'LOOKUP', 'PRINT', 'RPRINT'):
            raise InvalidInstruction("Invalid command")       
        
        if ' '.join(parts) != cmd:
            raise InvalidInstruction(cmd)

        if instruction == 'INSERT':
            if len(parts) != 3 or not is_valid_identifier(parts[1]) or parts[2] not in ('number', 'string'):
                raise InvalidInstruction(cmd)
            if any(map(lambda s: s['name'] == parts[1], current_scope['symbols'])):
                raise Redeclared(cmd)
            new_symbol = {'name': parts[1], 'type': parts[2], 'scope_level': current_scope['scope_level']}
            new_current_scope = {
                'scope_level': current_scope['scope_level'],
                'symbols': current_scope['symbols'] + [new_symbol],
                'parent': current_scope['parent']
            }
            return (symbol_table[:-1] + [new_current_scope], new_current_scope, output + ['success'], open_blocks)
        
        elif instruction == 'ASSIGN':
            if len(parts) != 3 or not is_valid_identifier(parts[1]):
                raise InvalidInstruction(cmd)
            if not is_number(parts[2]) and not is_string(parts[2]) and not is_valid_identifier(parts[2]):
                raise InvalidInstruction(cmd)
            var_symbol_assign = find_symbol(parts[1], current_scope)
            if not var_symbol_assign:
                raise Undeclared(cmd)
            value_type = get_symbol_type(parts[2], current_scope)
            if not value_type:
                raise Undeclared(cmd)
            if var_symbol_assign['type'] != value_type:
                raise TypeMismatch(cmd)
            return (symbol_table, current_scope, output + ['success'], open_blocks)
        
        elif cmd == 'BEGIN':
            new_scope = {
                'scope_level': current_scope['scope_level'] + 1,
                'symbols': [],
                'parent': current_scope
            }
            return (symbol_table + [new_scope], new_scope, output, open_blocks + [new_scope['scope_level']])

        elif cmd == 'END':
            if not open_blocks:
                raise UnknownBlock()
            return (symbol_table, current_scope['parent'], output, open_blocks[:-1])
        
        elif instruction == 'LOOKUP':
            if len(parts) != 2 or not is_valid_identifier(parts[1]):
                raise InvalidInstruction(cmd)
            var_symbol_lookup = find_symbol(parts[1], current_scope)
            if not var_symbol_lookup:
                raise Undeclared(cmd)
            return (symbol_table, current_scope, output +[str(var_symbol_lookup['scope_level'])], open_blocks)

        elif cmd == 'PRINT':
            symbols_print = visible_symbols(current_scope)
            line_print = ' '.join(map(lambda s: f"{s['name']}//{s['scope_level']}", symbols_print))
            return (symbol_table, current_scope, output + [line_print], open_blocks)
        elif cmd == 'RPRINT':
            symbols_rprint = visible_symbols_reverse(current_scope)
            line_rprint = ' '.join(map(lambda s: f"{s['name']}//{s['scope_level']}", symbols_rprint))
            return (symbol_table, current_scope, output + [line_rprint], open_blocks)


        else:
            raise InvalidInstruction(cmd)


    try:
        final_symbol_table, final_current_scope, final_output, final_open_blocks = reduce(
            process, list_of_commands, initial_state
        )
    except StaticError as e:
            return [str(e)]
    if final_open_blocks:
        raise UnclosedBlock(final_open_blocks[-1])
    return final_output + ([f"UnclosedBlock: {final_open_blocks[-1]}"] if final_open_blocks else [])