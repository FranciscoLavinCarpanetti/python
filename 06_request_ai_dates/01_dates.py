###
# tranbajar con fechas


from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Establecer la localización a español


datetime.now()  # fecha y hora actual
print(f"Fecha y hora actual: {datetime.now()}")

specific_date = datetime(2025, 11,16, 12, 0, 0)  # fecha y hora específica  
print(f"Fecha y hora específica: {specific_date}")

# Formatear fechas
# Metodo strftime() para formatear fechas

formatted_date = datetime.now().strftime("%A %B %Y %H:%M:%S")  # Formato: dia/mes/año
print(f"Fecha formateada: {formatted_date}")

# Operaciones con fechas, restar y sumar dias, horas, minutos, meses, años

yesterday = datetime.now() - timedelta(days=1)  # Restar un día
print(f"Ayer fue: {yesterday.strftime('%d/%m/%Y')}")

tomorrow = datetime.now() + timedelta(days=1)  # Sumar un día
print(f"Mañana será: {tomorrow.strftime('%d/%m/%Y')}")


# Componentes individuales de una fecha

now = datetime.now()  # Definir la variable 'now'
year = now.year  # Corregir para obtener el año
print(f"Año: {year}")

# Calcular la diferencia entre dos fechas

date1 = datetime(1988, 11, 16)
date2 = datetime(2025, 11, 16)
difference = date2 - date1  # Calcular la diferencia
print(f"Diferencia entre {date2.strftime('%d/%m/%Y')} y {date1.strftime('%d/%m/%Y')}: {difference.days} días")