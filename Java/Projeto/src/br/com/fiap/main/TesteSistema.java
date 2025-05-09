package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

import javax.swing.*;

public class TesteSistema {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    // Int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    // Double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // instanciar objetos

        // String nomeCliente, String cpf, int idade, double renda
        Cliente objCliente = new Cliente(
                texto("Informe o nome do cliente"),
                texto("Informe o CPF"),
                inteiro("Informe a idade"),
                real("Renda do cliente")
        );

        // String logradouro, int numero, String cep, String bairro, String cidade
        Endereco objEndereco = new Endereco(
                texto("Endereço do cliente, Logradouro"),
                inteiro("Número"),
                texto("Informe o CEP"),
                texto("Informe o bairro"),
                texto("Digite a cidade")
        );
        objCliente.setEndereco(objEndereco);

        // String nome, String setor, String cargo, int quantidadeHora, double valorHora
        Colaborador objColaborador = new Colaborador(
                texto("Informe o nome do colaborador"),
                texto("Setor"),
                texto("Cargo"),
                inteiro("Quantidade de horas trabalhadas"),
                real("Valor da hora trabalhada")
        );

        System.out.println(objCliente + "" + objColaborador);
    }
}
