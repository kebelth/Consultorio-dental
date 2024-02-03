print("Bienvenidos al consultorio Dental")
nombre=0
Citas_Mes=[ "libre" , "libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre","libre"]


def expedientes():
    print("Modulo del medico")
    Nombre=input("Digite el nombre del medico..:")
    especialidad=input("Digite su especialidad..:")
    correo=input("Digite su correo..:")
    tel=int(input("Digite el su numero de telefono..:"))
    horainicio=input("Inicia a las..:")
    ampm1=input("Digite si am o pm..:")
    horafinal=input("Termina a las..:")
    ampm2=input("Digite si am o pm..:")
    import os

    file=open("Medico.txt","w")
    file.write("------------------------------------------------------\n")
    file.write(Nombre+ "\n")
    file.write(especialidad+ "\n")
    file.write(correo+ "\n")
    file.write("tel= % s"%tel +"\n")
    file.write(horainicio)
    file.write(ampm1+ "---")
    file.write(horafinal)
    file.write(ampm1+ "\n")
    file.write("------------------------------------------------------\n")

    file=open("Medico.txt","r")
    medico=file.read()
    print(medico)  

    print("Modulo del paciente")
    Nombre2=input("Digite el nombre del paciente..:")
    correo2=input("Digite su correo..:")
    direccion=input("Digite su dirección..:")
    telefono=int(input("Digite el su numero de telefono..:"))
    atencion=input("Digite el nombre del medico que le dara atencion..:")
    tratamiento=input("Digite alguno de estos tratamientos(Carillas dentales/Ortodoncia/Blanqueamiento dental/Limpieza dental/Implantes dentales..:")

    import os

    file=open("Paciente.txt","w")
    file.write("------------------------------------------------------\n")
    file.write(Nombre2+ "\n")
    file.write(correo2+ "\n")
    file.write(direccion+ "\n")
    file.write("telefono= % s"%telefono +"\n")
    file.write(atencion+ "\n")
    file.write(tratamiento+ "\n")
    file.write("------------------------------------------------------\n")
    file=open("Paciente.txt","r")
    paciente=file.read()
    print(paciente)  

    
def Plataforma_Citas():
    Cita_eleccion=int(input("Desea agregar una cita? 1-agregar/ 2-Borrar / 3-Ver los espacios disponibles/ 4- Salir al menu.."))
    while Cita_eleccion == 1:

        Dia_cita=int(input("Para que dia del mes?___"))
        nombre_paciente=input("Digite los detalles de la cita___")
        Citas_Mes.insert(Dia_cita,[nombre_paciente])

        import os
        file=open("Citas y cancelaciones.txt","w")
        file.write("------------------------------------------------------\n")
        file.write("Cita para el dia= % s"%Dia_cita +"\n")
        file.write(nombre_paciente+"\n")
        file.write("------------------------------------------------------\n")
        file.close()

        Cita_eleccion=int(input("Desea agregar una cita? 1-agregar/ 2-Borrar / 3-Ver los espacios disponibles.."))
        if Cita_eleccion == 2:
            Dia_borrar=int(input("Que dia requiere borrar la cita?.."))
            Citas_Mes.pop(Dia_borrar)

            file=open("Citas y cancelaciones.txt","w")
            file.write("------------------------------------------------------\n")
            file.write("borro la ciTa para el dia= % s"%Dia_cita +"\n")
            file.write("------------------------------------------------------\n")
            file.close()

            Cita_eleccion=int(input("Desea agregar una cita? 1-agregar/ 2-Borrar / 3-Ver los espacios disponibles.."))
        elif Cita_eleccion == 3:
            Citas_Mes.pop(0)
            print(Citas_Mes)
            Cita_eleccion=int(input("Desea agregar una cita? 1-agregar/ 2-Borrar / 3-Ver los espacios disponibles.."))
        else:
            op=0

    
