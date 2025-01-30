package Numerica;

/**
 * Clase abstracta Numérica para representar operaciones matemáticas.
 */
public abstract class Numérica {
    public abstract Numérica sumar(Numérica otra);
    public abstract Numérica restar(Numérica otra);
    public abstract Numérica multiplicar(Numérica otra);
    public abstract Numérica dividir(Numérica otra);

    @Override
    public abstract String toString(); // Para mostrar los valores.
}

