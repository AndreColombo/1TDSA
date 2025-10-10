package br.com.fiap.main;

import br.com.fiap.api.Cartoon3D;
import br.com.fiap.services.Cartoon3DService;

import javax.swing.*;
import java.io.IOException;

public class TesteCartoon3D {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {
        Cartoon3DService cartoon3d = new Cartoon3DService();

        String desenho = texto("Informe o número do desenho (1-2)");

        Cartoon3D cartoon3D = cartoon3d.getCartoon(desenho);

        System.out.println(cartoon3D);
    }
}
