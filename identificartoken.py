# Abre el archivo en modo lectura y escritura
with open('salida.txt', 'r+') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()
    # Vuelve al inicio del archivo
    archivo.seek(0)
    # Trunca el archivo para eliminar su contenido anterior
    archivo.truncate()

    # Procesa cada línea
    for linea in lineas:
        # Elimina los espacios en blanco al principio y al final de la línea
        linea = linea.strip()

        if 'snorlax' in linea:
            linea += '  --1--'

        elif 'piglet' in linea:
            linea += '  --2--'

        elif 'vaporeon' in linea:
            linea += '  --3--'

        elif 'eevee' in linea:
            linea += '  --4--'

        elif 'magicarp' in linea:
            linea += '  --5--'

        elif 'ditto' in linea:
            linea += '  --6--'

        elif 'pichu' in linea:
            linea += '  --7--'

        elif 'rattata' in linea:
            linea += '  --8--'

        elif 'mew' in linea:
            linea += '  --9--'

        elif 'fuego' in linea:
            linea += '  --10--'

        elif 'planta' in linea:
            linea += '  --10--'

        elif 'agua' in linea:
            linea += '  --10--'

        elif 'electrico' in linea:
            linea += '  --10--'

        elif 'fantasma' in linea:
            linea += '  --10--'

        elif 'tierra' in linea:
            linea += '  --10--'

        elif '+' in linea:
            linea += ' --11--'

        elif '-' in linea:
            linea += ' --11--'

        elif '*' in linea:
            linea += ' --11--'

        elif '/' in linea:
            linea += ' --11--'

        elif '**' in linea:
            linea += ' --11--'

        elif '%' in linea:
            linea += ' --11--'

        elif '<' in linea:
            linea += '  --12--'

        elif '>' in linea:
            linea += '  --12--'

        elif '<=' in linea:
            linea += '  --12--'

        elif '>=' in linea:
            linea += '  --12--'

        elif '<>' in linea:
            linea += '  --12--'

        elif '==' in linea:
            linea += '  --12--'

        elif '|' in linea:
            linea += '  --13--'

        elif '&' in linea:
            linea += '  --13--'

        elif '¡' in linea:
            linea += '  --13--'

        elif '"' in linea:
            linea += '  --14--'

        elif '~' in linea:
            linea += '  --15--'

        elif '¿' in linea:
            linea += '  --16--'

        elif '(' in linea:
            linea += '  --17--'

        elif '}' in linea:
            linea += '  --18--'

        elif '=' in linea:
            linea += '  --19--'

        elif '.' in linea:
            linea += '  --20--'

        elif "'" in linea:
            linea += '  --21--'

        elif '#' in linea:
            linea += '  --23--'

        elif ')' in linea:
            linea += '  --24--'

        elif '[' in linea:
            linea += '  --25--'

        elif ':' in linea:
            linea += '  --26--'

        elif ',' in linea:
            linea += '  --27--'

        elif '$' in linea:
            linea += '  --28--'

        elif '_' in linea:
            linea += '  --29--'

        elif '@' in linea:
            linea += '  --30--'

        elif '{' in linea:
            linea += '  --31--'

        elif ']' in linea:
            linea += '  --32--'

        elif ';' in linea:
            linea += '  --33--'

        else:
            linea += '  --definido por automata o error--'

        archivo.write(linea + '\n')
