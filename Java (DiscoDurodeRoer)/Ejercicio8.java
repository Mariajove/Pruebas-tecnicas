public class Ejercicio8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Muestra los números del 1 al 100 que sean divisibles entre 2 y 3.
		*/
		
		for (int i=1; i<101; i++) {
			if (i%2==0 && i%3==0) {
				System.out.println(i);
			}
		}
	}

}
