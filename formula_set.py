# update is_solvable
from sympy.solvers import solve
from sympy import Symbol
SYMBOL = {"+", "-", "*", "\\", "=", "**", "^", "(", ")"}

class Formula_set:
    variable = dict()   # key value pair variable: value(default None)
    formula = []     # a list of class Formula
    
    def __init__(self, *formulas: str):
        variable = set()
        for f in formulas:
            self.formula.append(Formula(f))            
            variable = variable.union(self.formula[-1].arg_required)
        self.variable = dict.fromkeys(variable, None)  
        
    def is_solvable(self, formula)->bool:
        unknown_var = 0
        for i in formula.arg_required:
            if self.variable[i] == None:
                unknown_var += 1
        return unknown_var == 1
    
    def solve(self):
        while True:
            old_unknown_var = len([k for k, v in self.variable.items() if v == None])
            for f in self.formula:
                if self.is_solvable(f):
                    var = f.arg_required.pop()
                    self.variable[var] = solve(f.modify_content, Symbol(var))[0] # assume only one solution
                    self.update_variable(var)
            new_unkwown_var = len([k for k, v in self.variable.items() if v == None])
            if old_unknown_var == new_unkwown_var:
                break

    def update_variable(self, var: str):
        for f in self.formula:
            try:
                f.arg_required.remove(var)
                f.modify_content = f.modify_content.replace(var, str(self.variable[var]))
            except KeyError:
                pass
    
    def display(self):
        print("Variable:")
        for var in self.variable:
            print(var, end=' ')
        print("")
        
        print("Formula")
        for f in self.formula:
            print(f.content)
    
    def debug_display(self):
        print("Variable:")
        for var in self.variable:
            print(var, end=' ')
        print("")
        
        print("Formula")
        for f in self.formula:
            print(f.content, end=' ')
            print(self.is_solvable(f))

# a class with content(formula), arg_required
class Formula:
    content = ""
    modify_content = ""
    arg_required = set()    # the variable remain for this formula
    
    def __init__(self, content):
        self.content = content 
        self.arg_required =  set()
        for element in content.split():
            if element not in SYMBOL and not is_double(element):
                self.arg_required.add(element)
        self.modify_content = self.content.replace('=', '- (')
        self.modify_content += ' )'

        
def main():
    formula_set = Formula_set("b - 26 = 4 * 3 + 6 * 2", "c = b + 2", "a = c + b", "d = 3")
    formula_set.solve()
    print(formula_set.variable['a'])
    print(formula_set.variable['b'])
    print(formula_set.variable['c'])
    print(formula_set.variable['d'])
 
###############################################################
# helper function   
def is_double(s: str)->bool:
    try:
        float(s)
    except ValueError:
        return 0
    return 1
        
    

if __name__ == "__main__":
    main()