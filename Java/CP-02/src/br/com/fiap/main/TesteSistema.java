package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Endereco;

import javax.swing.*;

public class TesteSistema {
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        Cliente objCliente = new Cliente(
                texto("Digite o Nome do Cliente:"),
                texto("Digite o CPF:"),
                inteiro("Digite a Idade do Cliente:"),
                real("Digite a Renda:")
        );

        Endereco objEndereco = new Endereco(
                texto("Digite o Logradouro:"),
                inteiro("Digite o Número:"),
                texto("Digite o CEP:"),
                texto("Digite o Bairro:"),
                texto("Digite a Cidade:")
        );

        objCliente.setEndereco(objEndereco);

        Colaborador objColaborador = new Colaborador(
                texto("Digite o Nome do Colaborador:"),
                texto("Digite o Setor do Colaborador:"),
                texto("Digite o Cargo do Colaborador:"),
                inteiro("Digite a Quantidade de Horas trabalhadas:"),
                real("Digite o Valor da Hora trabalhada:")
        );
        System.out.println(objCliente + "" + objColaborador);
    }
}
