package br.com.fiap.main;

import br.com.fiap.api.Endereco;
import br.com.fiap.services.ViacepService;

import javax.swing.*;
import java.io.IOException;

public class TesteViaCep {

    // String
    static String texto(String j){

        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {

        ViacepService objViacep = new ViacepService();

        String cep = texto("Informe o CEP para a busca");

        Endereco endereco = objViacep.getEndereco(cep);

        System.out.println(endereco);
    }
}
