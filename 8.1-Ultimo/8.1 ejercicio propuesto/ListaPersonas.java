package Personas;

import java.util.ArrayList;

public class ListaPersonas {
    private ArrayList<Persona> lista;

    public ListaPersonas() {
        lista = new ArrayList<>();
    }

    public void agregarPersona(Persona persona) {
        lista.add(persona);
    }

    public void eliminarPersona(int indice) {
        if (indice >= 0 && indice < lista.size()) {
            lista.remove(indice);
        }
    }

    public void editarPersona(int indice, Persona nuevaPersona) {
        if (indice >= 0 && indice < lista.size()) {
            lista.set(indice, nuevaPersona);
        }
    }

    public boolean existePersona(String nombre, String apellidos) {
        for (Persona persona : lista) {
            if (persona.getNombre().equalsIgnoreCase(nombre) &&
                persona.getApellidos().equalsIgnoreCase(apellidos)) {
                return true;
            }
        }
        return false;
    }

    public ArrayList<Persona> getLista() {
        return lista;
    }

    void borrarLista() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
