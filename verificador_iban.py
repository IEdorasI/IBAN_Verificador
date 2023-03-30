import tkinter as tk
import re 


use_font, font_width_first, font_width_second =  'sans-serif', 15 , 18

IBAN_REGEX = r'^[A-Z]{2}\d{2}[A-Z\d]{1,30}$'

def verificar_iban():
    iban = entrada_iban.get().upper()

    
    if not iban: 
        resultado.set('Texto Vacio')
        etiqueta_resultado.configure(background='red')
    elif iban:    
        if not re.match(IBAN_REGEX, iban):
            resultado.set('El IBAN ingresado no corresponde a un IBAN aceptado')
            etiqueta_resultado.configure(background='green')
        elif len(iban) < 15:
            resultado.set("El IBAN ingresado es demasiado corto.")
            etiqueta_resultado.configure(background='red')
            
        elif len(iban) > 4 and iban[2:4].isdigit():
            resultado.set(f'Digitos de verificacon del IBAN: {iban[2:4]}')
            etiqueta_resultado.configure(background='goldenrod', foreground='black')
        else:
            check_digits = calcular_digitos_verificacion_iban(iban)
            resultado.set(f'Digitos de verificacon del IBAN: {check_digits}')
            etiqueta_resultado.configure(background='goldenrod', foreground='black')


        

def calcular_digitos_verificacion_iban(iban):
    iban_no_spaces = ''.join(ch for ch in iban if ch != ' ')
    # Replace the check digits with 00
    iban_replace_digits = iban_no_spaces[:2] + '00' + iban_no_spaces[4:]
    # Move the first four characters to the end
    rearranged_iban = iban_replace_digits[4:] + iban_replace_digits[:4]
    # Replace letters with numbers
    numeric_iban = ''.join(map(lambda ch: str(int(ch, 36)), rearranged_iban))
    # Perform mod-97 operation and subtract from 98
    check_digits = 98 - (int(numeric_iban) % 97)
    return '{:0>2}'.format(check_digits)

        

def borrar():
    entrada_iban.delete(0, tk.END)
    resultado.set('')
    etiqueta_resultado.configure(bg='white')

window = tk.Tk()
window.geometry("500x400")
window.title("Verificador de IBAN")


etiqueta_iban = tk.Label(window, text="Ingresa tu IBAN:")
etiqueta_iban.grid(row=0, column=0, columnspan=2)
etiqueta_iban.config(font=(use_font,22), fg='darkgreen')

entrada_iban = tk.Entry(window, highlightthickness= 1)
entrada_iban.grid(row=1, column=0, columnspan=2,sticky=tk.EW)
entrada_iban.grid_configure(padx=20, pady=20, ipadx= 10, ipady= 10)
entrada_iban.config(width=30, font=(use_font,18), fg='#456178', highlightbackground= 'gray', highlightcolor= 'gray')

boton_ingresar = tk.Button(window, text="Ingresar", command=verificar_iban)
boton_ingresar.grid(row=2, column=0,ipadx= 10, ipady= 10)
boton_ingresar.config(font=( use_font, font_width_first), bg= '#0047ab', fg= 'white')

boton_borrar = tk.Button(window, text="Borrar", command=borrar)
boton_borrar.grid(row=2, column=1, ipadx= 10, ipady= 10)
boton_borrar.config(font=( use_font, font_width_first), bg= 'crimson', fg='white')

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(window, textvariable=resultado)
etiqueta_resultado.grid(row=3, column=0, columnspan=2)
etiqueta_resultado.config(font=(use_font, font_width_first))


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

window.mainloop()
    