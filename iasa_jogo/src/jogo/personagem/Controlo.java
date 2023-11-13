package jogo.personagem;

import jogo.ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;

/*
* A classe controlo permite que o personagem interaja com o
* ambiente, utilizando o objeto da classe Percepcao.
* Esta também possui uma máquina de estados que irá permitir
* a transição de estado para estado de acordo com os "estímulos"
* recebidos e o estado anterior.
* */
public class Controlo {

    /*
    * Atributo privado:
    *   - maqEst, da classe MaquinaEstados, permite a transição
    *     de estados.
    * */
    private MaquinaEstados<Evento, Accao> maqEst;

    public Controlo()
    {
        //Definir estados
        Estado<Evento, Accao> procura = new Estado<>("Procura");
        Estado<Evento, Accao> inspeccao = new Estado<>("Inspecção");
        Estado<Evento, Accao> observacao = new Estado<>("Observação");
        Estado<Evento, Accao> registo = new Estado<>("Registo");

        //Definir transições
        procura
                //EVENTO    ,   NOVO ESTADO     ,   ACCAO
                .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
                .transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        inspeccao
                .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR)
                .transicao(Evento.SILENCIO, procura);

        observacao
                .transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
                .transicao(Evento.FUGA, inspeccao);

        registo
                .transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR)
                .transicao(Evento.FUGA, procura)
                .transicao(Evento.FOTOGRAFIA, procura);

        // Estado inicial = procura
        maqEst = new MaquinaEstados<>(procura);
    }

    /*
    * Método getEstado(): retorna o estado da máquina de estados.
    * */
    public Estado<Evento, Accao> getEstado()
    {
        return maqEst.getEstado();
    }

    /*
    * Método processar(Percepcao percepcao): método que permite à personagem,
    * consoante a sua percepcão que tem do ambiente.
    * */
    public Accao processar(Percepcao percepcao)
    {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    private void mostrar()
    {
        System.out.println("Estado: " + getEstado().getNome().toUpperCase());
    }
}
