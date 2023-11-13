package maqest;

import jogo.ambiente.Evento;
import jogo.personagem.Accao;

public class MaquinaEstados<EV, AC> {

    private Estado<EV, AC> estado;

    /*
    * Tipos genéricos:
    *   - EV, Tipo de evento
    *   - AV, Tipo de acção
    * */
    public MaquinaEstados(Estado<EV, AC> estado)
    {
        this.estado = estado;
    }

    public Estado<EV, AC> getEstado(){ return estado; }

    public AC processar(EV evento)
    {
        Transicao<EV, AC> transicao = estado.processar(evento);

        if (transicao != null)
        {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }
        return null;
    };

}
