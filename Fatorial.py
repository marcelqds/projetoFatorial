class Fatorial:
	""" Versão Interativa do calculo do Fatorial """
        def __init__(self, valor):
                self.valor = int(valor)
                self.resultadoFatorial()         

        def resultadoFatorial(self):
                self.resultado = 1
                for i in range(2,self.valor+1):
                        self.resultado *= i
                        print "--- %d = %d" %(i,self.resultado)

        def __str__(self) :
                return "Fatorial de %d = %d" %(self.valor, self.resultado)
        

# Incluindo um teste para merge
#fat = Fatorial(4)
#print fat
	
	

