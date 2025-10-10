package br.com.fiap.main;

import br.com.fiap.api.Cartoon2D;
import br.com.fiap.services.Cartoon2DService;

import javax.swing.*;
import java.io.IOException;

public class TesteCartoon2D {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {
        Cartoon2DService cartoon2d = new Cartoon2DService();

        String desenho = texto("Informe o número do desenho (7-23)");

        Cartoon2D cartoon2D = cartoon2d.getCartoon(desenho);

        System.out.println(cartoon2D);
    }
}
