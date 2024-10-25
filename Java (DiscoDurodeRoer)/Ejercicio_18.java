import java.util.*;

public class Ejercicio_18 {

    public static void main(String[] args) {
        Scanner escaner = new Scanner(System.in);
        System.out.print("Dime la longitud de la contraseña: ");
        int lon = escaner.nextInt();
        
        String letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        String numeros = "1234567890";
        String caracteres = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~";
        
        Random random = new Random();
        
        StringBuilder contraseña = new StringBuilder();
        
        for (int i = 0; i < lon; i++) {
            int tipo = random.nextInt(3);

            if (tipo == 0) {
                int indiceAleatorio = random.nextInt(letras.length());
                contraseña.append(letras.charAt(indiceAleatorio));
            } else if (tipo == 1) {
                int indiceAleatorio = random.nextInt(numeros.length());
                contraseña.append(numeros.charAt(indiceAleatorio));
            } else {
                int indiceAleatorio = random.nextInt(caracteres.length());
                contraseña.append(caracteres.charAt(indiceAleatorio));
            }
        }
        
        System.out.println("Contraseña generada: " + contraseña.toString());
    }
}

