import java.util.*;

public class Ejercicio_11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide una frase por teclado y cuenta cuentas vocales tiene.
		*/
		Scanner escaner = new Scanner(System.in);
		System.out.println("Dime una frase y te cuento las vocales que tiene:");
		String palabra = escaner.nextLine();
		char[] vocales = {'a', 'e', 'i', 'o', 'u'};
		int totalvocales=0;
		
		for (int i=0; i<palabra.length();i++) {
			char caracterActual = Character.toLowerCase(palabra.charAt(i));
			for (char vocal:vocales) {
				if (caracterActual==vocal) {
					totalvocales++;
					break;
				}
			}
		}
		System.out.println("Tu frase tiene " + totalvocales + " vocales.");
			
	}

}
