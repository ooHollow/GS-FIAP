from collections import deque
from typing import Dict, Tuple, Any
import regras

class MotorAnalise:
    def __init__(self, config: Dict[str, Dict[str, Any]]) -> None:
        self.historico: Dict[str, deque[float]] = {sensor: deque(maxlen=3) for sensor in config.keys()}
        self.config: Dict[str, Dict[str, float]] = config

    def adicionar_leitura(self, sensor: str, valor: float) -> Tuple[float, str]:
        buffer: deque[float] = self.historico[sensor]
        buffer.append(valor)
        media: float = sum(buffer) / len(buffer)

        info_limite: Dict[str, float] = self.config[sensor]
        nome_classe: str = info_limite["regra_classe"]
        valores: Dict[str, float] = info_limite["parametros"]

        instancia_regra = getattr(regras, nome_classe)()

        status: str = instancia_regra.validar(media, valores)
        return media, status