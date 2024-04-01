import arcpy

#Nombre GDB levantamiento
NOMBRE_GDB_LEV = "L_20231129_01" 

#Entidades que requieren adición de Geometría
arcpy.management.AddGeometryAttributes(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\ACOMETIDA" % NOMBRE_GDB_LEV, "LINE_START_MID_END", '', '', 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]')
arcpy.management.AddGeometryAttributes(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\TRAMO_BT" % NOMBRE_GDB_LEV, "LINE_START_MID_END", '', '', 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]')
#AGREGAR COORDENADAS A LA ENTIDAD- Este proceso solo debe cambiar la Ubicación del GDB
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\CAJA_DE_ABONADO" % NOMBRE_GDB_LEV)
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\APOYO_BT" % NOMBRE_GDB_LEV)
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\CAJA_DE_ABONADO" % NOMBRE_GDB_LEV)
try:
    with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
        arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\CAJA_SUBTERRANEA" % NOMBRE_GDB_LEV)
except: Exception
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\MEDIDOR" % NOMBRE_GDB_LEV)
try:
    with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
        arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Antena" % NOMBRE_GDB_LEV)
except: Exception
try:
    with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
        arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Camara_y_Sensor" % NOMBRE_GDB_LEV)
except: Exception
try:
    with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
        arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\OTRAS_CARGAS_TV_CABLE" % NOMBRE_GDB_LEV)
except: Exception
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\PUENTE_BT" % NOMBRE_GDB_LEV)
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\PUESTA_A_TIERRA" % NOMBRE_GDB_LEV)
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\SUMINISTROS" % NOMBRE_GDB_LEV)
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\TRANSICION" % NOMBRE_GDB_LEV)
try:
    with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
        arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Semaforo" % NOMBRE_GDB_LEV)
except Exception:
    print('Se han adicionado correctamente las coordenadas')
try:
    with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
        arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Valla_Publicitaria" % NOMBRE_GDB_LEV)
except Exception:
    print('Add coordinates sucesfully complete')
#Si no existe la entidad genera una alerta en la consola

#Se agregan las coordenadas agregadas al bloque de codigo 
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\ACOMETIDA" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_ACOMETIDA.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\APOYO_BT" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_APOYO_BT.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\CAJA_DE_ABONADO" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_CAJA_DE_ABONADO.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\CAJA_SUBTERRANEA" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_CAJA_SUBTERRANEA.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except: Exception
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\MEDIDOR" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_MEDIDOR.xlsx"% (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Antena" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_ANTENA.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except: Exception
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Camara_y_sensor" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_CAMARA_SENSOR.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except: Exception
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\OTRAS_CARGAS_TV_CABLE" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_TV_CABLE.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except: Exception
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\PUENTE_BT" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_PUENTE_BT.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\PUESTA_A_TIERRA" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_PUESTA_A_TIERRA.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\SUMINISTROS" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_SUMINISTROS.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\TRAMO_BT" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_TRAMO_BT.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\TRANSICION" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_TRANSICION.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Semaforo" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_SEMAFORO.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except Exception:
    print('Se ha finalizado con el proceso de generación de tablas')
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\Otras_Cargas_Valla_Publicitaria" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_SEMAFORO.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except Exception:
    print('Se ha finalizado con el proceso de generación de tablas, sin vallas publicitarias')
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'):
    arcpy.management.AddXY(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\APOYO_NN_CRUCE_FIC" % NOMBRE_GDB_LEV)
try:
    arcpy.conversion.TableToExcel(r"C:\Users\anliscen\OneDrive - Syspotec\Escritorio\%s.gdb\ENTIDADES_BT\APOYO_NN_CRUCE_FIC" % NOMBRE_GDB_LEV, r"C:\Users\anliscen\OneDrive - Syspotec\Entregas\Levantamiento\%s\EXCEL\%s_APOYO_NN.xlsx" % (NOMBRE_GDB_LEV, NOMBRE_GDB_LEV), "NAME", "CODE")
except: Exception
print('Se ha completado el proceso correctamente')