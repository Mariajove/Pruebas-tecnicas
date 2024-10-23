import javax.swing.*;
public class Ejercicio2 {
	public static void main(String[] args) {
	/*
    Pide el precio de un producto sin IVA y calcula su precio con IVA.

    El IVA es del 21%.

    Formatea el resultado para que se muestre con dos decimales.
*/
	double valor=Double.parseDouble(JOptionPane.showInputDialog("Dime el precio (en euros) y te lo calculo con IVA."));
	double coniva=valor+valor*0.21;
	System.out.println("El valor con IVA es de " + coniva +" euros.");
	}
	
}
