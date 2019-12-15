# Solve_formula_set
  This python packages allow you to calculate variables given multiple formulas and constants.
## Usage
### Installation
  ```console
  pip3 install -r requirements.txt
  python3 formula_set.py
  ```
### Command line usage
command line usage
   -   quit()         leave the command line prompt
   -   init [name]    initializa a new formula set
   -   delete [name]   delete a formula set
   -   list           list all formula set existed
   -   set [name] [op] [arg1] , [arg2] ....
            op:  +f  (add formula)   ex  set A +f 1 = 3 , 2 = 4 * a
                 +v  (add value)     ex  set A +v a 2 , b 4 , c 7
                 see (see variable)  ex set A see a , b , c
                 see_all (see all variable)  ex set A see_all
                 reset (reset all)   ex set A reset
                 resetf (reset all formulas)  ex set A resetf
                 resetv (reset all variables)  ex set A resetv
                 delf (delete formulas)  ex set A delf  1 , 3 , 4   // waiting for implementation
                 delv (delete values) ex  set A delv 1 , 5 , 7    // waiting for implementation
