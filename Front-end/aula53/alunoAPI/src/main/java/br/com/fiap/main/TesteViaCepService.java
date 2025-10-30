package br.com.fiap.main;

import br.com.fiap.model.Endereco;
import br.com.fiap.services.ViaCepService;

import javax.swing.*;
import java.io.IOException;

public class TesteViaCepService {

    // String
    static String texto(String j){
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {

        ViaCepService objViaCep = new ViaCepService();

        String cep = texto("Informe o CEP para a busca");

        Endereco endereco = objViaCep.getEndereco(cep);

        System.out.println(endereco);

    }
}
