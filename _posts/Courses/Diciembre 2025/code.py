
year = "2025"
m = 12
month = "0" + str(m) if m < 10 else str(m)

Months = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]

for i in range(1, 32): 
    day = "0" + str(i) if i < 10 else str(i)

    file_name = year + "-" + month + "-" + day + "-I.markdown"

    markdown_content = """---
layout:     poema
title:      " """ + Months[m] + " " + day + """, """ + year + """ "
date:       """ + year + """-""" + month + """-""" + day + """ 00:00:00 +0000
category:   """ + Months[m] + """-""" + year + """
---"""

    # Create and write to the file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(markdown_content)

    print(f"Successfully created {file_name}")
