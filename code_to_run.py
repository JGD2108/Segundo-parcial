from Paquete.Cpu import Cpu
from Paquete.user import User
if __name__ == '__main__':
    points=0
    list = []
    try:
        usuarios = input("Cuantos usuarios participan?")
    except ValueError:
        print("Escriba un numero")
    usuarios = int(usuarios)
    for a in range (usuarios):
        name = input("Digite su nombre")
        user = User(points)
        user.name = name
        list.append(user)
    for a in list:
        print(f"Comienzas{a.name}")
        cpu = Cpu(points)
        turnos=0
        while turnos<3:
            opc1 = input("Escoja 1.Defender, 2. Atacar")
            opc2 = input("Escoja 1. Low, 2.Mid, 3.High")
            opc1=int(opc1)
            opc2=int(opc2)
            if opc1==1:
                if opc2==1:
                    x=1
                    s=0
                    a.attack=s
                    a.defense=x
                elif opc2==2:
                    x=2
                    s=0
                    a.attack=s
                    a.defense=x
                elif opc2==3:
                    x=3
                    s=0
                    a.attack=s
                    a.defense=x
            else: 
                if opc2==1:
                    x=1
                    s=0
                    a.attack=x
                    a.defense=0
                elif opc2==2:
                    x=2
                    s=0
                    a.attack= x
                    a.defense=s
                elif opc2==3:
                    x=3
                    s=0
                    a.attack=x
                    a.defense=0
            cpu.Escoger()
            print(cpu.attack)
            print(cpu.defense)
            print(a.attack)
            print(a.defense)
            ## 2 defienden
            if a.attack==0 and cpu.attack==0:
                    print("Tie")
                    x=a.points+1
                    a.points= x
                    x= cpu.points+1
                    cpu.points=x
            
            ## Los 2 atacan en un lugar valido
            if a.attack!=0 and cpu.attack!=0:
                print("Both score")
                x = a.points+3
                a.points = x
                b = cpu.points+3
                cpu.points=b
            ##Cpu ataco bien
            while a.defense!=0 and cpu.attack!=0:
                if cpu.attack!=a.defense:
                    print("Cpu wins")
                    b= cpu.points+3
                    cpu.points=b
                if cpu.attack==a.defense:
                    print("Tie")
                    x= a.points+1
                    a.points=x
                    b= cpu.points+1
                    cpu.points=b
                break
            ##User ataco bien
            while a.attack!=0 and cpu.defense!=0:
                if cpu.defense!=a.attack:
                    print("User wins")
                    x= a.points+3
                    a.points=x
                if cpu.defense==a.attack:
                    print("Tie")
                    x= a.points+1
                    a.points=x
                    b= cpu.points+1
                    cpu.points=b
                break
            turnos+=1
        print(a.points)
        print(cpu.points)
    print("LeaderBoard")
    x=1
    mayor = 0
    n = []
    while x<=usuarios:
        for i in list:
            if i.points>mayor:
                pos = i.name
                mayor = i.points
        n.append(pos)
        x=x+1
    print(n)
    