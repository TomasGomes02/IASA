package maqest;

public class Transicao<EV, AC> {

    private Estado<EV, AC> estadoSucessor;
    private AC accao;

    public Transicao(Estado<EV, AC> estadoSucessor, AC accao)
    {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    public Estado<EV, AC> getEstadoSucessor(){return estadoSucessor;}

    public AC getAccao(){return accao;}
}
