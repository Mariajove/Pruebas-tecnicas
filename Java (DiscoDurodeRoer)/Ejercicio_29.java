import java.util.*;

public class Ejercicio_29 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Dime el número de filas: ");
        int m = scanner.nextInt();
        System.out.print("Dime el número de columnas: ");
        int n = scanner.nextInt();
        char[][] tablero = new char[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                tablero[i][j] = ' ';
            }
        }

        System.out.print("Dime la fila donde se colocará la X: ");
        int posX = scanner.nextInt() - 1;
        System.out.print("Dime la columna donde se colocará la X: ");
        int posY = scanner.nextInt() - 1;
        tablero[posX][posY] = 'X';

        mostrarTablero(tablero);

        while (true) {
            System.out.print("Ingresa la dirección para mover ('w' arriba, 's' abajo, 'a' izquierda, 'd' derecha, 'q' para salir): ");
            char direccion = scanner.next().charAt(0);

            int nuevaPosX = posX;
            int nuevaPosY = posY;

            switch (direccion) {
                case 'w': 
                    nuevaPosX = (posX > 0) ? posX - 1 : posX;
                    break;
                case 's': 
                    nuevaPosX = (posX < m - 1) ? posX + 1 : posX;
                    break;
                case 'a': 
                    nuevaPosY = (posY > 0) ? posY - 1 : posY;
                    break;
                case 'd':
                    nuevaPosY = (posY < n - 1) ? posY + 1 : posY;
                    break;
                case 'q': 
                    System.out.println("Programa terminado.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Dirección no válida. Inténtalo de nuevo.");
                    continue;
            }

            if (nuevaPosX != posX || nuevaPosY != posY) {
                tablero[posX][posY] = ' ';   
                tablero[nuevaPosX][nuevaPosY] = 'X'; 
                posX = nuevaPosX;
                posY = nuevaPosY;
            }

            mostrarTablero(tablero);
        }
    }

    public static void mostrarTablero(char[][] tablero) {
        for (char[] fila : tablero) {
            for (char celda : fila) {
                System.out.print("[" + celda + "]");
            }
            System.out.println();
        }
        System.out.println();
    }
}
