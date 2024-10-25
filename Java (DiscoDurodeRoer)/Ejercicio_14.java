import java.util.*;

public class Ejercicio_14 {

    public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide una frase e indica si es palindromo.

	    Un palindromo es una palabra o frase que se lee igual al reves sin espacios.

	    Por ejemplo, "Amad a la dama"
	    */
        Scanner escaner = new Scanner(System.in);
        System.out.println("Dime una frase y te digo si es palíndroma:");
        String palabra = escaner.nextLine();
        String palabrafinal = palabra.replace(" ", "").toLowerCase();
        
        boolean esPalindroma = true;
        int longitud = palabrafinal.length();
        
        for (int i = 0; i < longitud; i++) {
            char a = palabrafinal.charAt(i);
            char b = palabrafinal.charAt(longitud - 1 - i);
            if (a != b) {
                esPalindroma = false;
                break;
            }
        }
        if (esPalindroma) {
            System.out.println("Es palíndroma");
        } else {
            System.out.println("NO es palíndroma");
        }
    }
}

