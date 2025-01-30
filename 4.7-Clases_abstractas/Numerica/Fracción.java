package Numerica;

/**
 * Clase concreta Fracción que hereda de Numérica.
 */
public class Fracción extends Numérica {
    private int numerador;
    private int denominador;

    public Fracción(int numerador, int denominador) {
        if (denominador == 0) {
            throw new ArithmeticException("El denominador no puede ser cero.");
        }
        this.numerador = numerador;
        this.denominador = denominador;
    }

    private int mcd(int a, int b) {
        return b == 0 ? a : mcd(b, a % b);
    }

    private void simplificar() {
        int mcd = mcd(numerador, denominador);
        numerador /= mcd;
        denominador /= mcd;
    }

    @Override
    public Numérica sumar(Numérica otra) {
        Fracción f = (Fracción) otra;
        int nuevoNumerador = this.numerador * f.denominador + f.numerador * this.denominador;
        int nuevoDenominador = this.denominador * f.denominador;
        Fracción resultado = new Fracción(nuevoNumerador, nuevoDenominador);
        resultado.simplificar();
        return resultado;
    }

    @Override
    public Numérica restar(Numérica otra) {
        Fracción f = (Fracción) otra;
        int nuevoNumerador = this.numerador * f.denominador - f.numerador * this.denominador;
        int nuevoDenominador = this.denominador * f.denominador;
        Fracción resultado = new Fracción(nuevoNumerador, nuevoDenominador);
        resultado.simplificar();
        return resultado;
    }

    @Override
    public Numérica multiplicar(Numérica otra) {
        Fracción f = (Fracción) otra;
        Fracción resultado = new Fracción(this.numerador * f.numerador, this.denominador * f.denominador);
        resultado.simplificar();
        return resultado;
    }

    @Override
    public Numérica dividir(Numérica otra) {
        Fracción f = (Fracción) otra;
        Fracción resultado = new Fracción(this.numerador * f.denominador, this.denominador * f.numerador);
        resultado.simplificar();
        return resultado;
    }

    @Override
    public String toString() {
        return numerador + "/" + denominador;
    }
}
