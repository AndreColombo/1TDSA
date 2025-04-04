package br.com.fiap.main;

import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Empresa;
import br.com.fiap.beans.Endereco;

import javax.swing.*;

public class TesteSistema {
    public static void main(String[] args) {
        // instanciar objetos
        Colaborador objColaborador = new Colaborador();
        Empresa objEmpresa = new Empresa();
        Endereco objEndereco = new Endereco();

        // Entradas da Empresa
        objEmpresa.setCnpj(JOptionPane.showInputDialog("Informe o CNPJ da Empresa:"));
        objEmpresa.setRazaoSocial(JOptionPane.showInputDialog("Informe a Razão Social:"));
        objEmpresa.setNomeFantasia(JOptionPane.showInputDialog("Informe o Nome Fantasia:"));
        objEmpresa.setSegmento(JOptionPane.showInputDialog("Qual o Segmento da Empresa?"));

        // Entradas do Colaborador
        objColaborador.setNome(JOptionPane.showInputDialog("Informe o Nome do Colaborador:"));
        objColaborador.setIdade(Integer.parseInt(JOptionPane.showInputDialog("Informe a Idade:")));
        objColaborador.setEmail(JOptionPane.showInputDialog("Informe o Email:"));
        objColaborador.setCargo(JOptionPane.showInputDialog("Informe o Cargo:"));
        objColaborador.setSalario(Double.parseDouble(JOptionPane.showInputDialog("Informe o Salário:")));

        // Entradas do Endereço
        objEndereco.setLogradouro(JOptionPane.showInputDialog("Informe o Logradouro:"));
        objEndereco.setNumero(Integer.parseInt(JOptionPane.showInputDialog("Informe o Número:")));
        objEndereco.setComplemento(JOptionPane.showInputDialog("Informe o Complemento:"));
        objEndereco.setCep(JOptionPane.showInputDialog("Informe o CEP:"));
        objEndereco.setBairro(JOptionPane.showInputDialog("Informe o Bairro:"));
        objEndereco.setCidade(JOptionPane.showInputDialog("Informe o Cidade:"));

        objColaborador.setEndereco(objEndereco);

        // Saídas
        System.out.println("INFORMAÇÕES DA EMPRESA" +
                "\nCNPJ: " + objEmpresa.getCnpj() +
                "\nRazão Social: " + objEmpresa.getRazaoSocial() +
                "\nNome Fantasia: " + objEmpresa.getNomeFantasia() +
                "\nSegmento: " + objEmpresa.getSegmento() +
                "\n\nINFORMAÇÕES DO COLABORADOR: " +
                "\nNome: " + objColaborador.getNome() +
                "\nEmail: " + objColaborador.getEmail() +
                "\nIdade: " + objColaborador.getIdade() +
                "\nCargo: " + objColaborador.getCargo() +
                "\nSalário: " + objColaborador.getSalario() +
                "\nENDEREÇO" +
                "\nLogradouro: " + objEndereco.getLogradouro() +
                "\nNúmero: " + objEndereco.getNumero() +
                "\nComplemento: " + objEndereco.getComplemento() +
                "\nCEP: " + objEndereco.getCep() +
                "\nBairro: " + objEndereco.getBairro() +
                "\nCidade: " + objEndereco.getCidade());
    }
}
