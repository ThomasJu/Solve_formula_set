#!/usr/bin/env python3
# update is_solvable
from sympy.solvers import solve
from sympy import Symbol
import readline
SYMBOL = {"+", "-", "*", "\\", "=", "**", "^", "(", ")"}

class Formula_set:
    variable = dict()   # key value pair variable: value(default None)
    formula = []     # a list of class Formula
    
    def __init__(self, *formulas: str):
        for f in formulas:
            self.add_formula(f)
        
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
    
    #  User Interface
    #  1  add formula in a list to this formula set 
    def add_formula(self, formulas: list, need_solve=True):
        for f in formulas:
            if f not in self.formula:
                self.formula.append(Formula(f))
                for var in self.formula[-1].arg_required:
                    self.variable.setdefault(var)
        if need_solve:
            self.solve()
    #  2  add value to a corresponded variable (list of tuple)
    def add_variable(self, variables: list, need_solve=True):
        for var in variables:
            self.variable.setdefault(var[0], var[1])
        if need_solve:
            self.solve
    #  3  clear all values in variable
    def clear_variable(self):
        self.variable = self.variable.fromkeys(self.variable, None)
    #  4  clear all formulas in formulas
    def clear_formulas(self):
        self.formula = list()
    #  5  see the corresponded value of a variable 
    #     return None if it's still undefined or not existed
    def see(self, var: str)->float:
        try:
            return self.variable[var]
        except KeyError:
            return None
        
        

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
    while True:
        inputline = input("formula set> ")
        if inputline == "quit()":
            break
        #  command line waiting to implement
 
###############################################################
# helper function   
def is_double(s: str)->bool:
    try:
        float(s)
        return True
    except ValueError:
        return False      
    

if __name__ == "__main__":
    main()