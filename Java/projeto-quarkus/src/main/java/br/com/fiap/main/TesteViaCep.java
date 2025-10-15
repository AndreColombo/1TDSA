package br.com.fiap.main;

import br.com.fiap.api.Endereco;
import br.com.fiap.services.ViaCepService;

import javax.swing.*;
import java.io.IOException;

public class TesteViaCep {

    static String texto(String j){
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {

        ViaCepService viaCepService = new ViaCepService();

        String cep = texto("Informe o CEP para busca do endereço");

        Endereco objEndereco = viaCepService.getEndereco(cep);

        System.out.println(objEndereco);
    }
}
