package br.com.fiap.main;

import br.com.fiap.beans.Colaborador;
import br.com.fiap.beans.Empresa;
import br.com.fiap.beans.Endereco;

public class TesteSistema {
    public static void main(String[] args) {
        Empresa objEmpresa = new Empresa();
        Endereco objEndereco = new Endereco();
        Colaborador objColaborador = new Colaborador();

        objEmpresa.setCnpj("123456789");
        objEmpresa.setRazaoSocial("FIAP");
        objEmpresa.setNomeFantasia("FIAP");
        objEmpresa.setSegmento("Educação");

        objColaborador.setNumeroRegistro(123);
        objColaborador.setNome("Brafagélio");
        objColaborador.setCargo("Administrador");
        objColaborador.setSalario(4.175);

        objEndereco.setLogradouro("Avenida Lins");
        objEndereco.setNumero(123);
        objEndereco.setComplemento("3° Andar");
        objEndereco.setCep("01234-56");
        objEndereco.setBairro("Aclimação");
        objEndereco.setCidade("São Paulo");

        objColaborador.setEndereco(objEndereco);

        System.out.println("\nINFORMAÇÕES EMPRESA:" +
                "\nCNPJ: " + objEmpresa.getCnpj() +
                "\nRazão Social: " + objEmpresa.getRazaoSocial() +
                "\nNome Fantasia: " + objEmpresa.getNomeFantasia() +
                "\nSegmento: " + objEmpresa.getSegmento());
        System.out.println("\nINFORMAÇÕES COLABORADOR:" +
                "\nNúmero Registro: " + objColaborador.getNumeroRegistro() +
                "\nNome: " + objColaborador.getNome() +
                "\nCargo: " + objColaborador.getCargo() +
                "\nSalário: R$" + objColaborador.getSalario());
        System.out.println("\nINFORMAÇÕES ENDEREÇO:" +
                "\nLogradouro: " + objColaborador.getEndereco().getLogradouro() +
                "\nNúmero: " + objColaborador.getEndereco().getNumero() +
                "\nComplemento: " + objColaborador.getEndereco().getComplemento() +
                "\nCEP: " + objColaborador.getEndereco().getCep() +
                "\nBairro: " + objColaborador.getEndereco().getBairro() +
                "\nCidade: " + objColaborador.getEndereco().getCidade());
    }
}
