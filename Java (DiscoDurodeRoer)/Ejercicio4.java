import javax.swing.*;
public class Ejercicio4 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
    	Pide un año por teclado e indica si es bisiesto o no.

    	Un año es bisiesto cuando es divisible entre 4 y no divisible por 100 
    	o es divisible por 400
		 */
	
		int anual=Integer.parseInt(JOptionPane.showInputDialog("Dime el año y te digo si es bisiesto"));
	
		if ((anual%4==0 && anual%100!=0) || anual%400==0) {
			System.out.println(anual + " es un año bisiesto.");
		}
		
		else {
			System.out.println(anual + " NO es un año bisiesto.");
		}
	}
	
}
