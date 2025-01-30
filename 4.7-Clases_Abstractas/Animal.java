package Animales;

/**
 * Clase abstracta Animal
 */
public abstract class Animal {
    protected String sonido;
    protected String alimentos;
    protected String hábitat;
    protected String nombreCientífico;

    public String getSonido() {
        return sonido;
    }

    public String getAlimentos() {
        return alimentos;
    }

    public String getHábitat() {
        return hábitat;
    }

    public String getNombreCientífico() {
        return nombreCientífico;
    }
}
