#Función para 
import pandas as pd
# Leer el archivo CSV
df = pd.read_csv('datos.csv', delimiter=';')
# Obtener los datos de interés (Año, Trimestre 1, Trimestre 2, Trimestre 3, Trimestre 4)
datos_trimestres = df[['Año', 'Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4']]
# Imprimir los datos obtenidos
print(datos_trimestres)
opt=0;
while opt!=4:
    print("Seleccione una opción");
    print("1- Calcular total de ventas por año.");
    print("2- Total de ventas por archivo.");
    print("3- Total de ventas por cuatrimestre.");
    print("4- Salir");
    opt=int(input("Opción: "));
    if opt==1:
        año=int(input("Ingrese año a calcular: "));
        datos_año=df[df["Año"]==año];
        suma=datos_año[["Trimestre 1","Trimestre 2","Trimestre 3","Trimestre 4"]].sum().sum();
        print(f"Total del año {año}: {suma}");
        print("=========================================");
    elif opt==2:
        datos_columna1=df.iloc[:,1];
        suma_colum1=df["Trimestre 1"].sum();
        datos_columna2=df.iloc[:,2];
        suma_colum2=df["Trimestre 2"].sum();
        datos_columna3=df.iloc[:,3];
        suma_colum3=df["Trimestre 3"].sum();
        datos_columna4=df.iloc[:,4];
        suma_colum4=df["Trimestre 4"].sum(); 
        #Suma total de archivo
        suma_total=suma_colum1+suma_colum2+suma_colum3+suma_colum4;
        print(f"Resultado de archivo: {suma_total}");
        print("=========================================");
    elif opt==3:
        print("Seleccione Trimestre: ");
        print("1- Trimestre 1.");
        print("2- Trimestre 2.");
        print("3- Trimestre 3.");
        print("4- Trimestre 4.");
        opcionTri=int(input("--"));
        if opcionTri==1:
            datos_columna=df.iloc[:,opcionTri]
            suma_columa=df["Trimestre 1"].sum();
            print(f"Suma: {suma_columa}");
        elif opcionTri==2:
            datos_columna=df.iloc[:,opcionTri];
            suma_columa=df["Trimestre 2"].sum();
            print(f"Suma: {suma_columa}");
        elif opcionTri==3:
            datos_columna=df.iloc[:,opcionTri];
            suma_columa=df["Trimestre 3"].sum();
            print(f"Suma: {suma_columa}");
        elif opcionTri==4:
            datos_columna=df.iloc[:,opcionTri];
            suma_columa=df["Trimestre 4"].sum();
            print(f"Suma: {suma_columa}");
        print("=========================================");
    elif opt==4:
        print("FIN DEL PROGRAMA");
    else:
        print("Opción inválida, Intente nuevamente.")


