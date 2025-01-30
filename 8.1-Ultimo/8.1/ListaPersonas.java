package personas;

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

    public void borrarLista() {
        lista.clear();
    }

    public ArrayList<Persona> getLista() {
        return lista;
    }
}
