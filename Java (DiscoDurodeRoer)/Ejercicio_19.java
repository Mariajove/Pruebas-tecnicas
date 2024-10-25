import java.util.*;
public class Ejercicio_19 {
	// TODO Auto-generated method stub
			/*
		    Crea una funcion dado un parametro obtenga el numero de la serie fibonacci.

		    La serie fibonacci, empieza en 1 1 y el siguiente se obtiene sumando los dos anteriores.

		    Por ejemplo, 1 1 2 3 5 8 13 21 34 55 ...

		    Valida que la posicion es mayor o igual que 1.
			*/

	public static void fibonacci(int MAX) {

		int firstNumber = 0;
		int secondNumber = 1;
		int fibonacci = '\0';

		System.out.print(firstNumber + " ");
		System.out.print(secondNumber + " ");

		for (int i = 2; i < MAX; i++) {

			fibonacci = firstNumber + secondNumber;
			System.out.print(fibonacci + " ");

			firstNumber = secondNumber;
			secondNumber = fibonacci;
		}
	}
	public static void main(String[] args) {
		Scanner escaner = new Scanner(System.in);
		System.out.println("Dime un numero y calculo la sucesión de Fibonachi");
		int MAX = escaner.nextInt();
		System.out.println("La sucesión con " + MAX + " es:");
		fibonacci(MAX);
	}

}
