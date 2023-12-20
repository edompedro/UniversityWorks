#!/usr/bin/env python3

# USAGE:
# python3 compiler.py [input_file [output_file]]

import sys
from sly import Lexer, Parser

#################### LEXER ####################

class ÇLexer(Lexer):
    
    # token definitions
    literals = {';', '+', '-', '*', '/', '%', '(', ')', '{', '}', ',', '=', '[', ']'}
    tokens = {STDIO, INT, MAIN, PRINTF, STRING, NUMBER, NAME, IF, COMP, WHILE, VOID, RETURN}
    STDIO   = '#include <stdio.h>'
    INT     = 'int'
    MAIN    = 'main'
    PRINTF  = 'printf'
    IF      = 'if'
    WHILE   = 'while'
    VOID    = 'void'
    RETURN  = 'return'
    COMP    = r'(==|!=|>=|<=|<|>)'    
    STRING  = r'"[^"]*"'
    NUMBER  = r'\d+'
    NAME    = r'[a-z]+'

    # ignored characters and patterns
    ignore = r' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'//[^\n]*'

    # extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # error handling method
    def error(self, t):
        print(f"Illegal character '{t.value[0]}' in line {self.lineno}")
        self.index += 1

#################### PARSER ####################

class ÇParser(Parser):
    tokens = ÇLexer.tokens

    def __init__(self):
        self.if_counter = 0
        self.stack = []
        self.while_counter = 0
        self.whileStack = []
        self.variables_list = []
        self.array_counter = 0

    # error handling method
    def show_error(self, msg, line = None):
        if line:
            msg += ' in line ' + str(line)
        print('error: ', msg, file=sys.stderr)
        sys.exit(1)
        
    # ---------------- program ----------------

    @_('stdio functions')
    def program(self, p):
        print('\n# symbol_table: ', self.variables_list)

    @_('STDIO')
    def stdio(self, p):
        print('LOAD_CONST 0')
        print('LOAD_CONST None')
        print('IMPORT_NAME runtime')
        print('IMPORT_STAR')
        print()

    # ---------------- functions --------------

    @_('function functions')
    def functions(self, p):
        pass

    @_('main')
    def functions(self, p):
        pass

    @_('NAME  "(" parameters ")"')
    def function_name(self,p):
        print('.begin', p.NAME, p.parameters)
        if p.parameters != '':
            for i in range(len(p.parameters.split(' '))):
                self.variables_list.append(p.parameters.split()[i])
        # print(self.variables_list)

    @_('VOID function_name "{" statements "}"')
    def function(self, p):
        print('LOAD_CONST None')
        print('RETURN_VALUE')
        print('.end ')
        print('\n# symbol_table: ', self.variables_list)
        self.variables_list.clear()

    @_('INT function_name "{" statements "}"')
    def function(self, p):
        print('.end ')
        # print('LOAD_CONST None')
        # print('RETURN_VALUE')
        print('\n# symbol_table: ', self.variables_list)
        self.variables_list.clear()

    # ---------------- return ----------------
        
    @_('RETURN expression ";"')
    def return_st(self, p):
        print('RETURN_VALUE')

    # ---------------- parameters --------------

    @_('')
    def parameters(self, p):
        return ''

    @_('INT NAME')
    def parameters(self, p):
        return p.NAME

    @_('INT NAME "," parameters')
    def parameters(self, p):
        return p.NAME + ' ' + p.parameters

    # ---------------- main -------------------

    @_('INT MAIN "(" ")" "{" statements "}"')
    def main(self, p):
        print('LOAD_CONST None')
        print('RETURN_VALUE')  

    # ---------------- statements ----------------

    @_('statement statements')
    def statements(self, p):
        pass

    @_('')
    def statements(self, p):
        pass

    @_('function')
    def statements(self, p):
        pass

    # ---------------- statement ----------------

    @_('printf')
    def statement(self, p):
        print()

    @_('declaration')
    def statement(self, p):
        print()

    @_('attribution')
    def statement(self, p):
        print()
        
    @_('if_st')
    def statement(self, p):
        print()

    @_('while_st')
    def statement(self, p):
        print()

    @_('return_st')
    def statement(self, p):
        print()

    @_('call ";"')
    def statement(self, p):
        print()

    # ---------------- printf ----------------

    @_('STRING')
    def printf_format(self, p):
        print('LOAD_GLOBAL', 'print')
        print('LOAD_CONST', p.STRING)

    @_('PRINTF "(" printf_format "," expression ")" ";"')
    def printf(self, p):
        print('BINARY_MODULO')
        print('CALL_FUNCTION', 1)
        print('POP_TOP')

    # ---------------- call ----------------
        
    @_('NAME')
    def call_name(self, p):
        print('LOAD_NAME', p.NAME)

    @_('call_name "(" arguments ")" ')
    def call(self, p):
        # print('LOAD_FAST', p.NAME)
        print('CALL_FUNCTION', p.arguments)
        # print('POP_TOP')

    # ---------------- arguments ----------------

    @_('')
    def arguments(self, p):
        return 0

    @_('expression')
    def arguments(self, p):
        return 1

    @_('expression "," arguments')
    def arguments(self, p):
        return 1+p.arguments

    # ---------------- declaration ----------------
    
    @_('INT NAME "=" expression ";"')
    def declaration(self, p):
        if p.NAME in self.variables_list:
            self.show_error("variable already exist", p.lineno)
        else:
            print('STORE_FAST', p.NAME)
            self.variables_list.append(p.NAME)

    @_('INT NAME "[" "]" "=" "{" expressions "}" ";"')
    def declaration(self, p):
        if p.NAME in self.variables_list:
            self.show_error("variable already exist", p.lineno)
        else:
            print('BUILD_LIST', self.array_counter)
            print('STORE_FAST', p.NAME)
            self.variables_list.append(p.NAME)
            self.array_counter = 0
    
    # ---------------- declaration empty array ----------------

    @_('INT NAME "[" array_size expression "]" ";"')
    def declaration(self, p):
        if (p.NAME in self.variables_list):
            self.show_error(f"cannot redeclare variable '{p.NAME}'", p.lineno)
        self.variables_list.append(p.NAME)
        print('CALL_FUNCTION', 1)
        print('STORE_FAST', p.NAME)
    
    @_('')
    def array_size(self, p):
        print("LOAD_FAST array_zero")
    # ---------------- attribution ----------------

    @_('NAME "=" expression ";"')
    def attribution(self, p): 
        if p.NAME in self.variables_list:
            print('STORE_FAST', p.NAME)
        else:
            self.show_error(f"variable '{p.NAME}' not declared", p.lineno)

    @_('load_array "[" expression "]" "=" expression ";"') #add um load array no lugar do name que carregue o name e dps faz o resto e tira o load name daqui
    def attribution(self, p):
        # print('LOAD_FAST', p.NAME)
        print('ROT_THREE')
        print('STORE_SUBSCR')
       

    @_('NAME')
    def load_array(self, p):
        if p.NAME in self.variables_list:
            print('LOAD_FAST', p.NAME)
        else:
            self.show_error(f"variable '{p.NAME}' not declared", p.lineno)
  # ---------------- if_st ----------------

    @_('expression COMP expression')
    def if_comparison(self, p):
        print('COMPARE_OP', p.COMP)
        print(f'POP_JUMP_IF_FALSE', f'NOT_IF_{self.if_counter}')
        self.stack.append(self.if_counter)
        self.if_counter += 1

    @_('IF "(" if_comparison ")" "{" statements "}"')
    def if_st(self, p):
        print(f'NOT_IF_{self.stack.pop()}:')

    # ---------------- while_st ----------------

    @_('expression COMP expression')
    def while_comparison(self, p):
        print('COMPARE_OP', p.COMP)
        print(f'POP_JUMP_IF_FALSE', f'NOT_WHILE_{self.while_counter}')
        self.whileStack.append(self.while_counter)
        self.while_counter += 1
    
    @_('while_begin "(" while_comparison ")" "{" statements "}"')
    def while_st(self, p):
        valuePoped = self.whileStack.pop()
        print(f'JUMP_ABSOLUTE', f'WHILE_{valuePoped}')
        print(f'NOT_WHILE_{valuePoped}:')

    @_('WHILE')
    def while_begin(self, p):
        print(f'WHILE_{self.while_counter}:')
        # self.while_counter += 1

    # ---------------- expression ----------------

    @_('expression "+" term')
    def expression(self, p):
        print('BINARY_ADD')

    @_('expression "-" term')
    def expression(self, p):
        print('BINARY_SUBTRACT')

    @_('term')
    def expression(self, p):
        pass

    # ---------------- expressions ----------------

    @_('expressions "," expression')
    def expressions(self, p):
        self.array_counter += 1

    @_('expression')
    def expressions(self, p):
        self.array_counter += 1

    # ---------------- term ----------------

    @_('term "*" factor')
    def term(self, p):
        print('BINARY_MULTIPLY')

    @_('term "%" factor')
    def term(self, p):
        print('BINARY_MODULO')

    @_('term "/" factor')
    def term(self, p):
        print('BINARY_FLOOR_DIVIDE')

    @_('factor')
    def term(self, p):
        pass

    # ---------------- factor ----------------

    @_('NUMBER')
    def factor(self, p):
        print('LOAD_CONST', p.NUMBER)

    @_('"(" expression ")"')
    def factor(self, p):
        pass

    @_('NAME')
    def factor(self, p):
        if p.NAME not in self.variables_list:
            self.show_error(f"Variable '{p.NAME}' unknown", p.lineno)
        else:
            print('LOAD_FAST', p.NAME)

    @_('load_array "[" expression "]"')
    def factor(self, p):
        # if p.NAME not in self.variables_list:
        #     self.show_error(f"Variable '{p.NAME}' unknown", p.lineno)
        # else:
        #     print('LOAD_FAST', p.NAME)
        print('BINARY_SUBSCR')

    @_('call')
    def factor(self, p):
        pass

#################### MAIN ####################

lexer = ÇLexer()
parser = ÇParser()

if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1], 'r')
    
    if len(sys.argv) > 2:
        sys.stdout = open(sys.argv[2], 'w')

text = sys.stdin.read()
parser.parse(lexer.tokenize(text))
