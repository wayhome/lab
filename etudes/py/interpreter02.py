# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MUNUS', 'EOF'


class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type,
                                               value=repr(self.value)
                                               )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time
        """
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)
        current_char = text[self.pos]
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        if current_char.isspace():
            self.pos += 1
            return self.get_next_token()

        self.error()

    def eat(self, *token_type):
        if self.current_token.type in token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def read_integer(self):
        result = ''
        while self.current_token.type == INTEGER:
            token = self.current_token
            self.eat(INTEGER)
            result += str(token.value)
        return int(result)

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.read_integer()

        op = self.current_token
        self.eat(PLUS, MINUS)

        right = self.read_integer()

        if op.type == PLUS:
            result = left + right
        else:
            result = left - right

        return result


def main():
    while True:
        try:
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
