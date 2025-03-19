package br.com.fiap.main;

import br.com.fiap.beans.Produto;

public class TesteProduto {
    // psvm
    public static void main(String[] args) {
        // Instanciar objetos
        Produto objProduto = new Produto();

        // Entradas
        objProduto.setCodigo(1);
        objProduto.setTipo("Tênis");
        objProduto.setMarca("Nike");
        objProduto.setValor(150);

        // Saída
        // sout
        System.out.println(
                "Código: " + objProduto.getCodigo() +
                "\nTipo: " + objProduto.getTipo() +
                "\nMarca: " + objProduto.getMarca() +
                "\nValor: R$" + objProduto.getValor()
        );
    }
}