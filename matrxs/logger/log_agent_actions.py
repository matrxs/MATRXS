from matrxs.logger.logger import GridWorldLogger
from matrxs.grid_world import GridWorld


class LogActions(GridWorldLogger):

    def __init__(self, save_path="", file_name_prefix="", file_extension=".csv", delimeter=";"):
        super().__init__(save_path=save_path, file_name=file_name_prefix, file_extension=file_extension,
                         delimiter=delimeter, log_strategy=1)

    def log(self, grid_world: GridWorld, agent_data: dict):
        log_data = {}
        for agent_id, agent_body in grid_world.registered_agents.items():
            log_data[agent_id] = agent_body.current_action()

        return log_data
