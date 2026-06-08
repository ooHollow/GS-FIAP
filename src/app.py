from pathlib import Path
from typing import Dict, Any, List, Tuple
import json

from src.dados import logs_telemetria
from src.motor import MotorAnalise
from src.graphic import gerar_grafico
from src.processo import processar_telemetria
from src.interface import interface

def main() -> None:
    diretorio: Path = Path(__file__).parent.resolve()
    config: Path = diretorio.parent / "config.json"

    with open(config, 'r') as arquivo:
        config_sensores: Dict[str, Dict[str, Any]] = json.load(arquivo)

    motor: MotorAnalise = MotorAnalise(config_sensores)
    logs: List[Any] = logs_telemetria

    historico_sensores = processar_telemetria(logs, motor)
    sensor_escolhido: str = interface(historico_sensores)

    if sensor_escolhido:
        indices, medias = historico_sensores[sensor_escolhido]
        gerar_grafico(sensor_escolhido, indices, medias)


if __name__ == "__main__":
    main()