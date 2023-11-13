package jogo.personagem;

import jogo.ambiente.Ambiente;

public class Personagem
{

    /*
    * Atributos privados ambiente e controlo:
    * O objeto da classe controlo será utilizado para, como o nome indica, controlar a personagem, recebendo uma percecao.
    * */
    private Ambiente ambiente;
    private Controlo controlo;

    /*
    * Construtor da classe, que irá criar uma personagem no objeto ambiente que recebe como parametro.
    * */
    public Personagem(Ambiente ambiente)
    {
        controlo = new Controlo();
        this.ambiente = ambiente;
    }

    /*
    * Método executar: permite que a personagem execute o seu comportamento, chamado pela classe Jogo.
    *
    * */
    public void executar()
    {
        actuar(controlo.processar(percepcionar()));
    }

    /*
    * Método percepcionar: retorna uma instância da Classe percepcao, passando o ambiente como argumento no construtor.
    *
    * */
    private Percepcao percepcionar()
    {
        Percepcao percepcao = new Percepcao(ambiente.getEvento());

        return percepcao;
    }

    /*
    * Método Actuar: dá print da acçãoo realizada pelo personagem, caso esta não seja null.
    *
    * */
    private void actuar(Accao accao)
    {
        if(accao!=null)
        {
            System.out.println("Ação realizada: " + accao);
        }
    }
}
