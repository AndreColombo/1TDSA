package br.com.fiap.main;

import br.com.fiap.api.Endereco;
import br.com.fiap.services.ViaCepServices;

import javax.swing.*;
import java.io.IOException;

public class TesteViaCep {
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {
        ViaCepServices viaCep = new ViaCepServices();

        String cep = texto("Informe o CEP para busca do endereço");

        Endereco endereco = viaCep.getEndereco(cep);

        System.out.println(endereco);
    }
}