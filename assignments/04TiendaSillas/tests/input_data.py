# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["1", "5"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 25.0"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    (
        ["1", "15.5"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 240.25"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    
     (
        ["2", "99.9", "33.9"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 3386.61"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    
    (
        ["2", "10", "20"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 200.0"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    
    (
        ["3", "3", "25","26"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 36.0"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
     (
        ["3", "3", "25","26"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 36.0"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    
    (
        ["3", "10", "12","15"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 59.81168364124187"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
     (
        ["3", "10", "20","25"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "area = 94.99177595981665"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    
(
        ["4"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "Adios"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    (
        ["0"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "Opcion incorrecta"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
     (
        ["-1"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "Opcion incorrecta"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    ),
    (
        ["100"],
        ["""Area del
1. Cuadrado
2. Rectangulo
3. Triangulo
4. Salir
Teclea la opcion: """,
         "Opcion incorrecta"],
        '''
        revisa que si leiste los valores como flotantes, 
        revisa si la funcion regresa valor
        '''
    )
    
]
