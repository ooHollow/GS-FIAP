from collections import deque
from typing import Dict, Tuple
from regras import RegraValidacao, ValidacaoLimiteSimples, ValidacaoLimiteDuplo

class MotorAnalise:
    def __init__(self, config: Dict[str, Dict[str, float]]) -> None:
        self.historico: Dict[str, deque[float]] = {sensor: deque(maxlen=3) for sensor in config.keys()}
        self.config: Dict[str, Dict[str, float]] = config
        self.regras: Dict[str, RegraValidacao] = {
            "limite_simples": ValidacaoLimiteSimples(),
            "limite_duplo": ValidacaoLimiteDuplo()
        }

    def adicionar_leitura(self, sensor: str, valor: float) -> Tuple[float, str]:
        buffer: deque[float] = self.historico[sensor]
        buffer.append(valor)
        media: float = sum(buffer) / len(buffer)

        info_limite: Dict[str, float] = self.config[sensor]

        if "alerta_min_inf" in info_limite:
            tipo: str = "limite_duplo"
        else:
            tipo = "limite_simples"

        status: str = self.regras[tipo].validar(media, info_limite)
        return media, status