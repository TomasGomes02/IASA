package jogo.personagem;

import jogo.ambiente.Evento;

public class Percepcao {

    //Atributo privado evento da classe Evento
    private Evento evento;

    /*
    * Construtor da classe Percepcao, que inicializa o atributo evento, com o que recebe,
    * que irá ser posteriormente interpretado no método executar da classe Personagem.
    * */
    public Percepcao(Evento evento)
    {
        this.evento = evento;
    }

    /*
    * Método getEvento(): Getter do atributo privado evento, que retonar este mesmo.
    *
    * */
    public Evento getEvento()
    {
        return this.evento;
    }

}
