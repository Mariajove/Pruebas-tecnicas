import java.util.Scanner;

public class Ejercicio_12 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide una frase por teclado y cuenta cuantas mayusculas y minusculas hay.
		*/
		Scanner escaner = new Scanner(System.in);
		System.out.println("Dime una frase y te cuento las mayusculas y minusculas que tiene:");
		String palabra = escaner.nextLine();
		int totalmayus=0;
		int totalminus=0;
		
		for (int i=0; i<palabra.length();i++) {
			char caracterActual = palabra.charAt(i);
			if (Character.isUpperCase(caracterActual)) {
				totalmayus++;
			}
			else if (Character.isLowerCase(caracterActual)) {
				totalminus++;
			}
		}
		System.out.println("Tu frase tiene " + totalmayus + " mayusculas y " + totalminus + " minusculas.");		
		
	}

}
