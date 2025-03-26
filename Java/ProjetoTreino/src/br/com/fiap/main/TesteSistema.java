package br.com.fiap.main;

import br.com.fiap.beans.Produto;
import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Endereco;

public class TesteSistema {
    public static void main(String[] args) {
        Produto objProduto = new Produto();
        Cliente objCliente = new Cliente();
        Endereco objEndereco = new Endereco();

        // Entradas do Produto (setters)
        objProduto.setCodigo(123);
        objProduto.setTipo("Refrigerante");
        objProduto.setMarca("Dydyo");
        objProduto.setValor(5.45);

        // Entradas do Cliente com Endereço (setters)
        objCliente.setIdade(41);
        objCliente.setNome("Braufagelio");
        objCliente.setEmail("brf@gmail.com");
        objCliente.setRenda(7.455);

        objEndereco.setLogradouro("Rua Apito do Valor");
        objEndereco.setNumero(257);
        objEndereco.setComplemento("Casa");
        objEndereco.setCep("08485-450");
        objEndereco.setBairro("Cid Tiradentes");
        objEndereco.setCidade("São Paulo");

        objCliente.setEndereco(objEndereco);

        // Saídas do produto (getters)
        System.out.println("INFORMAÇÕES DO PRODUTO" +
                "\nCódigo: " + objProduto.getTipo() +
                "\nTipo: " + objProduto.getTipo() +
                "\nMarca: " + objProduto.getMarca() +
                "\nValor: " + objProduto.getValor()
        );

        System.out.println("----------");

        // Saídas do cliente (getters)
        System.out.println("INFORMAÇÕES DO CLIENTE" +
                "\nIdade: " + objCliente.getIdade() +
                "\nNome: " + objCliente.getNome() +
                "\nEmail: " + objCliente.getEmail() +
                "\nRenda: " + objCliente.getRenda() +
                "\n\nENDEREÇO: " +
                "\nLogradouro: " + objCliente.getEndereco().getLogradouro() +
                "\nNúmero: " + objCliente.getEndereco().getNumero() +
                "\nComplemento: " + objCliente.getEndereco().getComplemento() +
                "\nCEP: " + objCliente.getEndereco().getCep() +
                "\nBairro: " + objCliente.getEndereco().getBairro() +
                "\nCidade: " + objCliente.getEndereco().getCidade()
        );
    }
}
