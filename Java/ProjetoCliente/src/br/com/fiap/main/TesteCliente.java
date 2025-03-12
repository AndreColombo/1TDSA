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
        objCliente.setAltura(1.70);

        // Saída
        // sout
        System.out.println("Idade: "+objCliente.getIdade());
        System.out.println("Nome: "+objCliente.getNome());
        System.out.println("Altura: "+objCliente.getAltura());
    }
}
