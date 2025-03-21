package br.com.fiap.main;

import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Produto;

public class TesteClienteProduto {
    public static void main(String[] args) {
        // Instanciar objetos
        Cliente objCliente = new Cliente();
        Produto objProduto = new Produto();

        // Entradas do cliente (setters)
        objCliente.setIdade(53);
        objCliente.setNome("Braufagelio");
        objCliente.setEmail("brf@gmail.com");
        objCliente.setRenda(7.555);

        // Entradas do produto (setters)
        objProduto.setCodigo(123);
        objProduto.setTipo("Refrigerante");
        objProduto.setMarca("Didio");
        objProduto.setValor(5.75);

        // Saídas do cliente (getters)
        System.out.println("INFORMAÇÕES DO CLIENTE" +
                "\nIdade: " + objCliente.getIdade() +
                "\nNome: " + objCliente.getNome() +
                "\nEmail: " + objCliente.getEmail() +
                "\nRenda: " + objCliente.getRenda()
        );

        System.out.println("----------");

        // Saídas do produto (getters)
        System.out.println("INFORMAÇÕES DO PRODUTO" +
                "\nCódigo: " + objProduto.getTipo() +
                "\nTipo: " + objProduto.getTipo() +
                "\nMarca: " + objProduto.getMarca() +
                "\nValor: " + objProduto.getValor()
        );
    }
}
