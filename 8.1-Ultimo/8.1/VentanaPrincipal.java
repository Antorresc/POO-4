package personas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class VentanaPrincipal extends JFrame implements ActionListener {
    private JTextField campoNombre, campoApellidos, campoDireccion, campoTelefono;
    private DefaultListModel<String> modeloLista;
    private JList<String> listaVisual;
    private ListaPersonas listaPersonas;

    public VentanaPrincipal() {
        setTitle("Gestión de Personas");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Panel de entrada
        JPanel panelEntrada = new JPanel(new GridLayout(4, 2));
        panelEntrada.add(new JLabel("Nombre:"));
        campoNombre = new JTextField();
        panelEntrada.add(campoNombre);

        panelEntrada.add(new JLabel("Apellidos:"));
        campoApellidos = new JTextField();
        panelEntrada.add(campoApellidos);

        panelEntrada.add(new JLabel("Dirección:"));
        campoDireccion = new JTextField();
        panelEntrada.add(campoDireccion);

        panelEntrada.add(new JLabel("Teléfono:"));
        campoTelefono = new JTextField();
        panelEntrada.add(campoTelefono);

        add(panelEntrada, BorderLayout.NORTH);

        // Lista visual
        modeloLista = new DefaultListModel<>();
        listaVisual = new JList<>(modeloLista);
        add(new JScrollPane(listaVisual), BorderLayout.CENTER);

        // Panel de botones
        JPanel panelBotones = new JPanel();
        JButton botonAgregar = new JButton("Agregar");
        botonAgregar.addActionListener(this);
        panelBotones.add(botonAgregar);

        JButton botonEliminar = new JButton("Eliminar");
        botonEliminar.addActionListener(this);
        panelBotones.add(botonEliminar);

        JButton botonBorrarTodo = new JButton("Borrar Todo");
        botonBorrarTodo.addActionListener(this);
        panelBotones.add(botonBorrarTodo);

        add(panelBotones, BorderLayout.SOUTH);

        // Inicializar lista de personas
        listaPersonas = new ListaPersonas();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String comando = e.getActionCommand();

        if (comando.equals("Agregar")) {
            String nombre = campoNombre.getText();
            String apellidos = campoApellidos.getText();
            String direccion = campoDireccion.getText();
            String telefono = campoTelefono.getText();

            if (!nombre.isEmpty() && !apellidos.isEmpty()) {
                Persona persona = new Persona(nombre, apellidos, direccion, telefono);
                listaPersonas.agregarPersona(persona);
                modeloLista.addElement(persona.toString());

                campoNombre.setText("");
                campoApellidos.setText("");
                campoDireccion.setText("");
                campoTelefono.setText("");
            } else {
                JOptionPane.showMessageDialog(this, "El nombre y los apellidos son obligatorios.");
            }
        } else if (comando.equals("Eliminar")) {
            int seleccion = listaVisual.getSelectedIndex();
            if (seleccion != -1) {
                listaPersonas.eliminarPersona(seleccion);
                modeloLista.remove(seleccion);
            }
        } else if (comando.equals("Borrar Todo")) {
            listaPersonas.borrarLista();
            modeloLista.clear();
        }
    }
}
