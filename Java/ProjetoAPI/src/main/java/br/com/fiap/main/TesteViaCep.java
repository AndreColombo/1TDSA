package br.com.fiap.main;

import br.com.fiap.api.Endereco;
import br.com.fiap.services.ViaCepService;

import javax.swing.*;
import java.io.IOException;

public class TesteViaCep {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {
        ViaCepService viaCep = new ViaCepService();

        String cep = texto("CEP");

        Endereco endereco = viaCep.getEndereco(cep);

        System.out.println(endereco);
    }
}