def Pagos():
    Tratamiento1=60000
    Tratamiento2=23000
    Tratamiento3=25000
    Tratamiento4=18000
    Tratamiento5=20000
    acum1=0
    acum2=0
    acum3=0
    acum4=0
    acum5=0
    sumatotal=0
    suma=0
    opcion=0
    opcion2=0
    while opcion != 6:

        print("Carillas dentales=60000")
        print("Ortodoncia=23000")
        print("Blanqueamiento dental=25000")
        print("Limpieza dental=18000")
        print("Implantes dentales=20000")
        print()
        print()
        print("Carillas dentales(20%)=1")
        print("Ortodoncia(12%)=2")
        print("Blanqueamiento dental(15%)=3")
        print("Limpieza dental(5%)=4")
        print("Implantes dentales(10%)=5")
        print("No mas tratamientos=6")

    
        opcion=int(input("Digite los tratamientos realizados..:"))

        
        if opcion==1:
            acum1+=1
            sumatotal+=Tratamiento1
            descuento=(Tratamiento1*0.2)
            resta=Tratamiento1-descuento
            suma+=resta
            
        elif opcion==2:
            acum2+=1
            sumatotal+=Tratamiento2
            descuento2=(Tratamiento2*0.12)
            resta2=Tratamiento2-descuento2
            suma+=resta2

        elif opcion==3:
            acum3+=1
            sumatotal+=Tratamiento3
            descuento3=(Tratamiento3*0.15)
            resta3=Tratamiento3-descuento3
            suma+=resta3

        elif opcion==4:
            acum4+=1
            sumatotal+=Tratamiento4
            descuento4=(Tratamiento4*0.05)
            resta4=Tratamiento4-descuento4
            suma+=resta4

        elif opcion==5:
            acum5+=1
            sumatotal+=Tratamiento5
            descuento5=(Tratamiento5*0.1)
            resta5=Tratamiento5-descuento5
            suma+=resta5

        elif opcion==6:
            print("El total a pagar es",suma)
            print("Pagara con efectivo=1")
            print("Pagara con sinpe=2")
            print("Pagara con credito o debito=3")
            int(input("La opcion de pago es..:"))


    import os
    file=open("TratamientosReporte.txt","a")
    file.write("------------------------------------------------------\n")
    file.write("Carillas dentales=% s"%acum1 +"\n")
    file.write("Ortodoncia=% s"%acum2 +"\n")
    file.write("Blanqueamiento dental=% s"%acum3 +"\n")
    file.write("Limpieza dental=% s"%acum4 +"\n")
    file.write("Implantes dentales=% s"%acum5 +"\n")
    file.write("------------------------------------------------------\n")


    
    print("Modulo de Facturacion")

    Especialidad=input("Especialidad..:")
    print("Colones=1")
    print("Dolares=2")
    Moneda=int(input("Moneda a utilizar..:"))

    if Moneda==1:
        
        NombrePaciente=input("Nombre del paciente..:")
        Cantidad1=acum1
        Cantidad2=acum2
        Cantidad3=acum3
        Cantidad4=acum4
        Cantidad5=acum5
        Precio1=acum1*Tratamiento1
        Precio2=acum2*Tratamiento2
        Precio3=acum3*Tratamiento3
        Precio4=acum4*Tratamiento4
        Precio5=acum5*Tratamiento5
        Descuento=sumatotal-suma
        Subtotal=sumatotal
        IVA=(suma*0.13)
        Total=suma+(suma*0.13)

        import os
        file=open("Factura.txt","w")
        file.write("Clinica Dr.Blanco\n")
        file.write(Especialidad +"\n")
        file.write("Colones" +"\n")
        file.write(NombrePaciente +"\n")
        
        file.write("Detalle\n")
        file.write("------------------------------------------------------\n")
        file.write("Cantidad de Carillas dentales\n")
        file.write("Cantidad1= % s"%Cantidad1 +"\n")
        file.write("Precio1= % s"%Precio1 +"\n")
        
        file.write("Cantidad de Ortodoncia\n")
        file.write("Cantidad2= % s"%Cantidad2 +"\n")
        file.write("Precio2= % s"%Precio2 +"\n")
        
        file.write("Cantidad de Blanqueamiento dental\n")
        file.write("Cantidad3= % s"%Cantidad3 +"\n")
        file.write("Precio3= % s"%Precio3 +"\n")
        
        file.write("Cantidad de Limpieza dental\n")
        file.write("Cantidad4= % s"%Cantidad4 +"\n")
        file.write("Precio4= % s"%Precio4 +"\n")
        
        file.write("Cantidad de Implantes dentales\n")
        file.write("Cantidad5= % s"%Cantidad5 +"\n")
        file.write("Precio5= % s"%Precio5 +"\n")
        file.write("------------------------------------------------------\n")
        
        file.write("Descuento= % s"%Descuento +"\n")
        file.write("Subtotal= % s"%Subtotal +"\n")
        file.write("IVA= % s"%IVA +"\n")
        file.write("Total= % s"%Total +"\n")
        file.close()

    elif Moneda==2:
        NombrePaciente=input("Nombre del paciente..:")
        Cantidad1=acum1
        Cantidad2=acum2
        Cantidad3=acum3
        Cantidad4=acum4
        Cantidad5=acum5
        Precio1=acum1*Tratamiento1/620
        Precio2=acum2*Tratamiento2/620
        Precio3=acum3*Tratamiento3/620
        Precio4=acum4*Tratamiento4/620
        Precio5=acum5*Tratamiento5/620

        Precio=sumatotal/620
        Descuento=(sumatotal-suma)/620
        Subtotal=sumatotal/620
        IVA=(suma*0.13)/620
        Total=(suma+(suma*0.13))/620
        
        import os
        file=open("Factura.txt","w")
        file.write("Clinica Dr.Blanco\n")
        file.write(Especialidad +"\n")
        file.write("Dolares" +"\n")
        file.write(NombrePaciente +"\n")

        file.write("Detalle\n")
        file.write("------------------------------------------------------\n")
        file.write("Cantidad de Carillas dentales\n")
        file.write("Cantidad1= % s"%Cantidad1 +"\n")
        file.write("Precio1= % s"%Precio1 +"\n")
        
        file.write("Cantidad de Ortodoncia\n")
        file.write("Cantidad2= % s"%Cantidad2 +"\n")
        file.write("Precio2= % s"%Precio2 +"\n")
        
        file.write("Cantidad de Blanqueamiento dental\n")
        file.write("Cantidad3= % s"%Cantidad3 +"\n")
        file.write("Precio3= % s"%Precio3 +"\n")
        
        file.write("Cantidad de Limpieza dental \n")
        file.write("Cantidad4= % s"%Cantidad4 +"\n")
        file.write("Precio4= % s"%Precio4 +"\n")
       
        file.write("Cantidad de Implantes dentales\n")
        file.write("Cantidad5= % s"%Cantidad5 +"\n")
        file.write("Precio5= % s"%Precio5 +"\n")
        file.write("------------------------------------------------------\n")
        file.write("Descuento= % s"%Descuento +"\n")
        file.write("Subtotal= % s"%Subtotal +"\n")
        file.write("IVA= % s"%IVA +"\n")
        file.write("Total= % s"%Total +"\n")
        file.close()


    file=open("Factura.txt","r")
    contenido=file.read()
    print(contenido)  



    
def reportes():
    repo=int(input("Cual reporte desea ves?-- Citas agregadas y canceladas-1/ 2- Medico y hoarios/ 3-Reporte de tratamientos"))
    if repo == 1:
        file=open("Citas y cancelaciones.txt","r")
        reportacion=file.read()
        print(reportacion)
        file.close()
    elif repo == 2:
        print("Medico y horario")
        file=open("Medico.txt","r")
        reporte1=file.read()
        print(reporte1)
        file.close()
    elif repo ==3: 
        print("Reporte de trataminetos")
        
        file=open("TratamientosReporte.txt","r")
        reportetrata=file.read()
        print(reportetrata)
        file.close()

###MENU PRINCIPAL ###
op=0
while op !=5:
    print("digite 1=expedientes, 2=citas y cancelación, 3=pagos")
    print("digite 4=reportes,  y 5=salir")
    op=int(input("digite la opcion..:"))     
    if op == 1:
        print("expedientes")
        expedientes()
    elif op == 2:
        print("citas del mes y cancelacion...:")
        Plataforma_Citas()
    elif op ==3:
        print("pagos")
        Pagos()
    elif op ==4:
        print("reportes")
        reportes()
    elif op ==5:
        print("salir")
