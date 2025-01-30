package Animales;

/**
 * Clase Prueba para crear y mostrar información de los animales
 */
public class Prueba {
    public static void main(String[] args) {
        Animal[] animales = new Animal[4]; // Array de cuatro elementos de tipo Animal

        animales[0] = new Gato();
        animales[1] = new Perro();
        animales[2] = new Lobo();
        animales[3] = new León();

        for (Animal animal : animales) {
            System.out.println("Nombre científico: " + animal.getNombreCientífico());
            System.out.println("Sonido: " + animal.getSonido());
            System.out.println("Alimentos: " + animal.getAlimentos());
            System.out.println("Hábitat: " + animal.getHábitat());
            System.out.println();
        }
    }
}
