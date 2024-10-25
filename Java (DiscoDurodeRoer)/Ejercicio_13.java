import java.util.*;

public class Ejercicio_13 {
    public static void main(String[] args) {
    	// TODO Auto-generated method stub
		/*
    	Pide una frase por teclado, elimina los espacios y guardarlos en otra variable
		*/
        Scanner escaner = new Scanner(System.in);
        System.out.println("Dime una frase:");
        String frase = escaner.nextLine();
        ArrayList<Character> caracteresSinEspacios = new ArrayList<>();
        
        for (int i = 0; i < frase.length(); i++) {
            char caracterActual = frase.charAt(i);
            if (caracterActual != ' ') {
                caracteresSinEspacios.add(caracterActual);
            }
        }
        StringBuilder resultado = new StringBuilder();
        for (char c : caracteresSinEspacios) {
            resultado.append(c);
        }

        System.out.println("La frase sin espacios es: " + resultado.toString());
    }
}

