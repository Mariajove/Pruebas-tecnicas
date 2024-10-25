import javax.swing.*;

public class Ejercicio_16 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
	    Pide un numero por teclado y saca su factorial.

	    El factorial se obtiene de multiplicar los numeros de n a 1.

	    Por ejemplo, 5*4*3*2*1 = 120
		*/
		
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Dime un numero para sacar el factorial: "));

        int factorial = 1; 
        for (int i = numero; i > 0; i--) {
            factorial *= i; 
        }

        System.out.println("El factorial de " + numero + " es " + factorial);
	}

}
