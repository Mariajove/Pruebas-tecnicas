import javax.swing.*;
public class Ejercicio_3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide dos numeros por teclado e indica si el segundo es divisble por el primero

	    Por ejemplo, si numero1 = 10 y numero2 = 5 deberia mostrar:

	    "El numero 5 es divisible de 10"
	*/
		int numero1=Integer.parseInt(JOptionPane.showInputDialog("Dime el primer numero"));
		int numero2=Integer.parseInt(JOptionPane.showInputDialog("Dime el segundo numero"));

		if (numero1%numero2==0) {
			System.out.println("El numero " + numero2 + " es divisible de " + numero1 + ".");
		}
		
		else {
			System.out.println("El número " + numero2 + " NO es divisible de " + numero1 + ".");
		}
			
	}

}
