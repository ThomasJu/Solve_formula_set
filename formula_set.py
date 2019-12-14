#!/usr/bin/env python3
# update is_solvable
# upgrade TODO
# update README
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

# command line usage
#   0   quit()         leave the command line prompt
#   1   init [name]    initializa a new formula set
#   2   delete [name]   delete a formula set
#   3   list           list all formula set existed
#   4   set [name] [op] [arg1] , [arg2] ....
#            op:  +f  (add formula)   ex  set A +f 1 = 3 , 2 = 4 * a
#                 +v  (add value)     ex  set A +v a 2 , b 4 , c 7
#                 see (see variable)  ex set A see a , b , c
#                 see_all (see all variable)  ex set A see_all
#                 reset (reset all)   ex set A reset
#                 resetf (reset all formulas)  ex set A resetf
#                 resetv (reset all variables)  ex set A resetv
#                 delf (delete formulas)  ex set A delf  1 , 3 , 4  # TODO:  Haven't implemented shoudl wait for class implementation
#                 delv (delete values) ex  set A delv 1 , 5 , 7  # TODO:  Haven't implemented shoudl wait for class implementation
def main():
    formula_sets = dict()
    setoperation("set A reset 1 = 1 , 2 = 4 , x ** 2 + x * 2 = a", Formula_set())
    while True:
        inputline = input("formula set> ")
        command = inputline.split()[0]
        if command == "quit()":
            break
        #  1 
        if command == "init":
            name = inputline.split()[1]
            if name in formula_sets:
                print("This name has already existed, please delete before reinitialize")
            else:
                formula_sets[name] = Formula_set()
                print(f"Formula set {name} initialized")  
        #  2  
        if command == "delete":
            name = inputline.split()[1]
            if name in formula_sets:
                formula_sets.pop(name)
                print(f"Formula set {name} deleted")
            else:
                print("This name doesn't exist in formula sets")
        #  3
        if command == "list":
            print("Formula set existed: ", end="")
            for key in formula_sets:
                print(f"{key}", end=" ")
            print("")
        #  4 
        if command == "set":
            name = inputline.split()[1]
            if name not in formula_sets:
                print(f"Formula set {name} not existed")
            else:
                formula_sets[name] = setoperation(inputline, formula_sets[name])
        #  5
        if command == "help":
            print_help()
        print("=====================================")     
###############################################################
# command line usage
#   0   quit()         leave the command line prompt
#   1   init [name]    initializa a new formula set
#   2   delete [name]   delete a formula set
#   3   list           list all formula set existed
#   4   set [name] [op] [arg1] , [arg2] ....
#            op:  +f  (add formula)   ex  set A +f 1 = 3 , 2 = 4 * a
#                 +v  (add value)     ex  set A +v a 2 , b 4 , c 7
#                 see (see variable)  ex set A see a , b , c
#                 see_all (see all variable)  ex set A see_all
#                 reset (reset all)   ex set A reset
#                 resetf (reset all formulas)  ex set A resetf
#                 resetv (reset all variables)  ex set A resetv
#                 delf (delete formulas)  ex set A delf  1 , 3 , 4  # TODO:  Haven't implemented shoudl wait for class implementation
#                 delv (delete values) ex  set A delv 1 , 5 , 7  # TODO:  Haven't implemented shoudl wait for class implementation

# helper function
#  TODO: error handling   
def setoperation(line: str, fs: Formula_set)->Formula_set:
    op = line.split()[2]
    ##############################
    # argument processing
    argv = []
    s = ""
    for arg in line.split()[3:]:
        if arg == ',':
            argv.append(s)
            s = ""
        else:
            s += " " + arg
    argv.append(s)
    ###############################       
    if op == "+f":
        fs.add_formula(argv)
    elif op == "+v":
        variabletuple = []
        for arg in argv:
            variabletuple.append((arg.split()[0], arg.split()[1]))
        fs.add_variable(variabletuple)
    elif op == "see":
        for arg in argv:
            print(f"{arg}: {fs.see(arg)}")
    elif op == "see_all":
        for key, value in fs.variable.items():
            print(f"{key}: {value}")
    elif op == "reset":
        fs.clear_formulas()
        fs.clear_variable()
    elif op == "resetf":
        fs.clear_formulas()
    elif op == "resetv":
        fs.clear_variable()
    elif op == "delf":
        pass
    elif op == "delv":
        pass  
    else:
        print("Invalid op, use help to see all available op")
    return fs


def print_help():
    print(
''' 
=====================================
command line usage
0   quit()         leave the command line prompt
1   init [name]    initializa a new formula set
2   delete [name]   delete a formula set
3   list           list all formula set existed
4   set [name] [op] [arg1] , [arg2] ....
        op: +f  (add formula)   ex  set A +f 1 = 3 , 2 = 4 * a
            +v  (add value)     ex  set A +v a 2 , b 4 , c 7
            see (see variable)  ex set A see a , b , c
            see_all (see all variable)  ex set A see_all
            reset (reset all)   ex set A reset
            resetf (reset all formulas)  ex set A resetf
            resetv (reset all variables)  ex set A resetv
            delf (delete formulas)  ex set A delf  1 , 3 , 4  *** Waiting Implementation
            delv (delete values) ex  set A delv 1 , 5 , 7  *** Waiting Implemenation
            '''
    )

def is_double(s: str)->bool:
    try:
        float(s)
        return True
    except ValueError:
        return False      
    

if __name__ == "__main__":
    main()