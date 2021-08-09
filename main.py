import os

def litteral_to_clause(litteral):
    ''' Cette fonction transforme un litteral en clause '''
    clause = litteral +" 0"
    return clause

def negation_of_litteral(litteral):
    ''' Cette fonction donne la négation du littéral introduit'''
    negation="-"+litteral
    return negation

def read_BC(path):
    with open(path,'r') as file:
        lines=file.readlines()
    for line in lines:
        print(line)
def add_clause_to_BC(path,clause):
    ''' Cette fonction ajoute une clause à la BC'''

    created_path=r"C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\new.cnf"
    with open(created_path,'w') as new_file:
        with open(path,'r') as file:
            lines = file.readlines()
            lines.append(clause)
            line1 = lines[0].split() #premier est la liste des élément de la première ligne de format p cnf nbr_var nbr_clauses
            new_nbr_clause= int(line1[-1]) +1#metter a jour nombre de clauses
            line1[-1]=new_nbr_clause
            print("Nombre de clause dans la BC:"+str(new_nbr_clause-1))
            print("Nombre de clause dans la BC après ajout 7But: "+str(new_nbr_clause))
            new_line1=line1[0]
            for elt in line1[1:]:
                new_line1=new_line1+" "+str(elt)
            lines[0]=new_line1
            content=lines[0]
            for line in lines[1:]:
                content=content+"\n"+line
            new_file.write(content)
            new_file.close()

def solve_BC(path):
    ''' Cette fonction fait appel au solveur sat afin de vérifier la satisfiabilité d'une BC'''
    CNF=(path.split())[-1]
    #CNF='example1.cnf'
    os.system('ubcsat -alg saps -i '+CNF+' -solve > fiche')
    result=open('fiche','r').read()
    if("# Solution found for -target 0"in result):
        return True
    elif("# No Solution found for -target 0"in result):
     return False


def test_inference(path,litteral):

    n_litteral=negation_of_litteral(litteral)
    clause=litteral_to_clause(n_litteral)
    add_clause_to_BC(path,clause)
    new_path=r"C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\new.cnf"
    if(solve_BC(new_path)):
        print("BC n'infere pas le litteral")
    else:
        print("BC infere  le litteral")



litteral = input('enter but:')

#path =r'C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\example1.cnf'
path =r'C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\ocean2.cnf'

test_inference(path,litteral)







#print(solve_BC(path))
#read_BC(r"C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\fiche.txt")
#add_clause_to_BC(path,clause)
#new_path=r"C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\new.cnf"
#read_BC(new_path)
#path = r'C:\Users\Dell\OneDrive\Bureau\LKSC\USTHB\S8\RC\UBCSAT\exemple1.cnf'
#add_clause_to_BC(path,clause)