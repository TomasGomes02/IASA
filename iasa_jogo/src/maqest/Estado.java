package maqest;

import java.util.HashMap;
import java.util.Map;

public class Estado<EV, AC> {

    private String nome;
    private Map<EV, Transicao<EV, AC>> transicoes;
    public String getNome(){return this.nome;}

    public Estado(String nome){
        transicoes = new HashMap<>();
        this.nome = nome;
    }
    public Transicao<EV,AC> processar(EV evento)
    {
        return transicoes.get(evento);
    }

    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor)
    {
        return transicao(evento, estadoSucessor, null);
    }

    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao)
    {
        transicoes.put(evento, new Transicao<EV,AC>(estadoSucessor, accao));
        return this;
    }
}
