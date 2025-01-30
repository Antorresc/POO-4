package Numerica;

/**
 * Clase Prueba para realizar operaciones con fracciones.
 */
public class Prueba {
    public static void main(String[] args) {
        Fracción f1 = new Fracción(1, 2); // 1/2
        Fracción f2 = new Fracción(3, 4); // 3/4

        System.out.println("Fracción 1: " + f1);
        System.out.println("Fracción 2: " + f2);

        // Suma
        Fracción suma = (Fracción) f1.sumar(f2);
        System.out.println("Suma: " + suma);

        // Resta
        Fracción resta = (Fracción) f1.restar(f2);
        System.out.println("Resta: " + resta);

        // Multiplicación
        Fracción multiplicación = (Fracción) f1.multiplicar(f2);
        System.out.println("Multiplicación: " + multiplicación);

        // División
        Fracción división = (Fracción) f1.dividir(f2);
        System.out.println("División: " + división);
    }
}
