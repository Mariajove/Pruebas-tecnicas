import java.util.*;
public class Ejercicio10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide un numero por teclado y valida que sea positivo
		*/
		Scanner escaner= new Scanner(System.in);
		System.out.println("Dime un entero y te dire si es positivo o negativo: ");
		String numero = escaner.next();
		
		if (numero.charAt(0)=='-') {
			System.out.println(numero + " es un numero negativo.");
		}
		else {
			System.out.println(numero + " NO es un numero negativo.");
		}
		
	}

}
