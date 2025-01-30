package personas;

public class Persona {
    private String nombre;
    private String apellidos;
    private String direccion;
    private String telefono;

    public Persona(String nombre, String apellidos, String direccion, String telefono) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.direccion = direccion;
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return nombre + " " + apellidos + " (" + telefono + ")";
    }
}
