aprobaron_el_primer_parcial = {"Mario Mario", "Miranda Mendoza", "Miguel Núñez", "Marina Mendez", "Melisa Montero", "Martín Martín"}
aprobaron_el_segundo_parcial = {"Mario Mario", "Miguel Núñez", "Marcelo Mercedez", "Marina Mendez", "Mauricio Minoso", "Melisa Montero", "Martín Martín"}

print(f"Ambos parciales aprobados: {aprobaron_el_primer_parcial & aprobaron_el_segundo_parcial}")
print(f"Sólo un parcial aprobado: {aprobaron_el_primer_parcial ^ aprobaron_el_segundo_parcial}")
print(f"Al menos un parcial aprobado: {aprobaron_el_primer_parcial | aprobaron_el_segundo_parcial}")
