
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
        return unknown_var < 2
    
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
    arg_required = set()
    
    def __init__(self, content):
        self.content = content 
        self.arg_required =  set()
        for element in content.split():
            if element not in SYMBOL and not is_double(element):
                self.arg_required.add(element)

def main():
    formula_set = Formula_set("a = b + c", "b = ( d + e )", "a = a - c", " 1 = 1 ", " b = 3", "c = 4")
    formula_set.debug_display()
 
 
    
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