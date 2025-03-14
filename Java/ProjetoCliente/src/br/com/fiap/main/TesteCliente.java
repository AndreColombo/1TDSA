package br.com.fiap.main;

import br.com.fiap.beans.Cliente;

public class TesteCliente {
    // psvm
    public static void main(String[] args) {
        // Instanciar objetos
        Cliente objCliente = new Cliente();

        // Entradas
        objCliente.setIdade(17);
        objCliente.setNome("André Rosa Colombo");
        objCliente.setEmail("rm563112@fiap.com.br");
        objCliente.setRenda(8750);

        // Saída
        // sout
        System.out.println("Idade: " + objCliente.getIdade());
        System.out.println("Nome: " + objCliente.getNome());
        System.out.println("Email: " + objCliente.getEmail());
        System.out.println("Renda: R$" + objCliente.getRenda());
    }
}