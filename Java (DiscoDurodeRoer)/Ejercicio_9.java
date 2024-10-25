import java.util.*;
public class Ejercicio_9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide un numero por teclado y muestra su tabla de multiplicar hasta 10.
		*/
		Scanner escaner= new Scanner(System.in);
		System.out.println("Dime un numero y te dire su tabla de multiplicar");
		int numero=escaner.nextInt();
		
		System.out.println("Me has dado el " + numero + ", su tabla de multiplicar es:");
		
		for (int i=1; i<11; i++) {
			System.out.println(numero + " multiplicado por " + i + " es: " + (numero*i));
		}
	}

}
