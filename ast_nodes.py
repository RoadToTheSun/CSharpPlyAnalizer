from abc import ABC, abstractmethod
from typing import Callable, Tuple
from enum import Enum


class AstNode(ABC):
    @property
    def childs(self)->Tuple['AstNode', ...]:
        return ()

    def add_child(self, *ch):
        self.childs+=ch

    @abstractmethod
    def __str__(self)->str:
        pass

    @property
    def tree(self)->[str, ...]:
        res = [str(self)]
        childs = self.childs
        for i, child in enumerate(childs):
            ch0, ch = '├', '│'
            if i == len(childs) - 1:
                ch0, ch = '└', ' '
            res.extend(((ch0 if j == 0 else ch) + ' ' + s for j, s in enumerate(child.tree)))
        return res

    def visit(self, func: Callable[['AstNode'], None])->None:
        func(self)
        map(func, self.childs)

    def __getitem__(self, index):
        return self.childs[index] if index < len(self.childs) else None


class ValueNode(AstNode):
    pass


class NumNode(ValueNode):
    def __init__(self, num: float):
        super().__init__()
        self.num = float(num)

    def __str__(self)->str:
        return str(self.num)


class IdentNode(ValueNode):
    def __init__(self, name: str):
        super().__init__()
        self.name = str(name)

    def __str__(self)->str:
        return str(self.name)


class BoolValueNode(ValueNode):
    def __init__(self, name: str):
        super().__init__()
        self.name = str(name)

    def __str__(self)->str:
        return str(self.name)


class BinOp(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    GE = '>='
    LE = '<='
    NOTQUALS = '!='
    EQUALS = '=='
    GT = '>'
    LT = '<'
    BIT_OR = '|'
    BIR_AND = '&'


class BinOpNode(ValueNode):
    def __init__(self, op: BinOp, arg1: ValueNode, arg2: ValueNode):
        super().__init__()
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    @property
    def childs(self) -> Tuple[ValueNode, ValueNode]:
        return self.arg1, self.arg2

    def __str__(self)->str:
        return str(self.op.value)


class UnOp(Enum):
    NOT = '!'
    SUB = '-'


class UnOpNode(ValueNode):
    def __init__(self, op: UnOp, arg: ValueNode):
        super().__init__()
        self.op = op
        self.arg = arg

    @property
    def childs(self) -> Tuple[ValueNode]:
        return self.arg,

    def __str__(self)->str:
        return str(self.op.value)


class ExprListNode(AstNode):
    def __init__(self, *exprs: AstNode):
        super().__init__()
        self.exprs = exprs

    @property
    def childs(self) -> Tuple[AstNode]:
        return self.exprs

    def add_child(self, ch):
        self.exprs = self.exprs + (ch,)

    def __str__(self)->str:
        return '...'


class AssignNode(ValueNode):
    def __init__(self, var: IdentNode, val: ValueNode):
        super().__init__()
        self.var = var
        self.val = val

    @property
    def childs(self) -> Tuple[IdentNode, ValueNode]:
        return self.var, self.val

    def __str__(self)->str:
        return '='


class OutputNode(AstNode):
    def __init__(self, arg: ValueNode):
        self.arg = arg

    @property
    def childs(self) -> Tuple[ValueNode]:
        return self.arg,

    def __str__(self)->str:
        return 'cout'


class InputNode(AstNode):
    def __init__(self, var: IdentNode):
        self.var = var

    @property
    def childs(self) -> Tuple[IdentNode]:
        return self.var,

    def __str__(self)->str:
        return 'cin'


class IfNode(AstNode):
    def __init__(self, cond: ValueNode, then_: AstNode, else_: AstNode = None):
        self.cond = cond
        self.then_ = then_
        self.else_ = else_

    @property
    def childs(self) -> Tuple[ValueNode]:
        res = [self.cond, self.then_]
        if self.else_:
            res.append(self.else_)
        return res

    def __str__(self)->str:
        return 'if'

class ForNode(AstNode):
    def __init__(self, init: AstNode, cond: ValueNode, step: AstNode, body: AstNode):
        self.init = init
        self.cond = cond
        self.step = step
        self.body = body

    @property
    def childs(self) -> Tuple[ValueNode]:
        return self.init, self.cond, self.step, self.body

    def __str__(self)->str:
        return 'for'

class ModifiersNode(AstNode):
    def __init__(self, *modifiers: IdentNode):
        self.modifiers = modifiers

    @property
    def childs(self) -> Tuple[IdentNode]:
        return self.modifiers

    def add_child(self, *mod):
        self.modifiers += (mod, )

    def __str__(self)->str:
        return 'modifiers'


class ClassNode(AstNode):
    def __init__(self, modifiers: ModifiersNode, name: IdentNode, body: AstNode):
        self.modifiers = modifiers
        self.name = name
        self.body = body

    @property
    def childs(self):
        return self.name, self.modifiers, self.body

    def __str__(self)->str:
        return 'class ' + self.name.name + ' declaration'



class WhileNode(AstNode):
    def __init__(self, cond: ValueNode, body: AstNode):
        self.cond = cond
        self.body = body

    @property
    def childs(self) -> Tuple[ValueNode]:
        return self.cond, self.body

    def __str__(self)->str:
        return 'while'


class DoWhileNode(AstNode):
    def __init__(self, body: AstNode, cond: ValueNode):
        self.body = body
        self.cond = cond

    @property
    def childs(self) -> Tuple[ValueNode]:
        return self.body, self.cond

    def __str__(self)->str:
        return 'do while'


class IdentificationNode(AstNode):
    def __init__(self, type_: str, name: ValueNode, value: ValueNode = None):
        self.type_ = type_
        self.name = name
        self.value = value

    @property
    def childs(self) -> Tuple[ValueNode]:
        res = [self.name, ]
        if self.value:
            res.append(self.value)
        return res

    def __str__(self)->str:
        return str(self.type_)
