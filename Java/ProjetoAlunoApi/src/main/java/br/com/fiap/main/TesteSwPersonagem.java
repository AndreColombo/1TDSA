package br.com.fiap.main;

import br.com.fiap.api.Pessoa;
import br.com.fiap.services.SwPessoaService;

import javax.swing.*;
import java.io.IOException;

public class TesteSwPersonagem {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {
        SwPessoaService swPessoa = new SwPessoaService();

        String p = texto("Informe o número do personagem");

        Pessoa pessoa = swPessoa.getPessoa(p);

        System.out.println(pessoa);
    }
}
