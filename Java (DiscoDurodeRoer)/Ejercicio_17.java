import java.util.Scanner;

public class Ejercicio_17 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Crea una funcion que genere un numero aleatorio entre 2 numeros inclusive.
		*/
		
		Scanner entrada = new Scanner(System.in);
        System.out.println("Dime un primer número:");
        int num1 = entrada.nextInt();
        System.out.println("Dime un segundo número:");
        int num2 = entrada.nextInt();
        int numero1,numero2,valor;
        
        if (num1==num2) {
        	System.out.println("No puedo generarlo si los dos numeros son iguales.");
        }
        else {
            if (num1>num2) {
            	numero1=num2;
            	numero2=num1;
            	valor = (int) (Math.random()*(numero2-numero1+1)+numero1);
            	System.out.println("El numero generado es: " + valor);
            }
            else {
                numero2=num2;
                numero1=num1;
                valor = (int) (Math.random()*(numero2-numero1+1)+numero1);
                System.out.println("El numero generado es: " + valor);
            }

        }


        
        
        
	}

}
