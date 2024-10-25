import java.util.*;
public class Ejercicio_30 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Crea un enumerado con todos los meses del año.

	    Dado un mes, indica el numero de dias que tiene.

	    Los meses que tienen 31 dias son:
	        - Enero
	        - Marzo
	        - Mayo
	        - Julio
	        - Agosto
	        - Octubre
	        - Diciembre

	    Los meses que tienen 30 dias son:
	        - Abril
	        - Junio
	        - Septiembre
	        - Noviembre

	    En el caso de febrero, pediremos el año, ya que si el año es bisiesto tendra
	    29 dias sino tendra 28 dias.

	    Debes validar si se inserta un mes valido o si se inserta los datos correctos.
	 */
		Scanner scanner = new Scanner(System.in);
        boolean validar=false;
		
        while (validar==false) {
        	System.out.print("Dime el mes ");
        	String mes = scanner.next().toUpperCase();
        	switch (mes) {
        		case "ENERO", "MARZO", "MAYO", "JULIO", "AGOSTO", "OCTUBRE", "DICIEMBRE":
        			System.out.print(mes + " tiene 31 días.");
        			validar=true;
        			break;
        		case "ABRIL", "JUNIO", "SEPTIEMBRE", "NOVIEMBRE":
        			System.out.print(mes + " tiene 30 días.");
        			validar=true;
        			break;
        		case "FEBRERO":
        			System.out.print("Dime el año ");
        			int anio = scanner.nextInt();
        			if ((anio % 4 == 0 && anio %10 != 0) || anio % 400 == 0) {
        				System.out.print(mes + "en el año " + anio + " tiene 29 días.");
        				validar=true;
        				break;
        			}
        			else {
        				System.out.print(mes + " en el año " + anio + " tiene 28 días.");
        				validar=true;
        				break;
        			}
        		default:
        			System.out.print("No me has dicho bien ");
        			break;
        	}	
        }
	}

}
