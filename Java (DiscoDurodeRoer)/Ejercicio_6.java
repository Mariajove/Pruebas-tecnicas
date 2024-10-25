import java.util.*;

public class Ejercicio_6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
	    Pide 2 operandos, un operador (+ - * /) y realiza la operacion correspondiente.

	    Si el operador es invalido o el 2º operando es 0 en el caso de la division, 
	    debes indicar que no se puede realizar la operacion.

		 */
	       Scanner escaner = new Scanner(System.in);

	        System.out.println("Introduce el primer operando:");
	        double operando1 = escaner.nextDouble();

	        System.out.println("Introduce el segundo operando:");
	        double operando2 = escaner.nextDouble();

	        System.out.println("Introduce la operacion (+ - * /):");
	        String  operacion= escaner.next();
	        
	        switch(operacion) {
	        case "+":
	        	System.out.println("Has seleccionado la suma, la operación da de resultado " + (operando1+operando2));
	        	break;
	        case "-":
	        	System.out.println("Has seleccionado la resta, la operación da de resultado " + (operando1 - operando2));
	        	break;
	        case "*":
	        	System.out.println("Has seleccionado la multiplicacion, la operación da de resultado " + (operando1*operando2));
	        	break;
	        case "/":
	        	if (operando2==0) {
	        		System.out.print("No puedo dividir entre 0.");
	        		break;
	        	}
	        	else {
	        	System.out.print("Has seleccionado la division, la operación da de resultado ");
	        	System.out.printf("1.2f", (operando1/operando2));
	        	break;
	        	}
	        default:
	        	System.out.print("No me has dado un caracter correcto.");
	        	break;
	        }
	}

}
