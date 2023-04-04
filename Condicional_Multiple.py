

ingreso_mensual = 12000
 
 # SI...   
if ingreso_mensual > 10000:
    print ("Estas bien economicamente en cualquier parte del mundo")

# SINO...        
elif ingreso_mensual > 1000:
     print("Estas bien economicamente en latinoamerica")

# SINO...        
elif ingreso_mensual > 500:
    print("Estas bien en Argentina")

# SINO...    
elif ingreso_mensual < 200:
    print("estas bien en Venezuela")    
 
# DE OTRO MODO...       
else:
    print ("Sos pobre")