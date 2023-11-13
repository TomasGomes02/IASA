package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;


/*
* Contexto da aplicação: "O jogo consiste num ambiente onde a personagem tem por
* objectivo registar a presença de animais através de fotografias".
*
* */
public class Jogo
{
    /*
    *  Atributos privados correspondentes à personagem e ao ambiente.
    * */
    private static Personagem personagem;
    private static Ambiente ambiente;

    /*
    * Main método da aplicação, onde vão ser inicalizados os objetos das classes Ambiente e Personagem, e chamado o método
    * executar da classe Jogo.
    *
    * */
    public static void main(String[] args)
    {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        executar();
    }

    /*
    * Método que permite à personagem ter o seu comportamento necessário ao funcionamento do jogo.
    * Enquanto o evento não for o TERMINAR, realiza o método executar do personagem e evolui o ambiente.
    * */
    private static void executar() {
        do {
            personagem.executar();

            ambiente.evoluir();
        }
        while (ambiente.getEvento() != Evento.TERMINAR);
    }
}
