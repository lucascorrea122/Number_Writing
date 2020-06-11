import re

unity = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

ten = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 
        'sessenta', 'setenta', 'oitenta', 'noventa')

hundred = ('', 'cento', 'duzentos', 'trezentos','quatrocentos', 
            'quinhentos', 'seiscentos','setecentos', 'oitocentos', 'novecentos')

thousand = ('', 'mil', 'milhão')

thousands = (' reais ', ' mil ', ' milhões ')

def get_number():
        print('_____________Número por extenso_____________')
        print('_Não necessita . (ponto) para mil e milhões_')
        print('Utilize , (virgula) para informar os centavos')
        print('Utilize apenas 9 digitos antes da virgula e dois dígitos depois')
        value = input('Informe a quantia em R$: ')
        
        while True:
                try:
                        match_pattern = re.match(r'\d{1,9},\d{2}', value)
                        # print (match_pattern.group(0))
                        divider_cents = value.split(',')
                        whole_part = divider_cents[0]
                        cents_part = divider_cents[1]
                        all_number(whole_part, cents_part)
                        break
                except:    
                       get_number()



def all_number(whole_part, centss):
        parts = list()
        first_part = whole_part[-9:-6] ##writing
        second_part = whole_part[-6:-3] ##Mill
        third_part = whole_part[-3:] ##Centena
        writing = ""


        if(first_part != "" and first_part != "000"):                
                parts.append(int(first_part))
        if(second_part != ""):                
                parts.append(int(second_part))
        if(third_part != "" ):                
                parts.append(int(third_part))
        
        parts.reverse()
        tamanho = len(parts)
        
        while ( tamanho > 0 ):
                part = parts[tamanho - 1]
                d = part % 100
                if(part == 100):
                        quali = thousands[tamanho - 1]
                        writing += 'cem ' + quali
                elif(part == 000):
                        pass        
                elif(part > 100): 
                        cm = hundred[part // 100]
                        if(d <= 20):
                                dm = unity[d]
                                writing += cm + ' e ' + dm + thousands[tamanho - 1]
                        else:
                                dm = ten[d  // 10]  
                                um = unity[d % 10]  
                                writing += cm + ' e ' + dm + ' e ' + um + thousands[tamanho - 1] 
                else:
                        if(d <= 20):
                                if(d == 1 ):
                                        writing += thousands[tamanho - 1]
                                else:
                                        dm = unity[d]
                                        writing +=  dm + thousands[tamanho - 1]
                        else:
                                dm = ten[d  // 10]  
                                um = unity[d % 10]  
                                writing +=  dm + ' e ' + um + thousands[tamanho - 1]
                tamanho = tamanho - 1
                
        expression = writing + (cents(centss))
        print(expression)
        

def cents(cents_part):
        aux_cents = int(cents_part)
        if(aux_cents <= 20):
                if(aux_cents == 1):
                        return(f'e {unity[aux_cents]} centavo')
                elif(aux_cents == 0):
                        return ""    
                else:        
                        return(f'e {unity[aux_cents]} centavos')
        else:        
                unity_cent = unity[aux_cents % 10]
                ten_cent = ten[aux_cents // 10]
                cents_writing = ten_cent + ' e ' +unity_cent +' centavos'      
                return (cents_writing)

get_number()                 