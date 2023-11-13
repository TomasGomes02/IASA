package jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
* A classe ambiente serve como modo a simular a sequência de eventos do ambiente que decorre no Jogo.
* */
public class Ambiente
{

    /*
    * Atributos privados:
    *   - evento, representa o evento mais recente que ocorreu no ambiente,
    *     ou seja, o atualizado resultante do gerarEvento();
    *   - sc, permite que o jogo receba input do jogador na forma de Strings;
    *   - eventos, dicionário que associa as strings que o jogador insere a eventos.
    * */
    private Evento evento;

    private Scanner sc = new Scanner(System.in);
    private Map<String, Evento> eventos;

    /*
    *   Construtor da classe que cria o dicionário com os vários
    *   inputs disponiveis para o jogador, associados a eventos respetivamente.
    * */
    public Ambiente()
    {
        eventos = new HashMap<>();
        eventos.put("s", Evento.SILENCIO);
        eventos.put("r", Evento.RUIDO);
        eventos.put("a", Evento.ANIMAL);
        eventos.put("f", Evento.FUGA);
        eventos.put("o", Evento.FOTOGRAFIA);
        eventos.put("t", Evento.TERMINAR);
    }
    /*
    * Método getEvento(): retorna o evento atual no Ambiente
    * que irá ser utilizado no método executar() da classe Jogo
    * de modo a verificar se o Jogo terminou ou não.
    * Também é utilizado na classe Personagem de modo a que a personagem
    * possa reagir ao que está à sua volta.
    *
    *   @return Evento atual
    * */
    public Evento getEvento()
    {
        return evento;
    }

    /*
    * Método evoluir(): método que muda o evento atual e
    * dá print deste para que o jogador possa perceber o que
    * está a acontecer.
    * */
    public void evoluir()
    {
        evento = gerarEvento();
        mostrar();
    }

    /*
    * Método gerarEvento(): método que muda de evento,
    * recebido pelo jogador como input.
    *   @return novo Evento.
    * */
    private Evento gerarEvento()
    {
        System.out.println("Evento...? ");
        String command = sc.next();
        return eventos.get(command);
    }

    /*
    * Método mostrar(): método que mostra na consola o evento atual,
    * caso este não seja null.
    *
    * */
    private void mostrar() {
        if (this.evento != null)
        {
            System.out.println("Evento: " + this.evento.toString());
        }
    }
}
