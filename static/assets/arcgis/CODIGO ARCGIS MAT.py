import arcpy
#Matriculacion
#Nombre GDB Matriculación
NOMBRE_GDB_MAT = "M_20231128_01" 
#Genera el archivo de Matriculación en la carpeta seleccionada con la adición de los campos de Coordenadas
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\TRANSFORMADORES_MT\TRANSFORMADORES_MT" % NOMBRE_GDB_MAT)
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\TRANSFORMADORES_MT\TRANSFORMADORES_MT" % NOMBRE_GDB_MAT, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Matriculación\%s.xlsx" % NOMBRE_GDB_MAT, "NAME", "CODE")